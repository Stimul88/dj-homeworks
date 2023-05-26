from django.shortcuts import render, redirect

from phones.models import Phone


def index(request):
    return redirect('catalog')


def show_catalog(request):
    template = 'catalog.html'
    sort = request.GET.get('sort', '')
    all_phones = Phone.objects.all()
    match sort:
        case 'name':
            phone = all_phones.order_by('name')
            context = {'phones': phone}
            return render(request, template, context)
        case 'min_price':
            phone = all_phones.order_by('price')
            context = {'phones': phone}
            return render(request, template, context)
        case 'max_price':
            phone = all_phones.order_by('-price')
            context = {'phones': phone}
            return render(request, template, context)
    context = {'phones': all_phones}
    return render(request, template, context)


def show_product(request, slug):
    template = 'product.html'
    phones = Phone.objects.filter(slug=slug)
    for phone in phones:
        context = {'phone': phone}
        return render(request, template, context)
