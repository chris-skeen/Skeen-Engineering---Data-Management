from django.contrib import admin
from django.urls import path
from app.views import *

urlpatterns = [
  
    path("admin/", admin.site.urls),
    path("all-data/", all_data_view),
    path("map", view_map),

]
