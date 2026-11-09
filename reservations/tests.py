from datetime import timedelta

from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse
from django.utils import timezone

from .models import Reservation


User = get_user_model()
PASSWORD = "TrainingProjectPass123!"


class ReservationWorkflowTests(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username="customer", password=PASSWORD)
        self.client.login(username="customer", password=PASSWORD)

    def reservation_data(self, **overrides):
        data = {
            "customer_name": "Test Customer",
            "phone": "9876543210",
            "reservation_date": (timezone.localdate() + timedelta(days=2)).isoformat(),
            "reservation_time": "18:00",
            "guests": "2",
            "table_number": "7",
            "special_request": "",
        }
        data.update(overrides)
        return data

    def make_reservation(self, **overrides):
        status = overrides.pop("status", "Pending")
        data = self.reservation_data(**overrides)
        return Reservation.objects.create(
            customer=self.user,
            customer_name=data["customer_name"],
            phone=data["phone"],
            reservation_date=data["reservation_date"],
            reservation_time=data["reservation_time"],
            guests=data["guests"],
            table_number=data["table_number"],
            special_request=data["special_request"],
            status=status,
        )

    def test_registration_login_logout_and_protected_dashboard(self):
        self.client.post(reverse("logout"))
        response = self.client.post(reverse("register"), {
            "username": "new_customer",
            "password1": PASSWORD,
            "password2": PASSWORD,
        })
        self.assertRedirects(response, reverse("dashboard"))
        self.assertTrue(User.objects.filter(username="new_customer").exists())
        self.client.post(reverse("logout"))
        response = self.client.get(reverse("dashboard"))
        self.assertRedirects(response, f"{reverse('login')}?next={reverse('dashboard')}")
        response = self.client.post(reverse("login"), {
            "username": "new_customer",
            "password": PASSWORD,
        })
        self.assertRedirects(response, reverse("dashboard"))

    def test_reservation_create_update_search_filter_and_delete(self):
        response = self.client.post(reverse("reservation_create"), self.reservation_data())
        self.assertRedirects(response, reverse("reservation_list"))
        reservation = Reservation.objects.get()

        response = self.client.get(reverse("dashboard"))
        self.assertEqual(response.context["total_count"], 1)

        response = self.client.post(
            reverse("reservation_update", args=[reservation.pk]),
            self.reservation_data(customer_name="Updated Customer"),
        )
        self.assertRedirects(response, reverse("reservation_list"))
        reservation.refresh_from_db()
        self.assertEqual(reservation.customer_name, "Updated Customer")

        for search in ("Updated Customer", "9876543210"):
            with self.subTest(search=search):
                response = self.client.get(reverse("reservation_list"), {
                    "q": search,
                    "date": reservation.reservation_date.isoformat(),
                    "status": "Pending",
                })
                self.assertEqual(list(response.context["reservations"]), [reservation])

        response = self.client.get(reverse("reservation_delete", args=[reservation.pk]))
        self.assertEqual(response.status_code, 200)
        response = self.client.post(reverse("reservation_delete", args=[reservation.pk]))
        self.assertRedirects(response, reverse("reservation_list"))
        self.assertFalse(Reservation.objects.exists())

    def test_invalid_date_phone_and_guest_count_are_rejected(self):
        invalid_submissions = [
            self.reservation_data(
                reservation_date=(timezone.localdate() - timedelta(days=1)).isoformat()
            ),
            self.reservation_data(phone="123"),
            self.reservation_data(guests="21"),
        ]
        for data in invalid_submissions:
            with self.subTest(data=data):
                response = self.client.post(reverse("reservation_create"), data)
                self.assertEqual(response.status_code, 200)
                self.assertTrue(response.context["form"].errors)
        self.assertFalse(Reservation.objects.exists())

    def test_duplicate_table_and_time_are_rejected(self):
        existing = self.make_reservation()
        User.objects.create_user(username="another", password=PASSWORD)
        self.client.logout()
        self.client.login(username="another", password=PASSWORD)

        response = self.client.post(
            reverse("reservation_create"),
            self.reservation_data(table_number=str(existing.table_number)),
        )
        self.assertEqual(response.status_code, 200)
        self.assertIn("already reserved", str(response.context["form"].non_field_errors()))
        self.assertEqual(Reservation.objects.count(), 1)

    def test_cancelled_reservation_does_not_block_a_table(self):
        existing = self.make_reservation(status="Cancelled")
        User.objects.create_user(username="another", password=PASSWORD)
        self.client.logout()
        self.client.login(username="another", password=PASSWORD)

        response = self.client.post(
            reverse("reservation_create"),
            self.reservation_data(table_number=str(existing.table_number)),
        )
        self.assertRedirects(response, reverse("reservation_list"))
        self.assertEqual(Reservation.objects.count(), 2)

    def test_users_cannot_edit_or_delete_another_users_reservation(self):
        reservation = self.make_reservation()
        User.objects.create_user(username="another", password=PASSWORD)
        self.client.logout()
        self.client.login(username="another", password=PASSWORD)

        edit_response = self.client.get(reverse("reservation_update", args=[reservation.pk]))
        delete_response = self.client.post(reverse("reservation_delete", args=[reservation.pk]))
        self.assertEqual(edit_response.status_code, 404)
        self.assertEqual(delete_response.status_code, 404)
        self.assertTrue(Reservation.objects.filter(pk=reservation.pk).exists())