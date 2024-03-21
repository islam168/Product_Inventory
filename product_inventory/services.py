from rest_framework.pagination import PageNumberPagination


# Pagination
class LargePagination(PageNumberPagination):
    page_size = 10  # Количество записей на одной странице
