# Generated by Django 4.0.3 on 2022-04-05 12:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('wedding', '0007_alter_dateoforganization_unique_together'),
    ]

    operations = [
        migrations.CreateModel(
            name='TimeFrame',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('active', models.BooleanField(default=True)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('updated_date', models.DateTimeField(auto_now=True)),
                ('hour', models.IntegerField()),
                ('minute', models.IntegerField()),
                ('second', models.IntegerField()),
                ('price', models.FloatField()),
            ],
            options={
                'unique_together': {('hour', 'minute', 'second')},
            },
        ),
        migrations.AddField(
            model_name='dateoforganization',
            name='time_frame',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='dateorganizations', to='wedding.timeframe'),
        ),
    ]
