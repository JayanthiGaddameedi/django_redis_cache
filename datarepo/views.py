from django.shortcuts import render

from django.conf import settings
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.response import Response
from django.views.decorators.cache import cache_page
from .models import Newsfeed


# Create your views here.


@cache_page(settings.CACHE_TTL)
@api_view(['GET'])
def list_newsfeed(request):
    all_newsfeeds = Newsfeed.objects.all()
    data = []
    for item in all_newsfeeds:
        temp = {
            'news_id': item.id,
            'news': item.news
        }
        data.append(temp)
    context = {
        'data': data
    }
    return Response(context, status=status.HTTP_200_OK)

