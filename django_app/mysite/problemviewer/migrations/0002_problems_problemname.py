# Generated by Django 4.1.6 on 2023-04-22 06:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('problemviewer', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='problems',
            name='ProblemName',
            field=models.CharField(default='NOTEXISTS', max_length=200),
            preserve_default=False,
        ),
    ]
