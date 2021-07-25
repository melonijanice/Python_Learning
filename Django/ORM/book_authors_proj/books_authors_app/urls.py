from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('',views.index),
    path('authors',views.authors),
    path('create',views.create),
    path('books/<int:id>',views.view_books),
    path('authors/<int:id>',views.view_authors),
    path('add',views.add),

]