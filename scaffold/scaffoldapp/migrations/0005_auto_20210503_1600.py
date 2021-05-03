# Generated by Django 3.2 on 2021-05-03 16:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('portofolioapp', '0001_initial'),
        ('scaffoldapp', '0004_auto_20210503_1529'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='card',
            name='categorie',
        ),
        migrations.RemoveField(
            model_name='image',
            name='projet',
        ),
        migrations.DeleteModel(
            name='Partenaire',
        ),
        migrations.DeleteModel(
            name='Testimonial',
        ),
        migrations.AlterField(
            model_name='imagecard',
            name='card',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='image_card', to='portofolioapp.card'),
        ),
        migrations.DeleteModel(
            name='Card',
        ),
        migrations.DeleteModel(
            name='Categorie',
        ),
        migrations.DeleteModel(
            name='Image',
        ),
    ]
