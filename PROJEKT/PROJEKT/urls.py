from django.contrib import admin
from django.urls import path
from APP.views import bigyoview

urlpatterns = [
    path('admin/', admin.site.urls),
    path('bigyo/', bigyoview),
]
