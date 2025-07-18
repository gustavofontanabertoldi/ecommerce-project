from django.urls import path
from . import views

app_name = 'order'

urlpatterns = [
    path('pay/', views.Pay.as_view(), name='pay'),
    path('closeorder/', views.CloseOrder.as_view(), name='closeorder'),
    path('detail/', views.Detail.as_view(), name='detail')
]
