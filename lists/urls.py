from django.urls import path
from . import views
# from accounts import views

urlpatterns = [
	path('',views.index, name="index"),
	path('update/<str:pkey>', views.update, name = "update"),
	path('delete/<str:pkey>', views.delete, name = "delete"),
]
