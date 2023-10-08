# Generated by Django 4.2.5 on 2023-10-04 19:32

import courses.models
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('categories', '0011_remove_categories_description'),
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('description', models.TextField(blank=True, max_length=300)),
                ('article_slug', models.SlugField(default='', unique=True)),
                ('image', models.ImageField(default='./default/placeholder.webp', max_length=255, upload_to=courses.models.Article.image_upload_to)),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Created')),
                ('modified', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Modified')),
                ('author', models.ForeignKey(default=courses.models.Article.get_admin_users, on_delete=django.db.models.deletion.SET_DEFAULT, to=settings.AUTH_USER_MODEL)),
                ('series', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='categories.categories')),
            ],
            options={
                'verbose_name_plural': 'Sub_categories',
                'db_table': 'Subcategories',
                'ordering': ('-id',),
            },
        ),
    ]
