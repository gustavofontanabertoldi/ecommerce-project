from django.urls import path
from . import views

app_name = 'order'

urlpatterns = [
    path('', views.Pay.as_view(), name='pay'),
    path('saveorder/', views.SaveOrder.as_view(), name='saveorder'),
    path('detail/', views.Detail.as_view(), name='detail')
]
