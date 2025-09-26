from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from .models import Client


def fit_view(request):
    clients = Client.objects.filter(is_public=True).select_related('membership').prefetch_related('workouts')

    return render(request, 'fitness/fit.html', {
        'clients': clients,
        'fio': 'Лыскова Татьяна Михайловна',
        'group': '241-671'
    })