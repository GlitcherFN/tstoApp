from django.conf.urls import url
from django.contrib import admin
from core.views import *

urlpatterns = [
  url('^$', index),
  url('^items/$', item),
  url('^add/$', add_item),
  url('^add/donuts/$', add_donuts),
  url('^add/cash/$', add_cash),
  url('^add/xp/$', set_xp),
  url('^login/$', login),
  url('^signIn/$', auth),
]
