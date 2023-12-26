"""codestar URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.urls import path, include
from hotel import views 
from django.conf import settings 
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('hotel.urls')),
    path('contact/',views.contact_us,name="contact"),
    path('products/', include('products.urls')),

    # path('about/',views.about,name="about"),
    # path('team/',views.team_members,name="team"),
    # path('dishes/',views.all_dishes,name="all_dishes"),
    # path('register/',views.register,name="register"),
    # path('check_user_exists/',views.check_user_exists,name="check_user_exist"),
    # path('login/', views.signin, name='login'),
    # path('dashboard/', views.dashboard, name='dashboard'),
    # path('logout/', views.user_logout, name='logout'),
    # path('dish/<int:id>/', views.single_dish, name='dish'),
    # path('menu/', views.menu,name='menu'),    
    # path('dishes/',views.all_dishes,name="all_dishes"),
    # path('dish/<int:id>/', views.single_dish, name='dish'),
    # path('delete_dish/<slug:pk>/', views.DeleteDish.as_view(),name='delete_dish')
]+static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
