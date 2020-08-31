from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('explore/', views.SongListView.as_view(), name='song-list'),
    path('song/<int:pk>', views.SongDetailView.as_view(), name='song-detail'),
]