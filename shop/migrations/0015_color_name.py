# Generated by Django 3.2 on 2022-12-31 21:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0014_alter_color_color'),
    ]

    operations = [
        migrations.AddField(
            model_name='color',
            name='name',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
