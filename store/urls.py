from os import name, path

from django.contrib.auth import views as auth_views
from django.urls import path

from . import views
from .views import (LoginView, LogoutView, SignUpView, UpdatePasswordView,
                    UpdateUserView, OrderHistory, ViewOrder, SearchView)

urlpatterns = [
    path('store/', views.store, name="store"),
    path('cart/', views.cart, name="cart"),
    path('checkout/', views.checkout, name="checkout"),
    path('profile/', views.profile, name="profile"),
    path('update_item/', views.updateItem, name="update_item"),
    path('process_order/', views.processOrder, name="process_order"),
    path('order_history/', OrderHistory.as_view(), name='order_history'),
    path('order/<int:order_id>', ViewOrder.as_view(), name='order_detail'),
    path('search/', SearchView.as_view(), name='search'),
   

    path('signup/', SignUpView.as_view(), name='signup'),
    path('', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('update_user/', UpdateUserView.as_view(), name='update_user'),
    path('change_password/', UpdatePasswordView.as_view(), name='change_password'),

    path('reset_password/', auth_views.PasswordResetView.as_view(
        template_name='store/password_reset_form.html'), name='reset_password'),
    path('reset_password_sent/', auth_views.PasswordResetDoneView.as_view(
        template_name='store/password_reset_done.html'), name='password_reset_done'),
    path('reset/<uidb64>/<token>', auth_views.PasswordResetConfirmView.as_view(
        template_name='store/password_reset_confirm.html'), name='password_reset_confirm'),
    path('reset_password_complete/', auth_views.PasswordResetCompleteView.as_view(
        template_name='store/password_reset_complete.html'), name='password_reset_complete'),

]
