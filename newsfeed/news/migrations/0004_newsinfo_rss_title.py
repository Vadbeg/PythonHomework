# Generated by Django 2.2.5 on 2019-11-16 07:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0003_auto_20191115_1911'),
    ]

    operations = [
        migrations.AddField(
            model_name='newsinfo',
            name='rss_title',
            field=models.CharField(default='vadbeg_news', max_length=255),
        ),
    ]
