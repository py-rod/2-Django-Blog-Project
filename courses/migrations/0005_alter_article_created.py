# Generated by Django 4.2.5 on 2023-10-04 19:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0004_alter_article_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='created',
            field=models.DateTimeField(auto_created=True, auto_now_add=True, verbose_name='Created'),
        ),
    ]
