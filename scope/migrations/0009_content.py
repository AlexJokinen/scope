# Generated by Django 2.1.7 on 2019-05-31 23:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [("scope", "0008_alter_dip_objectszip")]

    operations = [
        migrations.CreateModel(
            name="Content",
            fields=[
                (
                    "key",
                    models.CharField(max_length=50, primary_key=True, serialize=False),
                ),
                ("content", models.TextField(blank=True, verbose_name="content")),
                (
                    "content_en",
                    models.TextField(blank=True, null=True, verbose_name="content"),
                ),
                (
                    "content_fr",
                    models.TextField(blank=True, null=True, verbose_name="content"),
                ),
            ],
        )
    ]