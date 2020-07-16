# Generated by Django 3.0.8 on 2020-07-16 20:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_remove_freelancer_password'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('facebook', models.CharField(blank=True, max_length=300, null=True)),
                ('instagram', models.CharField(blank=True, max_length=300, null=True)),
                ('whatsapp', models.CharField(blank=True, max_length=15, null=True)),
                ('freelancer', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='app.Freelancer')),
            ],
        ),
    ]