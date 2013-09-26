This module is based on project [django-simple-captcha](https://github.com/mbi/django-simple-captcha)  is an extremely simple,
yet highly customizable Django application to add captcha images to any Django form. We increase function image ajax refresh,  field custom etc. 

### Install django-simple-captcha
This projct is rely on django-simple-captcha, so you should install it first.

* Download django-simple-captcha using pip by running: pip install django-simple-captcha

* Add captcha to the INSTALLED_APPS in your settings.py

* Run python manage.py syncdb (or python manage.py migrate if you are managing databae migrations via South) to create the required database tables

### Adding to a Form
Using a VerificationCodeField is quite straight-forward:

* Define the Form <br>
To embed a verification code in your forms, simply add a VerificationCodeField to the form definition:
<pre>
from django import forms
from toollib.verificationcode  import VerificationCodeField, VerificationCodeTextInput
</pre>
<pre>
class VerificationCodeForm(forms.Form):
    verificationcode = VerificationCodeField(widget=VerificationCodeTextInput({"class": "test"}))
</pre>

* Validate the Form
In your view, validate the form as usually: if the user didn’t provide a valid response to the verification code challenge, the form will raise a ValidationError:
<pre>
from django.http import HttpResponseRedirect
from forms import VerificationCodeForm
from toollib.render import render_template
from toollib.render import render_json
</pre>
<pre>
def home(request):
    if request.POST:
        form = VerificationCodeForm(request.POST)
        if form.is_valid():
            return HttpResponseRedirect(request.path + '?ok')
    else:
        form = VerificationCodeForm()
    return render_template('home.html', request, form=form)
</pre>

### Define url

* Add entries in your urls.py file like this:
<pre>
    url(r'^code/$', 'views.home'),
    url(r'^code/captcha/', include('captcha.urls')),
    url(r'code/image/(?P<key>\w+)/$','captcha.views.captcha_image',name='verificationcode-image'),
    url(r'code/new/key/$','toollib.verificationcode.captcha_new_key',name='verificationcode-new-key'),
</pre>

### use field in the form

<pre>
	&lt;form action="." method="post"&gt;
		{% csrf_token %} {{form.verificationcode.errors}} {{form.verificationcode}}
		&lt;input type="button" id="js-verificationcode-refresh" value="change" /&gt;
		&lt;input type="submit" value="Submit" /&gt;
	&lt;/form&gt;
</pre>

### use ajax to refresh <br>

use jquery: 
<pre>
		function refresh_image() {
			$.get('{% url "captcha-new-key" %}', function(data) {
                                alert(data);
				var image_url = '{% url "captcha-image"  0 %}';
				image_url = image_url.replace('/0', '/' + data);
				$('#id_captcha_image').attr('src', image_url);
				$('#id_captcha_0').val(data);
				$('#id_captcha_1').val('');
			});
		};
</pre>

### Advanced Configuration

