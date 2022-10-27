# Generated by Django 4.1 on 2022-10-27 12:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('musicapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lyrics',
            name='content',
            field=models.TextField(max_length=600),
        ),
        migrations.AlterField(
            model_name='lyrics',
            name='song_id',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='musicapp.song'),
        ),
    ]