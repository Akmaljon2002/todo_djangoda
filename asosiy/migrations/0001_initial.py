# Generated by Django 4.1.5 on 2023-02-11 05:19

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Kundalik',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('muddat', models.CharField(max_length=20)),
                ('batafsil', models.CharField(max_length=50)),
                ('status', models.CharField(choices=[('Boshlanadi', 'Boshlanadi'), ('Boshlandi', 'Boshlandi'), ('Bajarildi', 'Bajarildi')], max_length=50)),
            ],
        ),
    ]
