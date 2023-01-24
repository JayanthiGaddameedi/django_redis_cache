from django.contrib import admin
from django.urls import path

from datarepo.views import list_newsfeed

urlpatterns = [
    path('admin/', admin.site.urls),
    path('list_newsfeed/', list_newsfeed),
]
