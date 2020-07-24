from django.urls import path
from . import views

urlpatterns = [
    path('detail/<int:pk>', views.read, name="detail"),
    path('create/', views.create, name="create"),
    path('update/<int:pk>', views.update, name="update"),
    path('delete/<int:pk>', views.delete, name="delete")
]