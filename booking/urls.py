from django.urls import path
from booking.views.home_view import home
from booking.views.menu_view import menu
from booking.views.booking_view import book
from booking.views.table_view import tables



urlpatterns = [
    path("", home),
    path("menu/", menu),
    path("book/", book),
    path("tables/", tables)

]