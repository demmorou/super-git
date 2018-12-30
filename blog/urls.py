from django.conf.urls import url
from blog.views import *

app_name = 'blog'

urlpatterns = [
    url(r'^$', index, name="index")
]