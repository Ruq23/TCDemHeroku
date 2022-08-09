# Generated by Django 4.0.5 on 2022-07-27 06:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('country', models.CharField(max_length=100)),
                ('duration', models.DurationField()),
                ('industry', models.CharField(choices=[('Banking', 'Banking'), ('Finance', 'Finance'), ('Tech', 'Tech'), ('Entertainment', 'Entertainment')], max_length=13)),
                ('Privacy', models.BooleanField(default=False)),
                ('Advertisment', models.BooleanField(default=False)),
            ],
        ),
    ]
