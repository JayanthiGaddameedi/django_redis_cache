# django_redis_cache


##### packages

1. django
2. django debug toolbar
3. django-redis
4. redis
5. django rest framework

##### Get started

1. Install all the requirements - `pip install -r requirements.txt`
2. In settings.py add the following lines.
    1. ```
       Installed_apps = [
           'debug_toolbar'
       ]
       MIDDLEWARE = [
           'debug_toolbar.middleware.DebugToolbarMiddleware'
       ]
       ```
    2. Add these cache lines in settings.py
       ``` 
       CACHES = {
       "default": {
           "BACKEND": "django_redis.cache.RedisCache",
            "LOCATION": "redis://127.0.0.1:6379/1",
            "OPTIONS": {
                "CLIENT_CLASS": "django_redis.client.DefaultClient"
             },
            "KEY_PREFIX": "django_cache"
           }
       }
       
       #  Cache time to live is 15 minutes
       CACHE_TTL = 60 * 15
       ```
3. models.py
    ```
    class Newsfeed(models.Model):
        news = models.CharField(max_length=255)
   ```
4. admin.py
   ```
   from .models import Newsfeed
   
   @admin.register(Newsfeed)
   class NewsfeedAdmin(admin.ModelAdmin):
   list_display = ('id', 'news')

   ```
5. views.py
    ```
    from django.conf import settings
    from django.shortcuts import render
    from rest_framework.decorators import api_view
    from rest_framework import status
    from rest_framework.response import Response
    from django.views.decorators.cache import cache_page
    from .models import Newsfeed
    
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
         context = {'data': data}
        return Response(context, status=status.HTTP_200_OK)

    ```
6. urls.py
   ```
   from datarepo.views import list_newsfeed
   
    urlpatterns = [
        path('list_newsfeed/', list_newsfeed)
    ]
   ```
7. To check redis connected
   ```
   $ redis-cli ping
   PONG
   ```
8. To test redis is working fine..!!
   ```
    $ redis-cli
    127.0.0.1:6379> set test "hello world"
    127.0.0.1:6379> OK
    127.0.0.1:6379> get test
    127.0.0.1:6379> "hello world"
    ```
9. To know the cache keys
    ```
   $ python3 manage.py shell
   >>> from django.core.cache import cache
   >>> cache.keys('*')  # this line gives the list of keys presenet in cache

   ```
10. To clear the cache
    ```
    >>> from django.core.cache import cache
    >>> cache.clear()
       True
    ```