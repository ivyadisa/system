from django.urls import path
from .import views

urlpatterns = [
    path('index/', views.index, name="index" ),
    path('<int:id>',views.view_student, name="view_student"),
    path('add/', views.add, name="add" ),
    path('edit/<int:id>/', views.edit, name="edit" ),
    path('', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('delete/<int:id>/',views.delete, name="delete" ),
    
    
]