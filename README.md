# Restaurant Table Reservation System

This full-stack project lets restaurant customers register, log in, and manage table reservations online. It uses Django for the backend, MySQL for data storage, and Bootstrap for the responsive interface.

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
The project uses Python 3.10+, Django 5.2, MySQL 8+, HTML, CSS, Bootstrap 5.0.2, and JavaScript.

## Setup (Windows PowerShell)

1. Install Python 3.10+ and MySQL Server, then open this project folder in VS Code.
2. Create and activate a virtual environment:

   ```powershell
   py -m venv .venv
   .\.venv\Scripts\Activate.ps1
   ```

3. Install the project dependencies:

   ```powershell
   python -m pip install --upgrade pip
   pip install -r requirements.txt
   ```

4. Create the MySQL database and a dedicated project user in MySQL Workbench:

   ```sql
   CREATE DATABASE restaurant_db CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
   CREATE USER 'restaurant_app'@'localhost' IDENTIFIED BY 'replace-with-a-strong-password';
   GRANT ALL PRIVILEGES ON restaurant_db.* TO 'restaurant_app'@'localhost';
   ```

5. Create a local environment file from the example and enter the database credentials and a Django secret key:

   ```powershell
   Copy-Item .env.example .env
   ```

   Keep `.env` local and never commit it; `.gitignore` excludes it. Commit only the placeholder `.env.example`.

6. Create the database tables and an admin account:

   ```powershell
   python manage.py migrate
   python manage.py createsuperuser
   ```

7. Start the development server:

   ```powershell
   python manage.py runserver
   ```

8. Open http://127.0.0.1:8000/ in a browser to register a customer account and create reservations. Django admin is available at http://127.0.0.1:8000/admin/.

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
The sample customer and reservation records were entered through the registration and reservation pages. In MySQL Workbench, select `restaurant_db` and run this query to display the bookings:

```sql
SELECT id, customer_id, customer_name, reservation_date, reservation_time,
       guests, table_number, status
FROM reservations_reservation
WHERE special_request = 'Sample booking entered through the web form'
ORDER BY reservation_date;
```

## Testing
The automated workflow tests use an isolated in-memory SQLite database:

```powershell
python manage.py test reservations --settings=restaurant_project.test_settings
```

All six automated tests passed. Live browser checks against MySQL covered registration, login, reservation creation and updates, dashboard counts, name/phone search, date/status filters, deletion, and logout. Validation, duplicate table/time prevention, and reservation ownership are covered by the automated tests.

## Repository
Source code, migrations, tests, documentation, and screenshots are available at [GitHub](https://github.com/Selva426/Restaurant-table-reservation-system). The local `.env` file is not tracked.

## Important project note
The current version represents restaurant tables with numbers 1–50 and allows customers to enter a reservation time. A future version could use a managed table inventory and defined opening hours.
