from django.urls import path, include
from rest_framework import routers
from payments.views import PaymentView

from products.views import CategoryDetail,CategoryList,ProductDetail,ProductList,OrderDetail,OrderList
from reviews.views import ReviewSet
from users.views import UserViewSet

user_router = routers.DefaultRouter()
user_router.register(r'users', UserViewSet, basename='user')

review_router = routers.DefaultRouter()
review_router.register(r'reviews', ReviewSet, basename='review')

app_name = 'api'
urlpatterns = [
    path('', include(user_router.urls)),
    path('', include(review_router.urls)),
    path('products/', ProductList.as_view(), name='product-list'),
    path('products/<int:pk>', ProductDetail.as_view(), name='products-detail'),
    path('categories/', CategoryList.as_view(), name='category-list'),
    path('categories/<int:pk>', CategoryDetail.as_view(), name='category-detail'),
    path('orders/', OrderList.as_view(), name='order-list'),
    path('orders/<int:pk>', OrderList.as_view(), name='order-detail'),
    path('payment/', PaymentView.as_view(), name='payment'),
]