from rest_framework.generics import ListAPIView
from api.models import Book
from api.serializers import BookSerializer

class GetBookById(ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

    def get_queryset(self):
        queryset = Book.objects.all()
        iden = self.request.query_params.get('id', None)
        if iden is not None:
            iden = int(iden)
            return Book.objects.filter(id = iden)
        return "ssij"
