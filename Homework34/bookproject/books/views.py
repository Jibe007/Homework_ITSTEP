from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from .models import Book
from .forms import BookForm


def book_list(request):
    books = Book.objects.all()
    return render(request, "books/book_list.html", {"books": books})


def book_detail(request, book_id):
    book = Book.objects.get(id=book_id)
    return render(request, "books/book_detail.html", {"book": book})


def add_book(request):
    if request.method == "POST":
        form = BookForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect("book_list")
    else:
        form = BookForm()

    return render(request, "books/add_book.html", {"form": form})
