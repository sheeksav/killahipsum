from django.shortcuts import render
from django.views.generic import TemplateView

from .models import Paragraph

# Create your views here.


class IpsumHomeView(TemplateView):
    template_name = 'ipsum/base.html'

    def get_context_data(self, **kwargs):

        paragraphs = Paragraph.objects.all()

        context = {
            'paragraphs': paragraphs,
        }

        return context