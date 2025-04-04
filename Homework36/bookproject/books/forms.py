from django import forms
from .models import Book

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ["title", "author", "category", "description", "published_date", "cover_image"]
        widgets = {
            "published_date": forms.DateInput(attrs={"type": "date"}),
        }
