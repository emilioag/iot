from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView
from environment.models import Temperature
from itertools import groupby
import numpy as np

class TemperatureView(TemplateView):

    template_name = "temperature.html"

    def get_context_data(self, *args, **kwargs):
        x, y = [], []
        _by = {
            'day': "%D",
            'hour': "%D %H",
            'minute': "%D %H:%M",
            'second': "%D %H:%M:%S"
        }
        by = self.request.GET.get('by', 'hour')
        for key, group in groupby(Temperature.objects.all(), lambda x: x.created_at.strftime(_by[by])):
            x.append(str(key))
            y.append(np.average([i.measure for i in group]))
        return {'x': x, 'y': y}
