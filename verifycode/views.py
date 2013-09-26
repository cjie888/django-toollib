from django.http import HttpResponseRedirect
from forms import CaptchaForm
from toollib.render import render_template
from toollib.render import render_json

@render_json
def home(request):
    if request.POST:
        form = CaptchaForm(request.POST)
        if form.is_valid():
            return HttpResponseRedirect(request.path + '?ok')
    else:
        form = CaptchaForm()
    return render_template('home.html', request, form=form)
