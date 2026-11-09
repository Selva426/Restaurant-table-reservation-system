# Restaurant Table Reservation System

A Django-based full-stack web application for customer registration, login and restaurant table reservations.

## Features
- Customer registration, login and logout
- Customer dashboard with reservation counts
- Create, view, edit and delete reservations
- Search by customer name or phone
- Filter by reservation date and status
- Server-side validation and JavaScript client-side validation
- MySQL database integration
- Django admin interface
- Responsive Bootstrap 5 UI
- Users can only view and manage their own reservations

## Technology
Python 3.10+, Django 5.2, MySQL 8+, HTML, CSS, Bootstrap 5.0.2, JavaScript.

## Setup (Windows PowerShell)

1. Install Python 3.10+ and MySQL Server. During MySQL setup, remember the database password.
2. Open this project folder in VS Code.
3. Create and activate a virtual environment:

   ```powershell
   py -m venv .venv
   .\.venv\Scripts\Activate.ps1
   ```

4. Install dependencies:

   ```powershell
   python -m pip install --upgrade pip
   pip install -r requirements.txt
   ```

5. Create the MySQL database and a dedicated project user. Open MySQL Workbench or the MySQL command line and run:

   ```sql
   CREATE DATABASE restaurant_db CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
   CREATE USER 'restaurant_app'@'localhost' IDENTIFIED BY 'replace-with-a-strong-password';
   GRANT ALL PRIVILEGES ON restaurant_db.* TO 'restaurant_app'@'localhost';
   ```

6. Create your local environment file from the example and edit it with your own credentials and a secret key:

   ```powershell
   Copy-Item .env.example .env
   ```

   Replace the placeholder values in `.env`. Never commit `.env`; it is excluded by `.gitignore`. `.env.example` is safe to commit.

7. Create the database tables and admin account:

   ```powershell
   python manage.py migrate
   python manage.py createsuperuser
   ```

8. Start the development server:

   ```powershell
   python manage.py runserver
   ```

9. Open http://127.0.0.1:8000/ in your browser. Register a normal customer account, then create a reservation. Admin: http://127.0.0.1:8000/admin/

## Main URL routes
- `/` dashboard (login required)
- `/register/` customer registration
- `/login/` login
- `/logout/` logout (POST)
- `/reservations/` list, search and filter
- `/reservations/add/` create reservation
- `/reservations/<id>/edit/` update reservation
- `/reservations/<id>/delete/` delete reservation
- `/admin/` Django administration

## MySQL screenshot
Sample customer and reservation records for the database screenshot were entered through the registration and reservation pages. With the app running, register a user and create reservations using the website forms. In MySQL Workbench, select `restaurant_db` and run this query to display the sample bookings:

```sql
SELECT id, customer_id, customer_name, reservation_date, reservation_time,
       guests, table_number, status
FROM reservations_reservation
WHERE special_request = 'Sample booking entered through the web form'
ORDER BY reservation_date;
```

## Test checklist
- Run automated workflow tests with an isolated in-memory SQLite database:

   ```powershell
   python manage.py test reservations --settings=restaurant_project.test_settings
   ```

- Register a new user and log in.
- Create a reservation with a future date.
- Verify it appears in the reservation list and dashboard.
- Edit the reservation and verify the changes.
- Search by name or phone and filter by date/status.
- Delete a reservation and confirm it disappears.
- Try a past date, invalid phone, guest count outside 1–20, and an already-booked table/time. The form should reject invalid input.
- Create two customer accounts and verify that one cannot access the other's reservation by changing the URL ID.
- Log out and verify protected pages redirect to login.

## GitHub upload
See `docs/GITHUB_SUBMISSION.md` for commands. Confirm `.env` is not staged and only `.env.example` is included. Capture genuine screenshots and add your repository link before submitting.

## Important project note
This is an academic starter implementation. The restaurant's table inventory and opening hours are represented by table numbers 1–50 and user-entered times. Adjust these rules to match the restaurant scenario you demonstrate.
