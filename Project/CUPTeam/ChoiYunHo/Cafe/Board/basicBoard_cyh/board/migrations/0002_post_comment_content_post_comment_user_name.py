# Generated by Django 4.1 on 2023-01-02 11:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('board', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='comment_content',
            field=models.TextField(default=None),
        ),
        migrations.AddField(
            model_name='post',
            name='comment_user_name',
            field=models.CharField(default=None, max_length=10),
        ),
    ]
