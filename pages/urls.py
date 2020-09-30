from django.urls import include, path
from pages.views import ProductListView

urlpatterns = [
    # path('listProduct/', ProductListView.as_view(), name='listProduct')
    path('listProduct/', ProductListView, name='listProduct'),
]