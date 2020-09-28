from django.urls import path
from . import views

app_name = 'karta'

urlpatterns = [
        path('', view=views.QSLListView.as_view(), name='qsl_list'),
        path('dodaj', view=views.QSLCreateView.as_view(), name='qsl_add'),
        path('edit/<int:pk>', view=views.QSLUpdateView.as_view(), name='qsl_edit'),
        path('<int:pk>', view=views.QSLView.as_view(), name='qsl_detail'),
        ]
