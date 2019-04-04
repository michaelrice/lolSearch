from django.shortcuts import render


def home(request):
    """
    Base home landing page view.

    Renders the home.html template in the project level
    template directory

    :param request:
    :return:
    """
    return render(request, template_name="home.html")
