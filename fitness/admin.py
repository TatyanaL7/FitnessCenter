
from django.contrib import admin
from .models import Membership, Trainer, Workout, Client


# Настройка для модели Client
@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ['full_name', 'birth_date', 'membership', 'phone', 'display_workouts']
    list_filter = ['membership', 'birth_date']
    search_fields = ['full_name', 'phone', 'workouts__title']
    filter_horizontal = ['workouts']

    def display_workouts(self, obj):
        return ", ".join([workout.title for workout in obj.workouts.all()])

    display_workouts.short_description = 'Занятия'


# Настройка для модели Trainer
@admin.register(Trainer)
class TrainerAdmin(admin.ModelAdmin):
    list_display = ['full_name', 'specialization', 'work_schedule']
    list_filter = ['specialization']
    search_fields = ['full_name']


# Настройка для модели Workout
@admin.register(Workout)
class WorkoutAdmin(admin.ModelAdmin):
    list_display = ['title', 'duration', 'trainer', 'time']
    list_filter = ['trainer', 'time']
    search_fields = ['title', 'trainer__full_name']
    date_hierarchy = 'time'


# Настройка для модели Membership
@admin.register(Membership)
class MembershipAdmin(admin.ModelAdmin):
    list_display = ['type', 'price', 'duration_days']
    list_filter = ['type']
    search_fields = ['type']