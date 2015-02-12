from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.


class IpsumHomeView(TemplateView):
    template_name = 'ipsum/base.html'