# Generated by Django 2.1.7 on 2019-04-01 18:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('buy_lunch', '0007_auto_20190331_1601'),
    ]

    operations = [
        migrations.CreateModel(
            name='LunchReview',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('review', models.TextField()),
                ('lunch', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='buy_lunch.Lunch')),
            ],
        ),
    ]