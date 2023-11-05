from rest_framework.generics import ListAPIView
from api.models import Book
from api.serializers import BookSerializer

class BestRatingBooks(ListAPIView):
    serializer_class = BookSerializer

    def get_queryset(self):
        nums = self.request.query_params.get('num-books', None)

        if nums is not None:
            nums = int(nums)
            return Book.objects.all().order_by('-rating')[:nums]
        return Book.objects.all().order_by('-rating')


