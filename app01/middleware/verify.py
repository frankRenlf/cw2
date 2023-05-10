import numpy
from django.utils.deprecation import MiddlewareMixin
from django.shortcuts import redirect


class Authorise(MiddlewareMixin):
    def process_request(self, request):
        if request.path_info in ["/login", "/image/code"]:
            return
        if not request.session.get("info"):
            return redirect('/login')

    def process_response(self, request, response):
        return response


if __name__ == "__main__":
    thisdict = {
        "brand": "Porsche",
        "model": "911",
        "year": 1963
    }
    print(type(thisdict))
    print(type([{
        "name": "fff"
    }][0]))
