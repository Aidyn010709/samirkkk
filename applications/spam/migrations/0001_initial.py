# Generated by Django 4.2.5 on 2023-10-18 07:58

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(help_text='Введите почту пользователя', max_length=254, unique=True, verbose_name='Почта')),
            ],
        ),
    ]