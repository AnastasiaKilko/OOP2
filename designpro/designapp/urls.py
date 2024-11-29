from django.urls import path
from . import views
from django.conf.urls import url


app_name = 'main'

urlpatterns = [
    #path('<str:page>/', views.other_page, name='other'),
    url(r'^$', views.index, name='index'),
    url(r'^applications/$', views.ApplicationListView.as_view(), name='applications'),
    url(r'^account/login/$', views.BBLoginView.as_view(), name='login'),
    url(r'^accounts/profile/change/$', views.ChangeUserInfoView.as_view(), name='profile_change'),
    url(r'^account/profile/$', views.profile, name='profile'),
    url(r'^accounts/logout/$', views.BBLogoutView.as_view(), name='logout'),
    url(r'^accounts/password/change/$', views.BBPasswordChangeView.as_view(), name='password_change'),
    url(r'^accounts/register/done/$', views.RegisterDoneView.as_view(), name='register_done'),
    url(r'^accounts/register/$', views.RegisterUserView.as_view(), name='register'),
]
