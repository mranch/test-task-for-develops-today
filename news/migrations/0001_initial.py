# Generated by Django 3.0.8 on 2020-08-02 11:29

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('author_name', models.CharField(max_length=50)),
                ('content', models.TextField()),
                ('creation_date', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('link', models.CharField(max_length=256)),
                ('creation_date', models.DateTimeField()),
                ('amount_of_upvotes', models.IntegerField()),
                ('author_name', models.CharField(max_length=50)),
            ],
        ),
    ]
