from django.core.paginator import Paginator
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth.models import Group
from django.db.models import Q
from .models import Book
from .forms import BookForm
import logging


# Configure logging
logger = logging.getLogger(__name__)

def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            default_group = Group.objects.get(name="Default")  # Assign to Default group
            user.groups.add(default_group)
            login(request, user)
            return redirect("book_list")
    else:
        form = UserCreationForm()
    return render(request, "books/register.html", {"form": form})


def user_login(request):
    if request.method == "POST":
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect("book_list")
    else:
        form = AuthenticationForm()
    return render(request, "books/login.html", {"form": form})


def user_logout(request):
    logout(request)
    return redirect("login")


@login_required
def book_list(request):
    query = request.GET.get("q", "")  # Get search query from GET request
    books = Book.objects.all()

    if query:
        books = books.filter(Q(title__icontains=query))  # Filter books by title

    return render(request, "books/book_list.html", {"books": books, "query": query})


@login_required
def book_detail(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    books = Book.objects.all()


    paginator = Paginator(books, 3)
    page_number = request.GET.get('page')
    books_page = paginator.get_page(page_number)

    if request.method == "POST":  # Handle book deletion
        if request.user.has_perm("books.delete_book"):
            book.delete()
            return redirect("book_list")  # Redirect after deletion

    return render(request, "books/book_detail.html", {"book": book})


@login_required
def add_book(request):
    if not request.user.has_perm("books.add_book"):
        return redirect("book_list")  # Restrict access

    if request.method == "POST":
        form = BookForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect("book_list")
    else:
        form = BookForm()

    return render(request, "books/add_book.html", {"form": form})


@login_required
@permission_required('books.change_book', raise_exception=True)
def update_book(request, book_id):
    book = get_object_or_404(Book, id=book_id)

    if request.method == "POST":
        form = BookForm(request.POST, request.FILES, instance=book)
        if form.is_valid():
            form.save()
            logger.info(f"Book updated: {book.title} (ID: {book.id}) by {request.user}")
            return redirect('book_detail', book_id=book.id)
        else:
            logger.warning(f"Invalid form submitted for book update (ID: {book.id}) by {request.user}")
    else:
        form = BookForm(instance=book)

    return render(request, 'books/update_book.html', {'form': form, 'book': book})


