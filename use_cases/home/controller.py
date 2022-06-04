from .use_case import HomeUseCase
from flask import request

class HomeController:
  def execute(self):
    request_data = request.get_json()
    name = request_data['name']

    if request.method != 'POST':
      return "Invalid Method"

    return HomeUseCase().execute(name)