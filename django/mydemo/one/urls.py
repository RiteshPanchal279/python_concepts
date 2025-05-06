from django.urls import path
from one import views

urlpatterns=[
   path('',views.welcome,name='welcome'),
   path('emp_edit/<int:eid>',views.emp_edit,name=views.emp_edit),
   path('emp_delete/<int:eid>',views.emp_delete,name=views.emp_delete)
]