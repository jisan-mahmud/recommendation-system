from django.urls import path
from .views import *


urlpatterns = [
    path('', ProductListView.as_view()),
    path('<int:pk>/', ProductDetailsView.as_view(), name= 'product-detail')
]
