# Generated by Django 4.0.5 on 2022-08-14 11:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0015_post_email_post_phone_post_poli_post_term_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='Email',
        ),
    ]
