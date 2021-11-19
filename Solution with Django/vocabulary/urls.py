from django.urls import path
from . import views

urlpatterns = [
    path('', views.HonePageView.as_view(), name='index'),
    path('add-word', views.AddWordView.as_view(), name='add_word'),
    path('delete-word', views.DeleteWordView.as_view(), name='delete_word'),
]
