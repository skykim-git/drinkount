from django.http import HttpResponse
from django.template import loader
from .models import Drinker

def drinkers(request):
    mydrinkers = Drinker.objects.all().values()
    template = loader.get_template('all_drinkers.html')
    context = {
        'mydrinkers': mydrinkers,
    }
    return HttpResponse(template.render(context, request))

def details(request, id):
    mydrinker = Drinker.objects.get(id=id)
    template = loader.get_template('details.html')
    context = {
        'mydrinker': mydrinker,
    }
    return HttpResponse(template.render(context, request))

def main(request):
    template = loader.get_template('main.html')
    return HttpResponse(template.render())