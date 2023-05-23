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


def recipes_view(request, recipe):
    template_name = 'calculator/index.html'
    amount = int(request.GET.get('servings', 1))
    recipe_dict = {}
    for i, j in DATA[recipe].items():
        j *= amount
        recipe_dict[i] = j
    context = {
      'recipe': recipe_dict,
        }
    return render(request, template_name, context)
