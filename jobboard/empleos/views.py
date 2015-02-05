# coding=utf8
# -*- coding: utf8 -*-

from django.views import generic
from django.db.models import Q
from empleos.models import Empleo
import forms
from django.core.urlresolvers import reverse


class EmpleoListView(generic.ListView):
    model = Empleo
    context_object_name = 'empleos_list'
    template_name = 'empleos/index.html'
    paginate_by = 20

    def get_queryset(self):

        results = Empleo.objects.all()

        q = self.request.GET.get('q', None)
        if q:
            results = results.filter(
                Q(titulo__icontains=q) |
                Q(ciudad__nombre__icontains=q) |
                Q(categoria__nombre__icontains=q) |
                Q(descripcion__icontains=q) |
                Q(nombre_empresa__icontains=q) |
                Q(email_empresa__icontains=q))

        return results.order_by('-fecha_creado')

    def get_context_data(self, **kwargs):
        context_data = super(EmpleoListView, self).get_context_data(**kwargs)
        context_data['q'] = self.request.GET.get('q', '')
        return context_data


class EmpleoCreateView(generic.CreateView):
    model = Empleo
    template_name = 'empleos/new.html'
    form_class = forms.EmpleoForm

    def get_success_url(self):
        return reverse('empleos:index')


class EmpleoDetailView(generic.DetailView):
    model = Empleo
    template_name = 'empleos/detail.html'
    context_object_name = 'empleo'