"""lunches URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.urls import path
from django.contrib.auth import views as auth_views
from django.conf.urls.static import static
from .settings import MEDIA_ROOT, MEDIA_URL


from buy_lunch.views import ShowMenu, AddLunch, AddAppetizer, AddBeverage, ShowLunches, ShowLAppetizers, ShowBeverages,\
    MakeOrder, UserOrders, LunchCalendar, SetMenu, EditMenu, ReviewOrder, RegisterView, AllOrders, DishRanking, \
    MenuDetails, TodayOrders, Users, UserDetails, LunchReview, OrderConfirm

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='logout.html'), name='logout'),
    path('register/', RegisterView.as_view(), name='register'),

    path('', ShowMenu.as_view(), name='index'),
    path('add-lunch/', AddLunch.as_view(), name='add-lunch'),
    path('add-appetizer/', AddAppetizer.as_view(), name='add-appetizer'),
    path('add-beverage/', AddBeverage.as_view(), name='add-beverage'),
    path('lunches/', ShowLunches.as_view(), name='lunches'),
    path('appetizers/', ShowLAppetizers.as_view(), name='appetizers'),
    path('beverages/', ShowBeverages.as_view(), name='beverages'),
    path('make-order/', MakeOrder.as_view(), name='make-order'),
    path('user-orders/', UserOrders.as_view(), name='user-orders'),
    path('lunch-calendar/', LunchCalendar.as_view(), name='lunch-calendar'),
    path('set-menu/', SetMenu.as_view(), name='set-menu'),
    path('order-review/<int:order_id>', ReviewOrder.as_view(), name='order-review'),
    path('edit-menu/<int:menu_id>', EditMenu.as_view(), name='edit-menu'),
    path('menu-details/<int:menu_id>', MenuDetails.as_view(), name='menu-details'),
    path('all-orders/', AllOrders.as_view(), name='all-orders'),
    path('ranking/', DishRanking.as_view(), name='ranking'),
    path('today-orders/', TodayOrders.as_view(), name='today-orders'),
    path('users/', Users.as_view(), name='users'),
    path('user-details/<int:user_id>', UserDetails.as_view(), name='user-details'),
    path('review/<int:review_id>', LunchReview.as_view(), name='review'),
    path('confirm-order/<int:order_id>', OrderConfirm.as_view(), name='confirm-order'),



    ] + static(MEDIA_URL, document_root=MEDIA_ROOT)