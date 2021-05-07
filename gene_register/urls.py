from django.urls import path,include
from . import views

urlpatterns = [
    path('', views.gene_form,name='gene_insert'), # get and post req. for insert operation
    path('<int:id>/', views.gene_form,name='gene_update'), # get and post req. for update operation
    path('delete/<int:id>/',views.gene_delete,name='gene_delete'),
    path('list/',views.gene_list,name='gene_list') # get req. to retrieve and display all records
]