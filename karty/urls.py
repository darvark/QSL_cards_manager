from django.urls import path
from . import views
from django.contrib.auth import views as bv
from django.contrib.auth.decorators import login_required

# app_name = 'karta'

urlpatterns = [
        path('', view=views.QSLListView.as_view(), name='qsl_list'),
        path('dodaj', login_required(views.QSLCreateView.as_view()), name='qsl_add'),
        path('edit/<int:pk>', login_required(views.QSLUpdateView.as_view()), name='qsl_edit'),
        path('<int:pk>', view=views.QSLView.as_view(), name='qsl_detail'),
        path('accounts/login/', bv.LoginView.as_view(), name='login'),
        path('accounts/logout/', bv.LogoutView.as_view(next_page='/'), name='logout'),
        path('accounts/rejestracja/', views.rejestracja_view, name='rejestracja'),
        ]
