from django.http import HttpResponse

def hello(request):
    return HttpResponse("Hello,world.")

def currentUrlView(request):
    return HttpResponse("Welcome to the page at %s" % request.path)

def uaDisplay1(request):
    try:
        ua = request.META["HTTP_USER_AGENT"]
    except KeyError:
        ua = "unknown"
    return HttpResponse("Your browser is %s " % ua)

def uaDisplay2(request):
    ua = request.META.get("HTTP_USER_AGENT","unknown")
    return HttpResponse("Your browser is %s " % ua)

def displayMeta(request):
    values = request.META.items()
    values.sort()
    html = []
    for k,v in values:
        html.append("<tr><td>%s</td><td>%s</td></tr>" % (k,v))
    return HttpResponse("<table>%s</table>" % "\n".join(html))
