from django.urls import path
from . import views

urlpatterns = [
    path('profile/<str:username>/', views.user_profile),
    path('likemovies/<int:user_id>/', views.user_like_movies),
    path('follow/', views.follow),
    path('uploadimg/', views.upload_img),
    # path('getimg/<int:user_id>/', views.get_img),
]