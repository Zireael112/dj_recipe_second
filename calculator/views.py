from django.http import HttpResponse
from django.shortcuts import render

DATA = {
    'omlet': {
        'яйца, шт': 2,
        'молоко, л': 0.1,
        'соль, ч.л.': 0.5,
    },
    'pasta': {
        'макароны, г': 0.3,
        'сыр, г': 0.05,
    },
    'buter': {
        'хлеб, ломтик': 1,
        'колбаса, ломтик': 1,
        'сыр, ломтик': 1,
        'помидор, ломтик': 1,
    },
}


def omlet(request):
    serv = request.GET.get('servings', 1)
    context = {
        'serv': serv,
        'recipe': {
            'яйца, шт': round(2 * int(serv), 1),
            'молоко, л': round(0.1 * int(serv), 1),
            'соль, ч.л.': round(0.5 * int(serv), 1),
        }
    }

    return render(request, 'calculator/index.html', context)


def pasta(request):
    serv = request.GET.get('servings', 1)
    context = {
        'serv': serv,
        'recipe': {
            'макароны, г': round(0.3 * int(serv), 1),
            'сыр, г': round(0.05 * int(serv), 1),
        }
    }

    return render(request, 'calculator/index.html', context)


def buter(request):
    serv = request.GET.get('servings', 1)
    context = {
        'serv': serv,
        'recipe': {
            'хлеб, ломтик': round(1 * int(serv), 1),
            'колбаса, ломтик': round(1 * int(serv), 1),
            'сыр, ломтик': round(1 * int(serv), 1),
            'помидор, ломтик': round(1 * int(serv), 1),
        },
    }
    return render(request, 'calculator/index.html', context)

