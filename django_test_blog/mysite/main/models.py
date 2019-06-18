from django.db import models
from datetime import datetime


class BlogPostCategory(models.Model):
    post_category = models.CharField(max_length=200)
    category_summary = models.CharField(max_length=200)
    category_slug = models.CharField(max_length=200)

    class Meta:
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.post_category


class BlogPostSeries(models.Model):
    post_series = models.CharField(max_length=200)
    post_category = models.ForeignKey(BlogPostCategory, default=1, verbose_name="Category", on_delete=models.SET_DEFAULT)
    series_summary = models.CharField(max_length=200)

    class Meta:
        verbose_name_plural = "Series"
    
    def __str__(self):
        return self.post_series


class BlogPost(models.Model):
    post_title = models.CharField(max_length=200)
    post_content = models.TextField()
    post_published = models.DateTimeField('date published', default=datetime.now())
    post_series = models.ForeignKey(BlogPostSeries, default=1, verbose_name="Series", on_delete=models.SET_DEFAULT)
    post_slug = models.CharField(max_length=200, default=1)
    # def post_slug(self):
    #     return slugify(self.post_title)


    def __str__(self):
        return self.post_title