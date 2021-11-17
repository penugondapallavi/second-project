from django.urls import path
from app1.views import dhoni
app_name='app1'
urlpatterns = [
    path('dhoni/',dhoni,name='dhoni'),
]