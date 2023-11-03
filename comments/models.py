from django.db.models import DO_NOTHING, CASCADE
from django.db import models
from user.models import User
from post.models import Post


class Comment(models.Model):
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=DO_NOTHING, null=False)
    post = models.ForeignKey(Post, on_delete=CASCADE, null=False)

