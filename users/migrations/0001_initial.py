# Generated by Django 3.2 on 2021-04-22 18:32

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('username', models.CharField(max_length=200, null=True)),
                ('profile_pic', models.ImageField(blank=True, default='default.png', null=True, upload_to='')),
                ('bio', models.TextField()),
                ('vote_ratio', models.IntegerField(blank=True, default=0, null=True)),
                ('followers_count', models.IntegerField(blank=True, default=0, null=True)),
                ('followers', models.ManyToManyField(blank=True, related_name='following', to=settings.AUTH_USER_MODEL)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
