# Generated by Django 4.1.6 on 2023-04-23 03:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('problemviewer', '0004_alter_testcases_input_alter_testcases_output'),
    ]

    operations = [
        migrations.AlterField(
            model_name='testcases',
            name='Input',
            field=models.TextField(null=True),
        ),
    ]
