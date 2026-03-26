from django.urls import path
from . import views
urlpatterns = [
    # path('admin/', admin.site.urls),
    path('',views.home, name='home'),
    path('about/',views.about, name='about'),
    path('menu/',views.menu, name='menu'),
    path('food/',views.food, name='food'),
    path('order/',views.order, name='order'),
    path('combo/',views.combo,name='combo'),
    path('contact/',views.contact,name='contact'),
    path("cart/", views.cart_view, name="cart"),
    path("cart/add/<str:item_key>/", views.cart_add, name="cart_add"),
    path("cart/update/<str:item_key>/", views.cart_update, name="cart_update"),
    path("cart/remove/<str:item_key>/", views.cart_remove, name="cart_remove"),
    path("cart/checkout/", views.cart_checkout, name="cart_checkout"),
]
