#from django.shortcuts import render
from django.http import HttpResponse
from django.template import Template, Context, loader
from familiares.models import Familiar

# Create your views here.
def listar_familiares(request):
    queryset = Familiar.objects.all()
    dictionary = {"familiares": queryset}
    template = loader.get_template("familiares_list.html")
    html_document = template.render(dictionary)

    return HttpResponse(html_document)