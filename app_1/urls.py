from django.urls import path
from . import views
app_name = 'app_1'
urlpatterns = [
    path('', views.allprocat , name="allprocat"),
    path('<slug:c_slug>/', views.allprocat, name="products_by_category"),
    path('<slug:c_slug>/<slug:product_slug>', views.proDetail, name="prodCatdetails"),
]