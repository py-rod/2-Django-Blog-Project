from django.db import models
import os
import string
import random
from django.utils import timezone
from django.contrib.auth import get_user_model
from django.template.defaultfilters import slugify
from django.db.models import Q
from colorfield.fields import ColorField
from django.urls import reverse
# Create your models here.


class Categories(models.Model):
    def image_upload_to(self, instance):
        if instance:
            return os.path.join("Categories", slugify(self.title), instance)
        return None

    def get_admin_users():
        User = get_user_model()
        return User.objects.filter(Q(is_superuser=True) | Q(is_staff=True)).first()

    title = models.CharField(max_length=200, default="", unique=True)
    bg_color = ColorField("Choise color", default="#F3F4F6",
                          format="hexa", blank=True)
    slug = models.SlugField(default="", unique=True, blank=False)
    author = models.ForeignKey(
        get_user_model(), default=get_admin_users, on_delete=models.SET_DEFAULT)
    image = models.ImageField(
        default="./default/placeholder.webp", upload_to=image_upload_to, max_length=255)

    created = models.DateTimeField("Created", auto_now_add=True)
    modified = models.DateTimeField("Modified", default=timezone.now)

    # SLUG AUTOMATICO
    def save(self, *args, **kwargs):
        while True:
            slug_random = "".join(random.sample(
                f"{string.ascii_lowercase}{string.ascii_uppercase}", 50))
            if Categories.objects.filter(slug=slug_random).exists() == False and self.slug == "":
                print("no existe este slug")
                self.slug = slug_random
                super(Categories, self).save(*args, **kwargs)
                break
            elif Categories.objects.filter(slug=self.slug).exists() == True and self.slug != "":
                print("Guardando el mismo slug")
                super(Categories, self).save(*args, **kwargs)
                break

    def __str__(self):
        return self.title

    def slug_category(self):
        return reverse("articles", args=[self.slug])

    class Meta:
        verbose_name_plural = "Categories"
        db_table = "Categories"
        ordering = ("-id", )
