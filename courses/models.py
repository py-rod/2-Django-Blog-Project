from django.db import models
import os
import random
import string
from django.template.defaultfilters import slugify
from categories.models import Categories
from users.models import CustomUser
from django.contrib.auth import get_user_model
from django.db.models import Q
from django.utils import timezone
from tinymce.models import HTMLField
# Create your models here.


class Article(models.Model):
    def image_upload_to(self, instance):
        if instance:
            return os.path.join("Articles", slugify(self.title), instance)
        return None

    def get_admin_users():
        User = get_user_model()
        return User.objects.filter(Q(is_superuser=True) | Q(is_staff=True)).first()

    title = models.CharField(max_length=200, unique=False, blank=False)
    description = models.CharField(max_length=300, blank=True, unique=False)
    article_slug = models.SlugField(default="", unique=True, blank=False)
    series = models.ForeignKey(
        Categories, default="", blank=False, on_delete=models.CASCADE)
    author = models.ForeignKey(
        get_user_model(), default=get_admin_users, on_delete=models.SET_DEFAULT)
    image = models.ImageField(
        default="./default/placeholder.webp", upload_to=image_upload_to, max_length=255)

    content = HTMLField("Content article", default="",
                        blank=True, unique=False)

    created = models.DateTimeField(
        "Created", auto_created=True, auto_now_add=True)
    modified = models.DateTimeField("Modified", default=timezone.now)

    # SLUG AUTOMATICO
    def save(self, *args, **kwargs):
        while True:
            slug_random = "".join(random.sample(
                f"{string.ascii_lowercase}{string.ascii_uppercase}", 50))
            if Article.objects.filter(article_slug=slug_random).exists() == False and self.article_slug == "":
                print("no existe este slug")
                self.article_slug = slug_random
                super(Article, self).save(*args, **kwargs)
                break
            elif Article.objects.filter(article_slug=self.article_slug).exists() == True and self.article_slug != "":
                print("Guardando el mismo slug")
                super(Article, self).save(*args, **kwargs)
                break

    def __str__(self):
        return self.title

    def slug(self):
        return f"{self.series.slug}/{self.article_slug}"

    class Meta:
        verbose_name_plural = "Articles"
        db_table = "Articles"
        ordering = ("-id",)
