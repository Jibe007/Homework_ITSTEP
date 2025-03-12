from django.contrib.auth.views import LogoutView, LoginView
from django.urls import path
from .views import BookListView, BookDetailView, BookCreateView, BookUpdateView

urlpatterns = [
    path('login/', LoginView.as_view(), name='login'),  # Built-in login view
    path('logout/', LogoutView.as_view(), name='logout'),  # Built-in logout view
    path("", BookListView.as_view(), name="book_list"),
    path("book/<int:pk>/", BookDetailView.as_view(), name="book_detail"),
    path("book/add/", BookCreateView.as_view(), name="add_book"),
    path("book/<int:pk>/edit/", BookUpdateView.as_view(), name="update_book"),
]


