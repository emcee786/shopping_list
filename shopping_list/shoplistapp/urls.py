from django.urls import path
from . import views

urlpatterns = [ 
    path("", views.item_list, name="item-list"),
    path("item/<int:pk>/update", views.item_update, name = "item-update"),
    path("item/<int:pk>/delete", views.item_delete, name = "item-delete")
]
