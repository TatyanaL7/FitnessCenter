from django.db import models
from django.contrib.auth.models import User


class Membership(models.Model):
    MEMBERSHIP_TYPES = [
        ('STANDARD', 'Стандартный'),
        ('PREMIUM', 'Премиум'),
        ('VIP', 'VIP'),
    ]

    type = models.CharField(max_length=20, choices=MEMBERSHIP_TYPES, verbose_name="Тип абонемента")
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Стоимость")
    duration_days = models.IntegerField(verbose_name="Срок действия (дни)")

    def __str__(self):
        return f"{self.get_type_display()} - {self.price} руб."

    class Meta:
        verbose_name = "Абонемент"
        verbose_name_plural = "Абонементы"


class Trainer(models.Model):
    SPECIALIZATIONS = [
        ('YOGA', 'Йога'),
        ('CARDIO', 'Кардио'),
        ('STRENGTH', 'Силовые тренировки'),
        ('CROSSFIT', 'Кроссфит'),
    ]

    full_name = models.CharField(max_length=100, verbose_name="ФИО тренера")
    specialization = models.CharField(max_length=20, choices=SPECIALIZATIONS, verbose_name="Специализация")
    work_schedule = models.TextField(verbose_name="График работы")

    def __str__(self):
        return self.full_name

    class Meta:
        verbose_name = "Тренер"
        verbose_name_plural = "Тренеры"


class Workout(models.Model):
    title = models.CharField(max_length=100, verbose_name="Название занятия")
    duration = models.IntegerField(verbose_name="Длительность (минуты)")
    description = models.TextField(verbose_name="Описание")
    time = models.DateTimeField(verbose_name="Время проведения")
    trainer = models.ForeignKey(Trainer, on_delete=models.CASCADE, verbose_name="Тренер")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Занятие"
        verbose_name_plural = "Занятия"


class Client(models.Model):
    full_name = models.CharField(max_length=100, verbose_name="ФИО клиента")
    birth_date = models.DateField(verbose_name="Дата рождения")
    membership = models.ForeignKey(Membership, on_delete=models.SET_NULL, null=True, verbose_name="Абонемент")
    phone = models.CharField(max_length=20, verbose_name="Телефон")
    # Прямая ManyToMany связь без промежуточной таблицы
    workouts = models.ManyToManyField(Workout, verbose_name="Занятия")

    def __str__(self):
        return self.full_name

    class Meta:
        verbose_name = "Клиент"
        verbose_name_plural = "Клиенты"