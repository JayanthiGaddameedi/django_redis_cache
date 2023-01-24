from django.contrib import admin
from .models import Newsfeed

# Register your models here.


@admin.register(Newsfeed)
class NewsfeedAdmin(admin.ModelAdmin):
    list_display = ("id", "news")
