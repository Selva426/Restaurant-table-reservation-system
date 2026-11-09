document.addEventListener("DOMContentLoaded", function () {
  const form = document.getElementById("reservationForm");
  if (!form) return;

  form.addEventListener("submit", function (event) {
    const dateInput = form.querySelector('[name="reservation_date"]');
    const guestsInput = form.querySelector('[name="guests"]');
    const tableInput = form.querySelector('[name="table_number"]');
    const phoneInput = form.querySelector('[name="phone"]');
    const errorBox = document.getElementById("clientError");
    const today = new Date();
    const localToday = new Date(today.getTime() - today.getTimezoneOffset() * 60000)
      .toISOString().slice(0, 10);

    let error = "";
    if (dateInput && dateInput.value && dateInput.value < localToday) {
      error = "Please choose today or a future date.";
    } else if (guestsInput && (+guestsInput.value < 1 || +guestsInput.value > 20)) {
      error = "Guest count must be between 1 and 20.";
    } else if (tableInput && (+tableInput.value < 1 || +tableInput.value > 50)) {
      error = "Choose a table number between 1 and 50.";
    } else if (phoneInput && phoneInput.value.replace(/\D/g, "").length < 10) {
      error = "Enter a valid phone number.";
    }

    if (error) {
      event.preventDefault();
      errorBox.textContent = error;
    } else if (errorBox) {
      errorBox.textContent = "";
    }
  });
});
