# Generated by Django 5.0 on 2024-01-07 14:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notes', '0003_alter_note_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='note',
            name='tags',
            field=models.CharField(choices=[(1, 'Programming'), (2, 'Daily Life'), (3, 'Science Fiction'), (4, 'Jobs'), (5, 'Home'), (6, 'Friends'), (7, 'Tours'), (8, 'Educational'), (9, 'Hobby'), (10, 'Cricket'), (11, 'Footbal')], max_length=100),
        ),
    ]
