from django.urls import path
from .views import book_list, book_detail, add_book, register, user_login, user_logout, update_book

urlpatterns = [
    path("", book_list, name="book_list"),
    path("book/<int:book_id>/", book_detail, name="book_detail"),
    path("add/", add_book, name="add_book"),
    path("register/", register, name="register"),
    path("login/", user_login, name="login"),
    path("logout/", user_logout, name="logout"),
    path('book/update/<int:book_id>/', update_book, name='update_book'),
]

