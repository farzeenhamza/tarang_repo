from django.contrib.auth.decorators import login_required
from django.urls import path
from . import views
from accounts.views import HomePageView, CreateProfileView, UsersView, UserDataTableView

urlpatterns = [

    path('home-page/', HomePageView.as_view(), name="home_page"),
    path('create/', CreateProfileView.as_view(), name="create"),
    path('all-users/', UsersView.as_view(), name="users_view"),
    path('users-table/', UserDataTableView.as_view(), name="user_table_view")

]
