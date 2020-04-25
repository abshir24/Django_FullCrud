from django.conf.urls import url

from . import views

app_name = 'newsfeed'
urlpatterns = [
    url(r'^addpost$', views.addPost, name = 'addPost'),
    url(r'^success$',views.success, name = 'success'),
    url(r'^(?P<id>\d+)/add_like$',views.addLike, name = 'addLike'),
    url(r'^(?P<id>\d+)/delete_post$',views.deletePost, name = 'deletePost'),
    url(r'^(?P<id>\d+)/edit_post$',views.editPost, name = 'editPost'),
    url(r'^update_post/(?P<id>\d+)$',views.updatePost, name = 'updatePost'),
]
    