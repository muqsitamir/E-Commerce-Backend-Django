# Generated by Django 3.2 on 2022-12-17 20:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0010_category_endorsement_pic'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='category',
            name='endorsement_pic',
        ),
        migrations.AddField(
            model_name='featuredimage',
            name='category_endorsement_pic',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
    ]
