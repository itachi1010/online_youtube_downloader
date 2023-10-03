from django.urls import path
from . import views

urlpatterns = [
    path('download/', views.download_video, name='download_video'),
    path('videos/', views.video_list, name='video_list'),
    path('get-csrf-token/', views.get_csrf_token, name='get_csrf_token'),

]
