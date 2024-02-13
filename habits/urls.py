from django.urls import path

from habits.apps import HabitsConfig
from habits.views import HabitCreateAPIView, HabitListAPIView, HabitRetrieveAPIView

app_name = HabitsConfig.name

urlpatterns = [
    path('create/', HabitCreateAPIView.as_view(), name='habit-create'),
    path('', HabitListAPIView.as_view(), name='habit-list'),
    path('<int:pk>/', HabitRetrieveAPIView.as_view(), name='habit-get'),
]
