from django.views.generic import ListView, DetailView, CreateView, UpdateView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Book
from .forms import BookForm
from .mixins import UserPermissionMixin, LoggingMixin

class BookListView(LoginRequiredMixin, ListView):
    model = Book
    template_name = "books/book_list.html"
    context_object_name = "books"
    paginate_by = 6  # Adjust the number of books per page

    def get_queryset(self):
        """Allow searching by title."""
        query = self.request.GET.get("q", "")
        queryset = Book.objects.all()
        if query:
            queryset = queryset.filter(title__icontains=query)
        return queryset


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
