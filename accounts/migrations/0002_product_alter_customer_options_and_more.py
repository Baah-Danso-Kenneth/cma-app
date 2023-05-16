# Generated by Django 4.2.1 on 2023-05-16 10:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("accounts", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Product",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=30)),
                ("price", models.FloatField()),
                ("category", models.CharField(max_length=5)),
                ("description", models.TextField()),
                ("date_created", models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.AlterModelOptions(
            name="customer",
            options={"ordering": ["-date_created"]},
        ),
        migrations.AddIndex(
            model_name="customer",
            index=models.Index(
                fields=["-date_created"], name="accounts_cu_date_cr_a1ed3a_idx"
            ),
        ),
        migrations.AddField(
            model_name="product",
            name="customer",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="customer",
                to="accounts.customer",
            ),
        ),
    ]
