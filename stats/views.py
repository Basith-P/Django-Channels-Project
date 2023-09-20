from django.shortcuts import render

from .models import Statistic


def main(request):
    qs = Statistic.objects.all()
    return render(request, 'stats/main.html', {'qs': qs})


def dashboard(request, slug):
    return render(request, 'stats/dashboard.html', {'slug': slug})
