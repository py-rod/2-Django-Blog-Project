# Generated by Django 4.2.5 on 2023-10-04 19:39

from django.db import migrations, models
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0002_alter_article_options_alter_article_table'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='content',
            field=tinymce.models.HTMLField(blank=True, default='', verbose_name='Content article'),
        ),
        migrations.AlterField(
            model_name='article',
            name='created',
            field=models.DateTimeField(auto_created=True, verbose_name='Created'),
        ),
    ]
