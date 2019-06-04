from django.db import models
from datetime import datetime

# Create your models here.
class BlogPost(models.Model):

    post_title = models.CharField(max_length=200)
    post_content = models.TextField()
    post_published = models.DateTimeField('date published', default=datetime.now())
    post_slug = models.CharField(max_length=200, default=1)
    # def post_slug(self):
    #     return slugify(self.post_title)

    def __str__(self):
        return self.post_title