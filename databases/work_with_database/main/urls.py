"""
main URL Configuration
"""

from django.contrib import admin
from django.urls import path, include

import phones.views

urlpatterns = [
    path('admin/', admin.site.urls),

    # каталог телефонов
    path('catalog/', phones.views.show_catalog),
    path('catalog/<slug:slug>/', phones.views.show_product),
]
