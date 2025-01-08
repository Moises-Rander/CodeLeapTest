# Generated by Django 5.1.4 on 2025-01-08 02:15

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_datetime', models.DateTimeField(auto_now_add=True)),
                ('title', models.CharField(max_length=200)),
                ('content', models.TextField()),
                ('username', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_posts', to='users.user')),
            ],
        ),
    ]
