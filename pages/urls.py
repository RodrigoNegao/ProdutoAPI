from django.urls import include, path
from pages.views import (ProductListView,
                        product_update_view,
                        ProductDeleteView)

urlpatterns = [
    # path('listProduct/', ProductListView.as_view(), name='listProduct')
    path('listProduct/', ProductListView, name='listProduct'),
    path('<int:pk>/update/', product_update_view, name='product-update'),
    path('<int:pk>/delete/', ProductDeleteView.as_view(), name='product-delete'),
]