# Generated by Django 4.2.9 on 2024-02-13 10:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_remove_user_username_user_avatar_user_phone_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='chat_id',
            field=models.TextField(blank=True, null=True, verbose_name='id чата в телеге'),
        ),
    ]