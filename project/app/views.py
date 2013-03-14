from django.utils.translation import ugettext as _

def index(request):
    output = _("Testing translation ...")
    return HttpResponse(output)
