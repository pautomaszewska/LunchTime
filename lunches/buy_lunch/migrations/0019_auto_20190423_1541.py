# Generated by Django 2.1.7 on 2019-04-23 15:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('buy_lunch', '0018_auto_20190422_1903'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='lunchreview',
            name='lunch',
        ),
        migrations.RemoveField(
            model_name='lunchreview',
            name='user',
        ),
        migrations.DeleteModel(
            name='LunchReview',
        ),
    ]