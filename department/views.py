from django.shortcuts import render
from django.views.generic import CreateView


class RegistrationView(CreateView):
    pass


def main(request):
    return render(request, 'main.html')


# Create your views here.
