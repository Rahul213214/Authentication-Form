# Generated by Django 4.0.2 on 2022-04-11 17:15

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Plot',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('DateTime', models.DateTimeField(auto_now_add=True)),
                ('Location', models.CharField(max_length=50)),
                ('Farm', models.CharField(max_length=50)),
                ('Plot', models.CharField(max_length=50)),
                ('Plants', models.CharField(max_length=50)),
            ],
        ),
    ]
