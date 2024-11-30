from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404
from django.template import TemplateDoesNotExist
from django.template.loader import get_template
from django.contrib.auth.views import LoginView, LogoutView, PasswordChangeView
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Application, AdvUser
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, TemplateView
from .forms import ChangeUserInfoForm, RegisterUserForm
from django.views import generic


# Create your views here.
def index(request):
    applications_done = Application.objects.filter(status__exact='d')[:4]
    num_applications_accepted = Application.objects.filter(status__exact='a').count()

    return render(
        request, 'main/index.html', {'applications_done': applications_done,
                                'num_applications_accepted': num_applications_accepted})


def other_page(request, page):
    try:
        template = get_template('main/' + page + '.html')
    except TemplateDoesNotExist:
        raise Http404
    return HttpResponse(template.render(request=request))


class BBLoginView(LoginView):
    template_name = 'main/login.html'


@login_required
def profile(request):
   # personal_applications = PersonalApplicationListView.as_view()
    return render(request, 'main/profile.html')
                  #{'personal_applications': personal_applications})

class BBLogoutView(LoginRequiredMixin, LogoutView):
    template_name = 'main/logout.html'


class ChangeUserInfoView(SuccessMessageMixin, LoginRequiredMixin, UpdateView):
    model = AdvUser
    template_name = 'main/change_user_info.html'
    form_class = ChangeUserInfoForm
    success_url = reverse_lazy('main:profile')
    success_message = 'Personal data has been updated.'

    def dispatch(self, request, *args, **kwargs):
        self.user_id = request.user.pk
        return super().dispatch(request, *args, **kwargs)

    def get_object(self, queryset=None):
        if not queryset:
            queryset = self.get_queryset()
        return get_object_or_404(queryset, pk=self.user_id)


class BBPasswordChangeView(SuccessMessageMixin, LoginRequiredMixin, PasswordChangeView):
   template_name = 'main/password_change.html'
   success_url = reverse_lazy('main:profile')
   success_message = 'Your password has been updated.'

class RegisterUserView(CreateView):
   model = AdvUser
   template_name = 'main/register_user.html'
   form_class = RegisterUserForm
   success_url = reverse_lazy('main:register_done')

class RegisterDoneView(TemplateView):
   template_name = 'main/register_done.html'


# class ApplicationListView(generic.ListView):
#     model = Application
#     paginate_by = 4
#
#
class PersonalApplicationListView(generic.ListView):
    model = Application
    paginate_by = 4

    def get_queryset(self):
        return Application.objects.filter(author=self.request.user)
#
# # class ApplicationDetailView(generic.DetailView):
# #     model = Application
# #
