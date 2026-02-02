from django.urls import path
from . import views

app_name = "posts" #tells the project the particular app this name urls belongs to.

# urls patterns for post app
urlpatterns = [
    path("", views.posts_lists, name="lists"),
    path("new_post", views.new_post, name="post"),
    path("delete/<int:id>", views.delete_view_post, name="delete"),
    path("update/<int:id>", views.update_view_post, name="update"),
    path("<slug:slug>", views.post_page, name="page"),

]
