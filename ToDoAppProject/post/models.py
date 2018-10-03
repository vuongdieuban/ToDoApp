from django.db import models
from django.urls import reverse
from django.db.models.signals import pre_save, post_save
from ToDoAppProject.utils import unique_slug_generator



class Post(models.Model):
    title       = models.CharField(max_length=120)
    created     = models.DateTimeField(auto_now_add=True)
    description = models.TextField(null=False)
    slug = models.SlugField(max_length=50, unique=True)

    def __str__(self):
        return f'{self.title}'

    def get_absolute_detail_url(self):
        return reverse("post:post-detail", kwargs={"slug": self.slug})


# pre save slug receiver
def slug_save(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = unique_slug_generator(instance, instance.title, instance.slug)


pre_save.connect(slug_save, sender=Post)

