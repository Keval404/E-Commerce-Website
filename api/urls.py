from django.urls import path, re_path
from . import views
from .views import ItemView, ItemInfo


urlpatterns = [
    # path('', views.getRoutes),
    # path('get/', views.getItem),
    # path('get/<str:pk>/', views.getItems),
    # path('post/', views.post),
    # path('put/<str:pk>', views.put),
    path('delete/<str:pk>', views.delete),
    path('apis/', ItemView.as_view(), name="apis"),
    path('apis/<int:id>/', ItemInfo.as_view())

]
