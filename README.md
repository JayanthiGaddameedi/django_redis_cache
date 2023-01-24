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
3. to check redis connected - `python3 manage.py shell`
   1. $ `redis-cli ping`
   2. then it should return `PONG`
4. to test redis is working fine..!!
    1. $ `redis-cli` --> it will return `127.0.0.1:6379>`
    2. 127.0.0.1:6379> `set test "hey jayanthi"`
    3.  then returns --> 127.0.0.1:6379>`OK`
    4. 127.0.0.1:6379>`get test`
    5.  then returns --> 127.0.0.1:6379>`hey jayanthi`
5. to know about cache -- use the below commands in the shell
   `python3 manage.py shell` this will open the shell for you.
6. then to know the cache `from django.core.cache import cache`
    1. to know the list of keys present in the cache `cache.keys('*')`
    2. to clear the cache `cache.clear()`
