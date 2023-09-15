from django.contrib import admin
from django.urls import path
from random_reads.rr_api import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.randomize_book)
]
