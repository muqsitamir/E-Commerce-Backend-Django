# Generated by Django 3.2 on 2022-12-17 20:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0009_featuredimage_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='endorsement_pic',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]
