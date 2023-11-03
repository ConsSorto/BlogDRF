from django.db import models
from user.models import User
from categories.models import Category
from django.db.models import DO_NOTHING


# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    slug = models.SlugField(max_length=255, unique=True)
    miniature = models.ImageField(upload_to='post/img/')
    created_at = models.DateTimeField(auto_now_add=True)
    published = models.BooleanField(default=False)
    user = models.ForeignKey(User, null=False, on_delete=DO_NOTHING)
    category = models.ForeignKey(Category, null=False, on_delete=DO_NOTHING)

    def __str__(self):
        return self.title