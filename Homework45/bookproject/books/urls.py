from django.contrib.auth.views import LogoutView, LoginView
from django.urls import path, include
from rest_framework import permissions

from .views import BookListView, BookDetailView, BookCreateView, BookUpdateView
from .views import BookListAPIView, BookDetailAPIView  # Include all your API views
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

# Swagger schema view
schema_view = get_schema_view(
    openapi.Info(
        title="Book API",
        default_version="v1",
        description="API documentation for the Book project",
    ),
    public=True,
    permission_classes=[permissions.AllowAny],
)

urlpatterns = [
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path("", BookListView.as_view(), name="book_list"),
    path("book/<int:pk>/", BookDetailView.as_view(), name="book_detail"),
    path("book/add/", BookCreateView.as_view(), name="add_book"),
    path("book/<int:pk>/edit/", BookUpdateView.as_view(), name="update_book"),
    path('accounts/', include('django.contrib.auth.urls')),
    path("swagger/", schema_view.with_ui("swagger", cache_timeout=0), name="schema-swagger-ui"),
    path("books/", BookListAPIView.as_view(), name="book_list_api"),
    path("books/<int:pk>/", BookDetailAPIView.as_view(), name="book_detail_api"),
]




