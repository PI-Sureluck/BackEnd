# Generated by Django 4.2.5 on 2023-10-28 19:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('sites', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='surebets',
            name='event',
        ),
        migrations.RemoveField(
            model_name='surebets',
            name='site',
        ),
        migrations.AlterField(
            model_name='surebets',
            name='oddA',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='oddsA', to='sites.odds'),
        ),
        migrations.AlterField(
            model_name='surebets',
            name='oddB',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='oddsB', to='sites.odds'),
        ),
    ]
