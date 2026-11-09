from datetime import date
from django.contrib import messages
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.db.models import Q
from django.shortcuts import get_object_or_404, redirect, render
from django.utils import timezone
from .forms import ReservationForm
from .models import Reservation

def register_view(request):
    if request.user.is_authenticated:
        return redirect("dashboard")
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Your account has been created.")
            return redirect("dashboard")
    else:
        form = UserCreationForm()
    return render(request, "registration/register.html", {"form": form})

@login_required
def dashboard(request):
    reservations = Reservation.objects.filter(customer=request.user)
    context = {
        "total_count": reservations.count(),
        "pending_count": reservations.filter(status="Pending").count(),
        "confirmed_count": reservations.filter(status="Confirmed").count(),
        "recent_reservations": reservations[:5],
    }
    return render(request, "reservations/dashboard.html", context)

@login_required
def reservation_list(request):
    reservations = Reservation.objects.filter(customer=request.user)
    query = request.GET.get("q", "").strip()
    date_filter = request.GET.get("date", "").strip()
    date_error = ""
    status_filter = request.GET.get("status", "").strip()
    if query:
        reservations = reservations.filter(
            Q(customer_name__icontains=query) | Q(phone__icontains=query)
        )
    if date_filter:
        try:
            parsed_date = date.fromisoformat(date_filter)
        except ValueError:
            date_error = "Enter a valid date."
        else:
            reservations = reservations.filter(reservation_date=parsed_date)
    if status_filter:
        reservations = reservations.filter(status=status_filter)
    return render(request, "reservations/reservation_list.html", {
        "reservations": reservations,
        "q": query, "date_filter": date_filter, "date_error": date_error,
        "status_filter": status_filter,
        "statuses": Reservation.STATUS_CHOICES,
    })

@login_required
def reservation_create(request):
    if request.method == "POST":
        form = ReservationForm(request.POST)
        if form.is_valid():
            reservation = form.save(commit=False)
            reservation.customer = request.user
            reservation.save()
            messages.success(request, "Reservation created successfully.")
            return redirect("reservation_list")
    else:
        form = ReservationForm()
    return render(request, "reservations/reservation_form.html", {
        "form": form, "page_title": "Make a Reservation"
    })

@login_required
def reservation_update(request, pk):
    reservation = get_object_or_404(Reservation, pk=pk, customer=request.user)
    if request.method == "POST":
        form = ReservationForm(request.POST, instance=reservation)
        if form.is_valid():
            form.save()
            messages.success(request, "Reservation updated successfully.")
            return redirect("reservation_list")
    else:
        form = ReservationForm(instance=reservation)
    return render(request, "reservations/reservation_form.html", {
        "form": form, "page_title": "Edit Reservation"
    })

@login_required
def reservation_delete(request, pk):
    reservation = get_object_or_404(Reservation, pk=pk, customer=request.user)
    if request.method == "POST":
        reservation.delete()
        messages.success(request, "Reservation deleted.")
        return redirect("reservation_list")
    return render(request, "reservations/reservation_confirm_delete.html", {
        "reservation": reservation
    })
