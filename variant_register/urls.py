from django.urls import path,include
from . import views

urlpatterns = [
    path('', views.variant_form,name='variant_insert'), # get and post req. for insert operation
    path('<int:id>/', views.variant_form,name='variant_update'), # get and post req. for update operation
    path('delete/<int:id>/',views.variant_delete,name='variant_delete'),
    path('list/',views.variant_list,name='variant_list') # get req. to retrieve and display all records
]