from django.urls import path
from owners import views

app_name = 'owners'
urlpatterns = [
    path('owners/', views.owner_list),
    path('owners/<int:pk>', views.owner_detail),
]