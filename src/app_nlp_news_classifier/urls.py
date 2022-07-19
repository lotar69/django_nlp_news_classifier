from django.urls import path
from .views import index, result

app_name = "app_nlp_news_classifier"

urlpatterns = [
    path('', index, name="index"),
    path('result', result, name="result")
]
