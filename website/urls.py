from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("login/", views.login_user, name="login"),
    path("logout/", views.logout_user, name="logout"),
    path("register/", views.register_user, name="register"),
    path("add-record/", views.add_record, name="add-record"),
    path("view-record/<str:pk>/", views.view_record, name="view-record"),
    path("delete-record/<str:pk>/", views.delete_record, name="delete-record"),
    path("edit-record/<str:pk>/", views.edit_record, name="edit-record"),

]
