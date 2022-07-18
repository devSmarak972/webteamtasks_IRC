
from django.urls import path
# now import the views.py file into this code
from . import views
urlpatterns = [
    path('home', views.home_page),
    path('/',views.home_page),
    path("get/univ", views.getUniversityCard),
    path("add/bookmark", views.addBookmark),
    path("remove/bookmark", views.removeBookmark),
    path("add/application", views.addApplication),
    path("remove/application", views.removeApplication),
    path("signup", views.Signup_view),
    path("login", views.Login_view),
    path("logout", views.Signout, name='logout'),
    path("bookmarks", views.Bookmarks_view),
    path("applications", views.Applications_view),
    path("notifications", views.Notifications_view),
    path("profile", views.ProfileUpdate),
    # path("auth/login",views.Login),
]
