from django.urls import path, include, re_path
# from .views import GetUserProfileView, UpdateUserProfileView
from .views import index, data
urlpatterns = [
    #gets all user profiles and create a new profile
#     path("all-profiles",UserProfileListCreateView.as_view(),name="all-profiles"),
#    # retrieves profile details of the currently logged in user
    path("",index),
    path("articles/",data, name='articles'),
    # path("article/",hello,name="article"),
]
