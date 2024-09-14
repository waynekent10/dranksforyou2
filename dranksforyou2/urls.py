"""
URL configuration for dranksforyou2 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.conf.urls import include
from django.urls import path
from rest_framework import routers
from dranksforyou2api.views import check_user, register_user
from dranksforyou2api.views import UserView, OrderView, BeverageView, LiquorView, IngredientView, OrderBeverageView


router = routers.DefaultRouter(trailing_slash=False)
router.register(r'user', UserView, 'user')
router.register(r'order', OrderView, 'order')
router.register(r'beverage', BeverageView, 'beverage')
router.register(r'liquor', LiquorView, 'liquor')
router.register(r'ingredient', IngredientView, 'ingredient')
router.register(r'orderbeverage', OrderBeverageView, 'orderbeverage')


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('register', register_user),
    path('checkuser', check_user),
]
