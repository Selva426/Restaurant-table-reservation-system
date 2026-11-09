from django.conf import settings
from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
from django.utils import timezone

class Reservation(models.Model):
    STATUS_CHOICES = [
        ("Pending", "Pending"),
        ("Confirmed", "Confirmed"),
        ("Cancelled", "Cancelled"),
        ("Completed", "Completed"),
    ]

    customer = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="reservations"
    )
    customer_name = models.CharField(max_length=100)
    phone = models.CharField(max_length=15)
    reservation_date = models.DateField()
    reservation_time = models.TimeField()
    guests = models.PositiveSmallIntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(20)]
    )
    table_number = models.PositiveSmallIntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(50)]
    )
    special_request = models.TextField(blank=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default="Pending")
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-reservation_date", "-reservation_time"]

    def __str__(self):
        return f"{self.customer_name} - Table {self.table_number} - {self.reservation_date}"

    @property
    def is_past(self):
        return self.reservation_date < timezone.localdate()
