from django.urls import path
from user import views as UserViews
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView
)
from products import views as ProductViews
from cart import views as Cartviews

urlpatterns = [
    path('register/', UserViews.RegisterView.as_view(), name = 'register'),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('profile/', UserViews.ProfileView.as_view(), name='profile'),
    path("categories/", ProductViews.CategoryListView.as_view()),
    path("products/", ProductViews.ProductListView.as_view()),
    path("products/<int:pk>/",ProductViews.ProductDetailView.as_view()),
    path("cart/", Cartviews.CartListView.as_view()),
    path("cart/add/", Cartviews.AddToCartView.as_view()),

]
