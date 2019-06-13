# Generated by Django 2.1.7 on 2019-05-10 18:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [("scope", "0007_delete_taskresult")]

    operations = [
        migrations.AlterField(
            model_name="dip",
            name="objectszip",
            field=models.FileField(
                help_text="Related DIP (only tar and zip files allowed).",
                upload_to="",
                verbose_name="DIP file",
            ),
        )
    ]