# Generated by Django 2.2.7 on 2019-11-18 11:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0006_auto_20191116_1139'),
    ]

    operations = [
        migrations.CreateModel(
            name='LastNewsInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_id', models.IntegerField()),
                ('pubDate', models.DateTimeField(max_length=255)),
                ('title', models.CharField(max_length=255, unique=True)),
                ('rss_title', models.CharField(default='vadbeg_news', max_length=255)),
                ('rss_hash', models.CharField(default=-3274672197587549420, max_length=255)),
                ('link', models.CharField(max_length=255)),
                ('description', models.CharField(max_length=1000)),
                ('imageLink', models.CharField(max_length=255)),
                ('imageDescription', models.CharField(max_length=255)),
            ],
        ),
        migrations.AlterField(
            model_name='newsinfo',
            name='rss_hash',
            field=models.CharField(default=-3274672197587549420, max_length=255),
        ),
    ]