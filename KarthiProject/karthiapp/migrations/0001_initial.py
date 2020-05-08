# Generated by Django 3.0.4 on 2020-05-05 03:42

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='KarthiData',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=56)),
                ('playtime', models.IntegerField()),
                ('cycletime', models.IntegerField()),
                ('kumonpages', models.CharField(choices=[('1', '1 page'), ('3', '2 pages'), ('4', '4 pages'), ('5', '5 pages'), ('6', '6 pages'), ('7', '7 pages'), ('8', '8 pages'), ('9', '9 pages'), ('1b', '1 book')], max_length=10)),
                ('schoolhomework', models.CharField(max_length=56)),
                ('comments', models.TextField(max_length=256)),
            ],
        ),
    ]