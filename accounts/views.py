from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth import login,logout
from django.urls import reverse_lazy
from django.views.generic import FormView,View
from django.contrib.auth.views import LoginView
from accounts.forms import UserRegisterForm
from django.contrib.auth.forms import AuthenticationForm

# Create your views here.
############# User Register View ##################
class UserRegisterView(FormView):
    template_name = 'accounts/form.html'
    form_class = UserRegisterForm
    success_url = reverse_lazy('home')

    def form_invalid(self, form):
        messages.error(self.request, 'There was an server error try again later!!')
        return super().form_invalid(form)
        
    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        messages.success(self.request, 'user registered successfully done')
        return super().form_valid(form)
    

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = 'Register'
        return context

############# User Login View ##################
class UserLoginView(LoginView):
    template_name = 'accounts/form.html'
    form_class = AuthenticationForm

    def form_invalid(self, form):
        messages.error(self.request, 'please provide valid user credentials.')
        return super().form_invalid(form)
    
    def get_success_url(self):
        messages.success(self.request, 'user logged in successful')
        return reverse_lazy('home')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Login"
        return context
    
############# User Logout View ##################
class UserLogoutView(View):
    def get(self,request):
        if request.user.is_authenticated:
            logout(request)
            messages.success(self.request, 'user logged out successful.')
            return redirect('login')
    
    
        
    