from rest_framework.generics import ListAPIView
from api.models import Book
from api.serializers import BookSerializer

class NewestBooksView(ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

    def get_queryset(self):
        queryset = Book.objects.all()
        nums = self.request.query_params.get('num-books', None)
        if nums is not None:
            nums = int(nums)
            return Book.objects.all().order_by('-date_of_publishing')[:nums]
        return Book.objects.all().order_by('-date_of_publishing')
