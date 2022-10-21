from django.urls import path
from .views import MinerView

urlpatterns = [
    path('machinedata/', MinerView.as_view())
]