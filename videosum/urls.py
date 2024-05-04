from django.urls import path

from . import views

app_name = 'videosum'
urlpatterns = [
    # path('', views.index, name='index'),
    path('upload_video/', views.upload_video, name='upload_video'),
    path('data_analysis/', views.data_analysis, name='data_analysis')
    # path('upload_video_success', views.upload_video_success, name='upload_video_success'),
]
