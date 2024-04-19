# Generated by Django 5.0.4 on 2024-04-19 19:22

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Habit",
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
                ("time", models.TimeField(verbose_name="Время привычки")),
                ("place", models.CharField(max_length=50, verbose_name="Место")),
                ("action", models.CharField(max_length=50, verbose_name="Действи")),
                (
                    "reward",
                    models.CharField(
                        blank=True, max_length=50, null=True, verbose_name="Награда"
                    ),
                ),
                (
                    "periodicity",
                    models.PositiveIntegerField(verbose_name="Периодичность"),
                ),
                (
                    "is_public",
                    models.BooleanField(
                        default=False, verbose_name="Является общедоступным"
                    ),
                ),
                ("duration_time", models.TimeField(verbose_name="Продолжительность")),
                (
                    "next_date",
                    models.DateField(
                        blank=True,
                        null=True,
                        verbose_name="Дата следующего действия по привычке",
                    ),
                ),
            ],
            options={
                "verbose_name": "Привычка",
                "verbose_name_plural": "Привычки",
            },
        ),
        migrations.CreateModel(
            name="NiceHabit",
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
                (
                    "place",
                    models.CharField(
                        blank=True, max_length=50, null=True, verbose_name="Место"
                    ),
                ),
                ("action", models.CharField(max_length=50, verbose_name="Действие")),
            ],
            options={
                "verbose_name": "Хорошая привычка",
                "verbose_name_plural": "Хорошие привычки",
            },
        ),
    ]