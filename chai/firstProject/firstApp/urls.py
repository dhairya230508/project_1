from django.urls import path
from . import views

urlpatterns = [
    path('', views.appHome, name='appHome'),
    path('chai-detail/<int:chai_id>',views.chaiDetail, name="chaiDetail"),
]