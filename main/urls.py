from django.contrib import admin
from django.urls import path,include

from . import views
urlpatterns = [
    path('', views.index , name = 'index'),
    path('channels', views.channels_page, name ='channels'),
    path('signup', views.signup, name = 'signup'),
    path('public_channel_form', views.public_channel_form, name='public_channel_form'),
    path('channel_posts/<str:pub_channel_name>', views.channel_posts, name='channel_posts'),
    path('channel_posts/<str:pub_channel_name>/pub_add_post', views.pub_add_post, name ='pub_add_post'),




]
