# Generated by Django 2.2.7 on 2019-11-26 10:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0009_auto_20191126_1306'),
    ]

    operations = [
        migrations.AddField(
            model_name='newsinfo',
            name='title_hash',
            field=models.CharField(default=103521887209868644, max_length=255),
        ),
        migrations.AlterField(
            model_name='newsinfo',
            name='rss_hash',
            field=models.CharField(default=-6901618732714633604, max_length=255),
        ),
    ]