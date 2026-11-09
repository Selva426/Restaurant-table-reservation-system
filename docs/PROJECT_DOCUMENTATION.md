# PROJECT DOCUMENTATION
## Restaurant Table Reservation System

**GitHub Repository:** https://github.com/Selva426/Restaurant-table-reservation-system

### 1. Project Introduction
The Restaurant Table Reservation System is a web-based application developed using Python Django. It allows customers to create accounts, log in, reserve restaurant tables, and manage their own bookings. The application stores reservation details in a MySQL database and provides search and filtering facilities.

### 2. Project Objectives
- Provide an online method for customers to reserve restaurant tables.
- Reduce manual reservation record handling.
- Allow customers to view, update and delete their bookings.
- Store reservation data securely in a relational database.
- Demonstrate Python, Django, MySQL and frontend development skills.

### 3. Technologies Used
| Layer | Technology |
|---|---|
| Frontend | HTML5, CSS3, Bootstrap 5 |
| Client-side scripting | JavaScript |
| Backend | Python 3, Django 5.2 |
| Database | MySQL |
| Database adapter | PyMySQL |
| Version control | Git and GitHub |
| Development tools | VS Code, MySQL Workbench |

### 4. System Requirements
**Hardware:** Computer with at least 4 GB RAM and internet access for installing packages and loading the Bootstrap CDN.

**Software:** Windows 10/11 (or compatible OS), Python 3.10+, MySQL Server 8+, web browser, VS Code or another code editor, Git.

### 5. Database Design
The system uses Django's built-in authentication tables and a custom `reservations_reservation` table.

**Reservation fields**
| Field | Type | Description |
|---|---|---|
| id | Big integer, primary key | Unique reservation identifier |
| customer_id | Foreign key | References the Django user |
| customer_name | Varchar(100) | Name for the booking |
| phone | Varchar(15) | Contact number |
| reservation_date | Date | Booking date |
| reservation_time | Time | Booking time |
| guests | Positive small integer | Number of guests (1–20) |
| table_number | Positive small integer | Table number (1–50) |
| special_request | Text | Optional customer request |
| status | Varchar(20) | Pending, Confirmed, Cancelled or Completed |
| created_at | Date/time | Record creation timestamp |

**Relationship:** One user can create many reservations. Each reservation belongs to exactly one user. The customer foreign key uses cascade deletion.

**Validation:** The Django reservation form checks that a table, date and time combination is not already reserved by a non-cancelled booking.

### 6. Module Description
1. **Registration module:** Creates a customer account using Django's built-in user authentication.
2. **Login and logout module:** Authenticates customers and safely ends their session.
3. **Dashboard module:** Displays total, pending and confirmed reservation counts and recent bookings.
4. **Reservation module:** Creates and displays reservation records.
5. **Update module:** Allows the owner of a reservation to edit booking details.
6. **Delete module:** Uses a confirmation page before deleting a reservation.
7. **Search and filter module:** Searches customer name/phone and filters by date/status.
8. **Validation module:** JavaScript provides quick client-side checks; Django forms validate submitted data on the server.
9. **Admin module:** Django admin allows an authorized administrator to inspect and manage reservation records.

### 7. Execution Procedure
1. Install Python and MySQL Server.
2. Create the `restaurant_db` database and `restaurant_app` user in MySQL as described in the README.
3. Create a Python virtual environment and install `requirements.txt`.
4. Copy `.env.example` to `.env` and set your local database credentials and Django secret key. Never commit `.env`.
5. Run `python manage.py migrate`.
6. Run `python manage.py createsuperuser`.
7. Run `python manage.py runserver`.
8. Open `http://127.0.0.1:8000/` in a browser and test the modules.

### 8. Testing
Automated verification: all 6 Django workflow tests pass using an isolated in-memory SQLite test database. They cover registration/login/logout, protected pages, reservation create/update/delete, dashboard counts, name and phone search, date/status filtering, form validation, duplicate table/time prevention, cancelled bookings, and reservation ownership.

Live MySQL verification: Django's system check and read-only migration check passed. In a browser, registration, dashboard, reservation creation and update, phone/date/status filtering, deletion, and logout passed. Temporary demonstration accounts and bookings were removed. The automated SQLite tests cover validation, duplicate prevention, and ownership checks.

Perform the following tests and record the actual result:
- Valid customer registration and login.
- Successful reservation creation.
- Reservation list displays saved records.
- Update and delete operations.
- Search by customer name and phone.
- Date and status filtering.
- Past date and invalid phone validation.
- Duplicate table/date/time reservation rejection.
- Access control: a customer cannot edit another customer's reservation.
- Logout and protected-page access.

### 9. Screenshots
The following screenshots were captured from the running application. The dashboard, reservation list, and admin screenshots show fictional sample bookings entered through the web forms. The local sample account and bookings remain in MySQL for the database screenshot; do not use demo credentials for deployment.

**Figure 1: Registration page**

![Registration page](../screenshots/registration.png)

**Figure 2: Login page**

![Login page](../screenshots/login.png)

**Figure 3: Dashboard**

![Dashboard](../screenshots/dashboard.png)

**Figure 4: New reservation form**

![New reservation form](../screenshots/reservation-form.png)

**Figure 5: Reservation list with search and filters**

![Reservation list](../screenshots/reservation-list.png)

**Figure 6: Edit reservation page**

![Edit reservation](../screenshots/reservation-edit.png)

**Figure 7: Delete confirmation page**

![Delete confirmation](../screenshots/reservation-delete.png)

**Figure 8: Django admin reservation list**

![Django admin reservations](../screenshots/admin-reservations.png)

**Figure 9: MySQL database/table view**

![MySQL Workbench reservation table](../screenshots/mysql-database.png)

### 10. Conclusion
The Restaurant Table Reservation System demonstrates the development of a Python full-stack web application using Django and MySQL. It includes authentication, reservation management, CRUD operations, search, filtering, validation and a responsive user interface. The project provides practical experience in backend development, database connectivity and frontend-backend integration.

### 11. Future Enhancements
- Real-time table availability calendar.
- Email or SMS booking confirmation.
- Restaurant opening-hour and seating-capacity management.
- Online payment integration.
- Administrator approval workflow.
