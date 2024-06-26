# Generated by Django 5.0.3 on 2024-04-21 14:21

import users.helpers
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_remove_products_users'),
    ]

    operations = [
        migrations.CreateModel(
            name='Testimonial',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField()),
                ('image', models.ImageField(upload_to=users.helpers.SaveMediaFile.testimonial)),
                ('client_name', models.CharField(max_length=100)),
                ('profession', models.CharField(max_length=100)),
                ('star_rating', models.PositiveIntegerField(default=5)),
            ],
        ),
    ]
