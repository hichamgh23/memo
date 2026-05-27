from django.urls import path
from . import views

urlpatterns = [
    path('', views.show_list, name='show_list'),
    path('shows/<int:show_id>/', views.show_detail, name='show_detail'),
    path('shows/<int:show_id>/add-video/', views.add_video, name='add_video'),
    path('artist/<str:artist_name>/videos/', views.videos_by_artist, name='videos_by_artist'),
]
