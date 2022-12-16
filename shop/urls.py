from django.urls import path
from . import views

app_name = 'shop'
urlpatterns = [
    path('', views.product_list, name='product_list'),  # calls view without any parameters
    path('slug/categort_slug', views.product_list, name='product_list_by_category'),  # uses slug parameter to filter
    # products by category
    path('<int:id>/<slug:slug>/', views.product_detail, name="product_detail")  # uses slug and id to view specific item
]
