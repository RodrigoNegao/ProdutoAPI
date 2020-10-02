from django.urls import include, path
from pages.views import (product_update_view,
                        product_delete_view)

urlpatterns = [
    path('<int:pk>/update/', product_update_view, name='product-update'),
    path('<int:pk>/delete/', product_delete_view, name='product-delete'),
]