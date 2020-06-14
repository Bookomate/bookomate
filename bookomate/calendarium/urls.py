from django.urls import path

from . import views

urlpatterns = [
    # path('', views.home, name='home'), TODO: show calendar once user is authenticated
    path('calendar/', views.calendar_view, name='calendar_view'),
    path('calendar/<int:year>/<int:month>', views.calendar_view, name='calendar_view'),
]
