# Generated by Django 4.2.3 on 2023-07-05 15:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('video', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Video2',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('req_text', models.TextField()),
                ('time_video', models.IntegerField()),
                ('fps', models.IntegerField()),
                ('red', models.IntegerField()),
                ('green', models.IntegerField()),
                ('blue', models.IntegerField()),
            ],
        ),
    ]