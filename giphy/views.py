import sys

from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.http.response import HttpResponseNotAllowed
from django.shortcuts import render

from .models import Gif
from .gclient import Gclient

from accounts.models import CustomUser


@login_required
def search(request):
    context = {}
    gc = Gclient()
    if request.method == 'POST' and not request.POST.get("offset"):
        # render the results from our search
        search_term = request.POST.get("search_term")
        results = gc.search(query=search_term)
        if not results or results.pagination.count < 1:
            return render(request, template_name='not_found.html')
        context['results'] = results
        context['search_term'] = search_term
        return render(request, template_name="results.html", context=context)
    elif request.method == 'POST' and request.POST.get("offset"):
        search_term = request.POST.get("search_term")
        results = gc.search(query=search_term, offset=int(request.POST.get("offset")))
        if not results or results.pagination.count < 1:
            return render(request, template_name='not_found.html')
        context['search_term'] = search_term
        context['results'] = results
        return render(request, "results.html", context=context)
    else:
        # render the search box only
        return render(request, template_name="search.html", context=context)


@login_required
def index(request):
    context = {}
    user = CustomUser.objects.filter(username=request.user).get()
    images = Gif.objects.filter(owner=user).all()
    context['images'] = images
    return render(request, template_name="index.html", context=context)


@login_required
def save(request):
    if not request.POST:
        return HttpResponseNotAllowed("POST")
    g = Gif()
    g.image_orig_url = request.POST.get('img_orig_url')
    g.image_200_url = request.POST.get('img_200_url')
    g.image_id = request.POST.get('img_id')
    g.owner = request.user
    g.save()
    for tag in request.POST.get('img_tags').split(","):
        g.image_tags.add(tag)
    g.full_clean()
    return HttpResponse(status=201)
