
from django.urls import include, path
from . import views
from rest_framework import routers
#from .views import AddProductViewSet
router = routers.DefaultRouter()
router.register(r'product', views.ProductViewSet)
router.register(r'store', views.AdminStoreViewSet)
router.register(r'order', views.OrderViewSet)


urlpatterns = [
    path('rest/', include(router.urls)),
    path('rest-auth/', include('rest_auth.urls')),
    #path('api-auth/', include('rest_framework.urls')),
    #path('addproduct/', views.AddProductViewSet.as_view(), name='addproduct'),
]

