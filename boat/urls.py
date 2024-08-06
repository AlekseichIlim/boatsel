from django.urls import path

from boat.apps import BoatConfig
from boat.views import BoatListView, BoatDetailView

app_name = BoatConfig.name

urlpatterns = [
    # path('materials/create/', MaterialCreateView.as_view(), name='create'),
    path('', BoatListView.as_view(), name='boat_list'),
    path('<int:pk>/', BoatDetailView.as_view(), name='boat_view'),
    # path('edit/<int:pk>/', MaterialUpdateView.as_view(), name='edit'),
    # path('delete/<int:pk>/', MaterialDeleteView.as_view(), name='delete'),
]