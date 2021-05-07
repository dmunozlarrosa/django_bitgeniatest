from django.urls import path,include
from . import views

urlpatterns = [
    path('', views.disease_form,name='disease_insert'), # get and post req. for insert operation
    path('<int:id>/', views.disease_form,name='disease_update'), # get and post req. for update operation
    path('delete/<int:id>/',views.disease_delete,name='disease_delete'),
    path('list/',views.disease_list,name='disease_list') # get req. to retrieve and display all records
]