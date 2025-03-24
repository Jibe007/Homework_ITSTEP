from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response

class CustomPagination(PageNumberPagination):
    page_size = 5  # Default number of items per page
    page_size_query_param = 'page_size'  # Allow dynamic page size
    max_page_size = 20  # Prevent excessive queries

    def get_paginated_response(self, data):
        return Response({
            'total_pages': self.page.paginator.num_pages,
            'total_items': self.page.paginator.count,
            'current_page': self.page.number,
            'next': self.get_next_link(),
            'previous': self.get_previous_link(),
            'results': data
        })
