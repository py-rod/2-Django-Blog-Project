# Generated by Django 4.2.5 on 2023-10-04 19:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0003_article_content_alter_article_created'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='description',
            field=models.CharField(blank=True, max_length=300),
        ),
    ]