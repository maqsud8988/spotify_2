# Generated by Django 5.0.3 on 2024-05-12 12:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0006_rename_testimonial_testimonials'),
    ]

    operations = [
        migrations.AddField(
            model_name='products',
            name='rating',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]
