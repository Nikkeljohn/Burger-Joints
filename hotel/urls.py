from . import views
from django.urls import path

urlpatterns = [
    path('', views.PostList.as_view(), name='home'),
     path('contact/',views.contact_us,name="contact"),
    path('about/',views.about,name="about"),
    path('team/',views.team_members,name="team"),
    path('dishes/',views.all_dishes,name="all_dishes"),
    path('register/',views.register,name="register"),
    path('check_user_exists/',views.check_user_exists,name="check_user_exist"),
    path('login/', views.signin, name='login'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('logout/', views.user_logout, name='logout'),
    path('dish/<int:id>/', views.single_dish, name='dish'),
    path('menu/', views.menu,name='menu'),    
    path('dishes/',views.all_dishes,name="all_dishes"),
    path('dish/<int:id>/', views.single_dish, name='dish'),
    path('delete_dish/<slug:pk>/', views.DeleteDish.as_view(),name='delete_dish')
    #path('<slug:slug>/', views.PostDetail.as_view(), name='post_detail'),
    #path('like/<slug:slug>', views.PostLike.as_view(), name='post_like'),
]