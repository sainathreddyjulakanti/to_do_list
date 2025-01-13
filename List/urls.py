from django.urls import path
from . import views

urlpatterns=[
    path('',views.show,name="task_list"),
    path('add/',views.add_item,name='add_item'),
    path('delete/<int:S_No>/',views.delete,name='delete_item'),
    path('update/<int:S_No>/',views.update,name='update_item'),
]