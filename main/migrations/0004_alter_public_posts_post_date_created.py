# Generated by Django 4.0.4 on 2022-07-18 20:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_alter_public_channel_channel_members'),
    ]

    operations = [
        migrations.AlterField(
            model_name='public_posts',
            name='post_date_created',
            field=models.DateTimeField(null=True),
        ),
    ]
