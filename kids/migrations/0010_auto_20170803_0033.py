# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-08-02 19:03
from __future__ import unicode_literals

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('kids', '0009_auto_20170725_0438'),
    ]

    operations = [
        migrations.CreateModel(
            name='CommentLikeModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('updated_on', models.DateTimeField(auto_now=True)),
                ('has_liked', models.BooleanField(default=False)),
                ('comment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='kids.CommentModel')),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='kids.PostModel')),
            ],
        ),
        migrations.AlterField(
            model_name='user',
            name='name',
            field=models.CharField(max_length=40, validators=[django.core.validators.RegexValidator('[a-zA-Z]{3,40}$')]),
        ),
        migrations.AlterField(
            model_name='user',
            name='password',
            field=models.CharField(max_length=40, validators=[django.core.validators.RegexValidator('.{4,40}')]),
        ),
        migrations.AlterField(
            model_name='user',
            name='username',
            field=models.CharField(max_length=40, validators=[django.core.validators.RegexValidator('^[a-zA-Z0-9_-]{3,40}$')]),
        ),
        migrations.AddField(
            model_name='commentlikemodel',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='kids.User'),
        ),
    ]
