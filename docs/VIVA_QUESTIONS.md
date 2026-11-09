# Viva Preparation – Restaurant Table Reservation System

1. **What is Django?** Django is the Python web framework used here for URL routing, views, templates, authentication, and database access.
2. **What is a Django model?** The `Reservation` model describes the reservation table and its fields.
3. **What is a migration?** A migration creates or updates the database schema based on Django models.
4. **What is CRUD?** CRUD means Create, Read, Update, and Delete. Customers can perform these operations on their reservations.
5. **Why was MySQL chosen?** MySQL is a relational database that stores structured reservation records and connects them to users.
6. **What is a foreign key?** It links each reservation to the customer who created it.
7. **What does `login_required` do?** It restricts protected views to signed-in users.
8. **How is reservation ownership checked?** The update and delete views look up a reservation using both its ID and the current user.
9. **What is form validation?** It checks submitted values before a reservation is saved.
10. **Why validate on the server as well as in JavaScript?** JavaScript helps users correct mistakes, but it can be bypassed. Django checks submitted data on the server.
11. **How do search and filters work?** Customers can search by name or phone and filter by reservation date or status.
12. **What is Django admin?** It is Django's built-in interface for authorized staff to view and manage application data.
13. **Why use Git?** Git tracks changes to the project source code.
14. **What is GitHub?** GitHub hosts the Git repository for sharing and submission.
15. **What is the difference between authentication and authorization?** Authentication verifies who a user is; authorization determines which records that user can access.
