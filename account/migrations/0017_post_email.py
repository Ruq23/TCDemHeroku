# Generated by Django 4.0.5 on 2022-08-14 12:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0016_remove_post_email'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='Email',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
