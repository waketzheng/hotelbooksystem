# Generated by Django 2.0.5 on 2018-06-02 16:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0005_auto_20180603_0002'),
    ]

    operations = [
        migrations.AddField(
            model_name='hotel',
            name='overview',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]
