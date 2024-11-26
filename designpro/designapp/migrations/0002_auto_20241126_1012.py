# Generated by Django 3.2.25 on 2024-11-26 03:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('designapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='application',
            name='status',
            field=models.CharField(choices=[('n', 'New'), ('a', 'Accepted'), ('d', 'Done')], default='n', help_text='The status of the application', max_length=1),
        ),
        migrations.DeleteModel(
            name='Status',
        ),
    ]
