# Generated by Django 4.2.5 on 2023-10-01 19:43

import categories.models
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Categories',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='', max_length=200, unique=True)),
                ('slug', models.SlugField(default='', unique=True)),
                ('image', models.ImageField(default='./default/placeholder.webp', max_length=255, upload_to=categories.models.Categories.image_upload_to)),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Created')),
                ('modified', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Modified')),
                ('author', models.ForeignKey(default='', on_delete=django.db.models.deletion.SET_DEFAULT, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'Categories',
                'db_table': 'Categories',
                'ordering': ('-id',),
            },
        ),
    ]
