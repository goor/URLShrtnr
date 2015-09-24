from django.shortcuts import render,render_to_response, get_object_or_404
import random, string, json
from shorturlEng.models import Urls
from django.http import HttpResponseRedirect, HttpResponse
from django.conf import settings
from django.core.context_processors import csrf
from django.views.decorators.csrf import csrf_exempt
def index(request):
    c = {}
    c.update(csrf(request))
    return render_to_response('shorturlEng/r4.html', c)

def redirectOriginal(request, short_id):
    url = get_object_or_404(Urls, pk=short_id) # get object, if not found return 404 error
    return HttpResponseRedirect('http://'+url.url)

@csrf_exempt
def shortenUrl(request):
    url_post = request.POST.get("url", '')
    if not (url_post== ''):
        id_short = getShortCode()
        b = Urls(url=url_post, id=id_short)
        b.save()

        response_data = {}
        response_data['url'] = settings.SITE_URL + "/" +id_short
        return HttpResponse(json.dumps(response_data), content_type="application/json")
    return HttpResponse(json.dumps({"error": "error occurs"}),
             content_type="application/json")

def getShortCode():
    length = 12
    char = string.ascii_uppercase + string.digits + string.ascii_lowercase
    # if the randomly generated short_id is used then generate next
    while True:
        short_id = ''.join(random.choice(char) for x in range(length))
        try:
            temp = Urls.objects.get(pk=short_id)
        except:
            return short_id