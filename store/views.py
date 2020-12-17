import json
from builtins import print
from json import loads

from django.conf import settings
from django.contrib.auth import (authenticate, login, logout,
                                 update_session_auth_hash)
from django.contrib.auth.forms import (AuthenticationForm, PasswordChangeForm,
                                       UserCreationForm)
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.shortcuts import render
from django.urls import reverse, reverse_lazy
from django.views import generic
from django.views.generic import View
from django.views.generic.edit import CreateView

from .forms import EditUserProfileForm, UpdateUserForm, UserRegisterForm
from .models import *


class SignUpView(SuccessMessageMixin, CreateView):
    template_name = 'store/signup.html'
    success_url = reverse_lazy('login')
    form_class = UserRegisterForm
    success_message = "Your profile was created successfully"


class LoginView(generic.View):
    form_class = AuthenticationForm
    template_name = 'store/login.html'

    def get(self, request, *args, **kwargs):
        form = self.form_class(request=request)
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = self.form_class(request=request, data=request.POST)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(username=username, password=password)

            if user is not None:
                if user.is_active:
                    login(request, user)

                return HttpResponseRedirect('store')
            else:
                return HttpResponse("Inactive user.")
        else:
            return HttpResponseRedirect(settings.LOGIN_REDIRECT_URL)

        return render(request, "store/store.html")


class LogoutView(generic.RedirectView):
    
    def get_redirect_url(self, *args, **kwargs):
            logout(self.request)
            return reverse('login')
            
class UpdateUserView(LoginRequiredMixin, generic.UpdateView):
    form_class = UpdateUserForm
    template_name = 'store/update_user.html' 

    def get(self, request, *args, **kwargs):
        form = self.form_class(initial=self.initial, instance = request.user)
        context = {'form': form}
        return render(request, 'store/update_user.html', context)

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST, instance = request.user)
        context = {'form': form}
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')

        return render(request, 'store/update_user.html', context )

class UpdatePasswordView(LoginRequiredMixin, generic.FormView):
    form_class = PasswordChangeForm
    template_name = 'store/change_password.html' 

    def get(self, request, *args, **kwargs):
        form = self.form_class(initial=self.initial, user = request.user)
        context = {'form': form}
        return render(request, 'store/change_password.html', context)

    def post(self, request, *args, **kwargs):
        form = self.form_class(data = request.POST, user = request.user)
        context = {'form': form}
        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)
            return HttpResponseRedirect('/')

        return render(request, 'store/change_password.html', context )
        


def store(request):
    products = Product.objects.all()
    context = {'products':products}
    return render(request, 'store/store.html', context)

def cart(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        items = order.orderitem_set.all()
    else:
        items =[]
        order = {'get_cart_total':0, get_cart_items:0 }
    context = {'items':items, 'order':order}
    return render(request, 'store/cart.html', context)

def checkout(request):
    
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        items = order.orderitem_set.all()
    else:
        items =[]
        order = {'get_cart_total':0, get_cart_items:0 }
    context = {'items':items, 'order':order}
    return render(request, 'store/checkout.html', context)

def profile(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = EditUserProfileForm(request.POST, instance=request.user)
            if form.is_valid():
                form.save()
        else:
            form = EditUserProfileForm(instance=request.user)
        return render(request, 'store/profile.html', {'name': request.user, 'form': form})
    else:
        return render('store/store.html')

def updateItem(request):
    data = json.loads(request.body)
    productId = data['productId']
    action = data['action']

    print('action:', action)
    print('productId', productId)

    return JsonResponse('Item was added', safe=False)
