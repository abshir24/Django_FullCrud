from django.db import models

from ..first_app.models import User

# Create your models here.

class PostManager(models.Manager):
    def validate_post(self,request_object,user_id):
        status = False
        
        if len(request_object['post']) > 180:
            status = False
        else:
            user = User.objects.get(id = user_id)

            new_post = self.create(post = request_object['post'], user = user)

            status = True
        
        return status

    def validate_like(self, user_id, post_id):
        user = User.objects.get(id = user_id)

        post = Post.objects.get(id = post_id)

        if not user in post.likes.all():
            post.likes.add(user)

        return 

class Post(models.Model): 
    post = models.CharField(max_length = 180)
    user = models.ForeignKey(User, related_name = "created_by", on_delete = models.DO_NOTHING) 
    likes = models.ManyToManyField(User, related_name = "likes")
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)

    objects = PostManager()