from django.shortcuts import render
from django.views import generic
from .models import KartaQSL
from .forms import KartaQSLForm
from django.urls import reverse_lazy

# Create your views here.

#glowna strona
class QSLListView(generic.ListView):
    model = KartaQSL

class QSLCreateView(generic.CreateView):
    model = KartaQSL
    form_class = KartaQSLForm
    success_url = reverse_lazy('karta:qsl_list')

class QSLUpdateView(generic.UpdateView):
    model = KartaQSL
    form_class = KartaQSLForm
    success_url = reverse_lazy('karta:qsl_list')

class QSLView(generic.DetailView):
    model = KartaQSL
