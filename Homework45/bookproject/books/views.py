from django.views.generic import ListView, DetailView, CreateView, UpdateView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django_filters.views import FilterView
from drf_yasg.openapi import Response
from drf_yasg.utils import swagger_auto_schema
from rest_framework.generics import ListAPIView
from rest_framework.filters import OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.views import APIView

from .models import Book
from .forms import BookForm
from .serializers import BookSerializer
from .mixins import UserPermissionMixin, LoggingMixin
from .filters import BookFilter
from .custom_pagination import CustomPagination


# ✅ Class-based view for HTML rendering (with pagination & search)
class BookListView(LoginRequiredMixin, ListView):
    model = Book
    template_name = "books/book_list.html"
    context_object_name = "books"
    paginate_by = 6  # Pagination for Django template-based views

    def get_queryset(self):
        """Allow searching by title."""
        query = self.request.GET.get("q", "")
        queryset = Book.objects.all()
        if query:
            queryset = queryset.filter(title__icontains=query)
        return queryset


class BookListAPIView(APIView):
    @swagger_auto_schema(operation_description="Get all books")
    def get(self, request):
        books = Book.objects.all()
        serializer = BookSerializer(books, many=True)
        return Response(serializer.data)


class BookDetailAPIView(APIView):
    @swagger_auto_schema(operation_description="Get a single book by ID")
    def get(self, request, pk):
        try:
            book = Book.objects.get(pk=pk)
        except Book.DoesNotExist:
            return Response({"detail": "Not found."}, status=404)

        serializer = BookSerializer(book)
        return Response(serializer.data)

# # ✅ API View with Pagination & Filtering (RESTful API)
# class BookListAPIView(ListAPIView):
#     queryset = Book.objects.all()
#     serializer_class = BookSerializer
#     pagination_class = CustomPagination  # Custom paginator for API
#     filter_backends = [DjangoFilterBackend, OrderingFilter]  # Filtering and sorting
#     filterset_class = BookFilter  # Custom filter class
#     ordering_fields = ['title', 'published_year', 'price']  # Sorting options


class BookDetailView(LoginRequiredMixin, DetailView):
    model = Book
    template_name = "books/book_detail.html"
    context_object_name = "book"


class BookCreateView(LoginRequiredMixin, UserPermissionMixin, LoggingMixin, CreateView):
    model = Book
    form_class = BookForm
    template_name = "books/add_book.html"
    success_url = reverse_lazy("book_list")
    permission_required = "books.add_book"

    def form_valid(self, form):
        response = super().form_valid(form)
        self.log_action(f"Book added: {self.object.title} (ID: {self.object.id})")
        return response


class BookUpdateView(LoginRequiredMixin, UserPermissionMixin, LoggingMixin, UpdateView):
    model = Book
    form_class = BookForm
    template_name = "books/update_book.html"
    success_url = reverse_lazy("book_list")
    permission_required = "books.change_book"

    def form_valid(self, form):
        response = super().form_valid(form)
        self.log_action(f"Book updated: {self.object.title} (ID: {self.object.id})")
        return response
