# Generated by Django 3.2 on 2022-06-09 03:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_blogpost_date'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='blogpost',
            options={'ordering': ['blog_id']},
        ),
    ]
