# Generated by Django 4.2.2 on 2023-07-03 04:38

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='NewsCategoryModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='Unknown', max_length=100)),
            ],
            options={
                'db_table': 'category',
            },
        ),
        migrations.CreateModel(
            name='NewsModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='Title', max_length=200)),
                ('content', models.TextField(default='Not Given')),
                ('timestamp', models.DateTimeField(default=datetime.datetime.now)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='news.newscategorymodel')),
            ],
            options={
                'db_table': 'news',
            },
        ),
        migrations.CreateModel(
            name='CommentModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('author', models.CharField(max_length=50)),
                ('content', models.TextField(max_length=10000)),
                ('timestamp', models.DateTimeField(default=datetime.datetime.now)),
                ('news', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='news.newsmodel')),
            ],
            options={
                'db_table': 'comment',
            },
        ),
    ]
