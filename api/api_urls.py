import json

from django.urls import path, include
from rest_framework.routers import DefaultRouter
from api.endpoints.NewestBookView import NewestBooksView
from api.endpoints.GetAllBooks import GetAllBooks
from api.endpoints.BestRatingBooks import BestRatingBooks
from api.endpoints.GetBookById import GetBookById

from . import views



router = DefaultRouter()
urlSetting = json.loads(open("./api/appsetting.json").read())
urlSetting = urlSetting['ApiSettings']



urlpatterns = [
    path('', include(router.urls)),
    path(urlSetting['NewestBooksUrl'], NewestBooksView.as_view(), name='newest-books'),
    path(urlSetting['GetAllUrl'], GetAllBooks.as_view(), name='get-all'),
    path(urlSetting['BestRatingUrl'], BestRatingBooks.as_view(), name='best-rating'),
    path(urlSetting['GetBookByIdUrl'], GetBookById.as_view(), name = 'getBookById'),
    path("book/<int:pk>/"+urlSetting['UpdateBookUrl'], views.update_items, name='update-book'),
    path("book/<int:pk>/"+urlSetting['DeleteBookUrl'], views.delete_items, name='delete-book'),


]
