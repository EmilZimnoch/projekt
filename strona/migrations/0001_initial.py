# Generated by Django 3.2.8 on 2021-10-20 10:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Room',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(choices=[('kuchnia', 'kitchen'), ('salon', 'living room'), ('pokój', 'room'), ('garaż', 'garage'), ('przedpokój', 'hall'), ('jadalnia', 'dining room'), ('garderoba', 'walk-in wardrobe'), ('spiżarnia', 'pantry'), ('główna sypialnia', 'master bedroom'), ('klatka schodowa', 'staircase'), ('piwnica', 'basement'), ('łazienka', 'bathroom')], default='', max_length=25)),
            ],
        ),
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=125)),
                ('square_meters', models.CharField(choices=[('50m2', '50'), ('100m2', '100'), ('150m2', '150'), ('200m2', '200'), ('250m2', '250'), ('300m2', '300'), ('>300m2', '>300')], default='', max_length=6)),
            ],
        ),
        migrations.CreateModel(
            name='TypeOfSpot',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('wall_type', models.CharField(choices=[('GK', 'plasterboard'), ('BT', 'concrete'), ('PK', 'airbrick'), ('CG', 'brick'), ('WD', 'wood')], default='PK', max_length=2)),
                ('description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Spot',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('furrowing', models.CharField(choices=[('GK', 'plasterboard'), ('BT', 'concrete'), ('PK', 'airbrick'), ('CG', 'brick'), ('WD', 'wood')], max_length=2)),
                ('room', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='strona.room')),
                ('type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='strona.typeofspot')),
            ],
        ),
        migrations.CreateModel(
            name='Smart',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256)),
                ('description', models.TextField()),
                ('smart', models.ManyToManyField(to='strona.Service')),
            ],
        ),
        migrations.AddField(
            model_name='room',
            name='service',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='strona.service'),
        ),
    ]
