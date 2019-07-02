# Generated by Django 2.2.3 on 2019-07-02 21:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Site',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('site_name', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(max_length=200)),
                ('title', models.CharField(max_length=20000)),
                ('pub_date', models.DateTimeField(verbose_name='date published')),
                ('site_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='articles.Site')),
            ],
        ),
    ]
