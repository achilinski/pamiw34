from rest_framework.generics import ListAPIView
from api.models import Book
from api.serializers import BookSerializer

class GetAllBooks(ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

    def get_queryset(self):
        queryset = Book.objects.all()
        nums = self.request.query_params.get('num-books', None)
        if nums is not None:
            nums = int(nums)
            return Book.objects.all()[:nums]
        return Book.objects.all()
