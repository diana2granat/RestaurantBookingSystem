from django.urls import path
from booking.views.home_view import home
from booking.views.menu_view import menu
from booking.views.booking_view import book
from booking.views.table_view import tables
from django.contrib.auth import views as auth_views



urlpatterns = [
    path("", home, name="home"),
    path("menu/", menu, name="menu"),
    path("book/", book, name="book"),
    path("tables/", tables, name="tables"),
    path("login/", auth_views.LoginView.as_view(template_name="login.html"),name="login") #using the view of the Dajngo

]