from django.contrib import admin
from django.urls import path, include

from ormdemo.views import AddressAPI, Index

urlpatterns = [
    path('address/<int:address_id>', AddressAPI.as_view(), name="address"),
    path('', Index.as_view(), name="index"),
]
