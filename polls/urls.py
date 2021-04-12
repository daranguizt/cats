from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('details/<int:post_id>', views.details, name='details')
]