from django.urls import path
from .views import index,export_pdf

urlpatterns=[
    path('export_pdf',export_pdf,name='export_pdf'),
    path('',index),
]