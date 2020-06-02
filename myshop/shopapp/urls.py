from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

urlpatterns = [
	path('products/', views.product_list),
    path('products/<int:pk>/', views.product_detail),
    path('category/', views.category_list),
    path('category/<int:pk>/', views.category_detail),
]

urlpatterns = format_suffix_patterns(urlpatterns)