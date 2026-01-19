from django.urls import path
from . import views


app_name = 'dashyboard'
urlpatterns = [
    path('', views.DeckListView.as_view(), name='all'),
    path('create/', views.DeckCreateView.as_view(), name='create'),
    path('<int:pk>/update/', views.DeckUpdateView.as_view(), name='update'),
    path('<int:pk>/delete/', views.DeckDeleteView.as_view(), name='delete'),
]