from django.http import HttpResponseRedirect
from forms import VerificationCodeForm
from toollib.render import render_template
from toollib.render import render_json

@render_json
def home(request):
    if request.POST:
        form = VerificationCodeForm(request.POST)
        if form.is_valid():
            return HttpResponseRedirect(request.path + '?ok')
    else:
        form = VerificationCodeForm()
    return render_template('home.html', request, form=form)
