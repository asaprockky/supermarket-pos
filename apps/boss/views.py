from django.shortcuts import render
from django.views.generic import TemplateView
from .forms import UserSignUpForm, UserLoginForm
from django.views.generic.edit import CreateView
from django.contrib.auth.views import LoginView
from django.contrib.auth import login
from django.contrib.auth.mixins import LoginRequiredMixin

from django.urls import reverse_lazy
# Create your views here.


class SignUpVIew(CreateView):
    form_class = UserSignUpForm
    template_name = 'boss/signup.html'


class BossLoginView(LoginView):
    form_class = UserLoginForm
    template_name = 'boss/login.html'
    redirect_authenticated_user = True

    def form_valid(self, form):
        # Log in the user
        login(self.request, form.get_user())
        return super().form_valid(form)

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs.pop('instance', None)  # Prevent previous TypeError
        return kwargs
    

class BossMainView(LoginRequiredMixin, TemplateView):
    template_name = 'boss/boss_dashboard.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['first_name'] = self.request.user.first_name
        context['last_name'] = self.request.user.last_name
        print(context)
        return context 

class BossMarketDetails(TemplateView):
    template_name = 'boss/boss_market_details.html'



class BossUsers(TemplateView):
    template_name = 'boss/boss_users.html'