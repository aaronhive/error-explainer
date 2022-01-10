# Generated by Django 4.0.1 on 2022-01-10 15:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('results', '0002_rename_name_errortemplate_template'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='errortype',
            name='id',
        ),
        migrations.AlterField(
            model_name='errortype',
            name='name',
            field=models.CharField(help_text='Must be a python error class, e.g. TypeError', max_length=30, primary_key=True, serialize=False),
        ),
    ]
