from django.shortcuts import get_object_or_404, redirect, render
from faker import Faker

from .models import Statistic

fake = Faker()


def main(request):
    qs = Statistic.objects.all()

    if request.method == 'POST':
        name = request.POST.get('name')
        statistic, _ = Statistic.objects.get_or_create(name=name)
        return redirect("stats:dashboard", statistic.slug)

    return render(request, 'stats/main.html', {'qs': qs})


def dashboard(request, slug):
    obj = get_object_or_404(Statistic, slug=slug)
    context = {
        'name': obj.name,
        'slug': obj.slug,
        'data': obj.data,
        'user': request.user.username if request.user.username else fake.name(),
    }
    return render(request, 'stats/dashboard.html', context)
