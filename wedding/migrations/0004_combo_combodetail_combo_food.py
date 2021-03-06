# Generated by Django 4.0.3 on 2022-04-05 08:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('wedding', '0003_categoryfood_food'),
    ]

    operations = [
        migrations.CreateModel(
            name='Combo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('active', models.BooleanField(default=True)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('updated_date', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=255, unique=True)),
                ('price', models.FloatField()),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='ComboDetail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField()),
                ('combo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='wedding.combo')),
                ('food', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='wedding.food')),
            ],
        ),
        migrations.AddField(
            model_name='combo',
            name='food',
            field=models.ManyToManyField(related_name='combos', through='wedding.ComboDetail', to='wedding.food'),
        ),
    ]
