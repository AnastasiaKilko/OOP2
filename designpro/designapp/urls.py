from django.urls import path
from . import views

app_name = 'main'

urlpatterns = [
    path('<str:page>/', views.other_page, name='other'),
    path('', views.index, name='index'),
    path('account/login', views.BBLoginView.as_view(), name='login'),
    path('accounts/profile/change/', views.ChangeUserInfoView.as_view(), name='profile_change'),
    path('account/profile/', views.profile, name='profile'),
    path('acconts/logout/', views.BBLogoutView.as_view(), name='logout'),
    path('accounts/password/change/', views.BBPasswordChangeView.as_view(), name='password_change'),
    path('accounts/register/done/', views.RegisterDoneView.as_view(), name='register_done'),
    path('accounts/register/', views.RegisterUserView.as_view(), name='register'),
]
