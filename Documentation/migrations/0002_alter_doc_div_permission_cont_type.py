# Generated by Django 4.2.1 on 2023-05-25 10:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('contenttypes', '0002_remove_content_type_name'),
        ('Documentation', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='doc_div_permission',
            name='cont_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='contenttypes.contenttype'),
        ),
    ]
