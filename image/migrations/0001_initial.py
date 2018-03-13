# Generated by Django 2.0.3 on 2018-03-13 10:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=130)),
                ('picture', models.ImageField(upload_to='pictures')),
            ],
            options={
                'db_table': 'profile',
            },
        ),
    ]