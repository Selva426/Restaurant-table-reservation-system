from django.contrib.auth import views as auth_views
from django.urls import path
from . import views

urlpatterns = [
    path("", views.dashboard, name="dashboard"),
    path("register/", views.register_view, name="register"),
    path("login/", auth_views.LoginView.as_view(template_name="registration/login.html"), name="login"),
    path("logout/", auth_views.LogoutView.as_view(), name="logout"),
    path("reservations/", views.reservation_list, name="reservation_list"),
    path("reservations/add/", views.reservation_create, name="reservation_create"),
    path("reservations/<int:pk>/edit/", views.reservation_update, name="reservation_update"),
    path("reservations/<int:pk>/delete/", views.reservation_delete, name="reservation_delete"),
]
