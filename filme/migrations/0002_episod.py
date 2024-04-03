# Generated by Django 4.1.3 on 2024-04-02 02:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('filme', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Episod',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('link', models.URLField()),
                ('film', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='episodios', to='filme.film')),
            ],
        ),
    ]
