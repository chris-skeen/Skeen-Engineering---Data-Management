from django.shortcuts import render
from app.models import *
import json
from django.core.serializers.json import DjangoJSONEncoder
# Create your views here.

def all_data_view(request):
  # Always re writing json file on new page
  data = surveys.objects.values()
  json_data = json.dumps(list(data), indent=2, cls=DjangoJSONEncoder)

  file_path = "app/static/data.json"

  with open(file_path, "w") as json_file:
    json_file.write(json_data)

  return render(request, "data.html", {"data": data, "json_data": json_data})

def view_map(request):
  
  # Always re writing json file on new page
  data = surveys.objects.values()
  json_data = json.dumps(list(data), indent=2, cls=DjangoJSONEncoder)

  file_path = "app/static/data.json"

  with open(file_path, "w") as json_file:
    json_file.write(json_data)

  data = surveys.objects.all()
  return render(request, "map.html", {"data": data})