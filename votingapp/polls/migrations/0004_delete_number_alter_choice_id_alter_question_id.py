# Generated by Django 4.1 on 2022-08-10 13:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0003_merge_0002_auto_20220809_2056_0002_number'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Number',
        ),
        migrations.AlterField(
            model_name='choice',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='question',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
