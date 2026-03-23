from django.urls import path
from . import views
urlpatterns = [
    # path('admin/', admin.site.urls),
    path('',views.home, name='home'),
    path('about/',views.about, name='about'),
    path('menu/',views.menu, name='menu'),
    path('food/',views.food, name='food'),
    path('combo/',views.combo,name='combo'),
    path('contact/',views.contact,name='contact'),
]
