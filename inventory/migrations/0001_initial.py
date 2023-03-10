# Generated by Django 4.1.7 on 2023-03-03 13:55

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('user_id', models.AutoField(primary_key=True, serialize=False)),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('password', models.CharField(max_length=128)),
                ('phone_number', models.CharField(max_length=15)),
                ('address', models.TextField()),
                ('role', models.CharField(choices=[('admin', 'Admin'), ('staff', 'Staff')], default='user', max_length=10)),
            ],
        ),
    ]
