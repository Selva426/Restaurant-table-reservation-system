from django import forms
from django.utils import timezone
from .models import Reservation

class ReservationForm(forms.ModelForm):
    class Meta:
        model = Reservation
        fields = [
            "customer_name", "phone", "reservation_date", "reservation_time",
            "guests", "table_number", "special_request"
        ]
        widgets = {
            "reservation_date": forms.DateInput(attrs={"type": "date", "class": "form-control"}),
            "reservation_time": forms.TimeInput(attrs={"type": "time", "class": "form-control"}),
            "special_request": forms.Textarea(attrs={"rows": 3, "class": "form-control"}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs.setdefault("class", "form-control")

    def clean_reservation_date(self):
        value = self.cleaned_data["reservation_date"]
        if value < timezone.localdate():
            raise forms.ValidationError("Reservation date cannot be in the past.")
        return value

    def clean_phone(self):
        value = self.cleaned_data["phone"].strip()
        digits = "".join(ch for ch in value if ch.isdigit())
        if len(digits) < 10 or len(digits) > 15:
            raise forms.ValidationError("Enter a valid phone number (10–15 digits).")
        return value

    def clean(self):
        cleaned = super().clean()
        date = cleaned.get("reservation_date")
        time = cleaned.get("reservation_time")
        table = cleaned.get("table_number")
        if date and time and table:
            qs = Reservation.objects.filter(
                reservation_date=date, reservation_time=time,
                table_number=table
            ).exclude(status="Cancelled")
            if self.instance.pk:
                qs = qs.exclude(pk=self.instance.pk)
            if qs.exists():
                raise forms.ValidationError("That table is already reserved for this date and time.")
        return cleaned
