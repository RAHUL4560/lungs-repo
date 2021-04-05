from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('base', views.base, name='base'),
    path('signup', views.signup, name='signup'),
    path('contacts', views.contacts, name='contacts'),
    path('crackles_wheezes', views.crackles_wheezes, name='crackles_wheezes'),
    path('crackles', views.crackles, name='crackles'),
    path('disease', views.disease, name='disease'),
    path('references', views.references, name='references'),
    path('sounds', views.sounds, name='sounds'),
    path('squawks', views.squawks, name='squawks'),
    path('stirdor', views.stirdor, name='stirdor'),
    path('wheezes', views.wheezes, name='wheezes'),
    path('review', views.review, name='review'),
    path('crackles_sound', views.crackles_sound, name='crackles_sound'),
    path('crackleswheezes_sound', views.crackleswheezes_sound, name='crackleswheezes_sound'),
    path('wheezes_sound', views.wheezes_sound, name='wheezes_sound'),
    path('stirdor_sound', views.stirdor_sound, name='stirdor_sound'),
    path('squawks_sound', views.squawks_sound, name='squawks_sound'),


    path('signup', views.handleSignup, name='handleSignup'),
    path('login', views.handleLogin, name='handleLogin'),
    path('logout', views.handleLogout, name='handleLogout'),

    ]