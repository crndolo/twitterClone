# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Reply',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('replied_message', models.CharField(max_length=160)),
                ('reply_date', models.DateTimeField(verbose_name=b'default date')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Retweet',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('date_retweeted', models.DateTimeField(verbose_name=b'default date')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Tweet',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('message', models.CharField(max_length=160)),
                ('date_created', models.DateTimeField(verbose_name=b'date created')),
                ('slug', models.SlugField()),
                ('author', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='retweet',
            name='retweeted_message',
            field=models.ForeignKey(to='tweet.Tweet'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='reply',
            name='message',
            field=models.ForeignKey(to='tweet.Tweet'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='reply',
            name='replier',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL),
            preserve_default=True,
        ),
    ]
