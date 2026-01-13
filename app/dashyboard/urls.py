from django.urls import path
from django.views.generic import TemplateView

app_name = 'dashyboard'
urlpatterns = [
    path('', TemplateView.as_view(template_name='dashyboard/home.html'), name='home'),
]