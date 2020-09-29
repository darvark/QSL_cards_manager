from django.shortcuts import render
from django.views import generic
from .models import KartaQSL
from .forms import KartaQSLForm
from django.urls import reverse_lazy
from .forms import UserRegisterForm
from django.shortcuts import redirect
from django.contrib.auth import authenticate, login

# Create your views here.

#glowna strona
class QSLListView(generic.ListView):
    model = KartaQSL

    # def get_queryset(self):
    #     queryset = super(QSLListView, self).get_queryset()
        # return queryset.filter(operator=[self.request.user])

    def get_queryset(self):
        # self.publisher = get_object_or_404(Publisher, name=self.args[0])
        return KartaQSL.objects.filter(operator=self.request.user)


class QSLCreateView(generic.CreateView):
    model = KartaQSL
    form_class = KartaQSLForm
    success_url = reverse_lazy('qsl_list')

    # def get_form_kwargs(self):
    #     kwargs = super(QSLCreateView, self).get_form_kwargs()
    #     kwargs.update({'operator': self.request.user})
    #     return kwargs

    def form_valid(self, form): 
        form.instance.operator = self.request.user
        return super().form_valid(form) 

class QSLUpdateView(generic.UpdateView):
    model = KartaQSL
    form_class = KartaQSLForm
    success_url = reverse_lazy('qsl_list')

class QSLView(generic.DetailView):
    model = KartaQSL

def rejestracja_view(request):
    next = request.GET.get('next')
    form = UserRegisterForm(request.POST or None)
    if form.is_valid():
        user = form.save(commit=False)
        password = form.cleaned_data.get('password')
        user.set_password(password)
        user.save()
        new_user = authenticate(username=user.username, password=password)
        login(request, new_user)
        if next:
            return redirect(next)
        return redirect('/')

    context = {
        'form': form,
    }
    return render(request, "karty/rejestracja.html", context)