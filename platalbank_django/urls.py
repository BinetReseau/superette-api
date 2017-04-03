"""platalbank_django URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin
from rest_framework import routers

from platalbank_core.views.event import EventViewSet
from platalbank_core.views.transaction import TransactionViewSet
from platalbank_core.views.account import AccountViewSet
from platalbank_core.views.user import UserViewSet
from platalbank_core.views.frankiz_user import FrankizUserViewSet
#from platalbank_auth.views import UserViewSet

from platalbank_core.views.ldap_user import ldap_search

router = routers.DefaultRouter()

router.register("event", EventViewSet)
router.register("transaction", TransactionViewSet)
router.register("account", AccountViewSet)
router.register("user", UserViewSet)
router.register("frankiz_user", FrankizUserViewSet)

urlpatterns = [
    url(r'^api/', include(router.urls)),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^api-token-auth/', 'rest_framework_jwt.views.obtain_jwt_token'),
    url(r'^ldap_search$', ldap_search, name="ldap_search")
]
