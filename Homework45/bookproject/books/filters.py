import django_filters
from .models import Book

class BookFilter(django_filters.FilterSet):
    title = django_filters.CharFilter(lookup_expr='icontains')  # Case-insensitive title search
    author = django_filters.CharFilter(lookup_expr='icontains')  # Search by author name
    published_year = django_filters.NumberFilter()  # Exact match for published year
    min_price = django_filters.NumberFilter(field_name="price", lookup_expr='gte')  # Minimum price
    max_price = django_filters.NumberFilter(field_name="price", lookup_expr='lte')  # Maximum price

    class Meta:
        model = Book
        fields = ['title', 'author', 'published_year', 'min_price', 'max_price']
