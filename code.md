This module is based on project [django-simple-captcha](https://github.com/mbi/django-simple-captcha) which is an extremely simple,
yet highly customizable Django application to add captcha images to any Django form. We increase function -- image ajax refresh,  field custom etc. 

### Install django-simple-captcha 
This projct is rely on django-simple-captcha, so you should install it first.

* Download django-simple-captcha using pip by running: pip install django-simple-captcha

* Add captcha to the INSTALLED_APPS in your settings.py

* Run python manage.py syncdb (or python manage.py migrate if you are managing databae migrations via South) to create the required database tables

### Adding to a Form 
Using a VerificationCodeField is quite straight-forward:

* Define the Form <br/>
To embed a verification code in your forms, simply add a VerificationCodeField to the form definition:
<pre>
from django import forms
from toollib.verificationcode  import VerificationCodeField, VerificationCodeTextInput
</pre>
<pre>
class VerificationCodeForm(forms.Form):
    verificationcode = VerificationCodeField(widget=VerificationCodeTextInput({"class": "test"}))
</pre>

* Validate the Form <br/>
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

### Define Django Url

Add entries in your urls.py file like this:
<pre>
    url(r'^code/$', 'views.home'),
    url(r'^code/captcha/', include('captcha.urls')),
    url(r'code/image/(?P<key>\w+)/$','captcha.views.captcha_image',name='verificationcode-image'),
    url(r'code/new/key/$','toollib.verificationcode.captcha_new_key',name='verificationcode-new-key'),
</pre>

### Use Field in the Form

<pre>
	&lt;form action="." method="post"&gt;
		{% csrf_token %} {{form.verificationcode.errors}} {{form.verificationcode}}
		&lt;input type="button" id="js-verificationcode-refresh" value="change" /&gt;
		&lt;input type="submit" value="Submit" /&gt;
	&lt;/form&gt;
</pre>

### Use Ajax to Refresh Image <br>

use jquery: 
<pre>
		$(document).ready(function() {
			$('#js-verificationcode-refresh').click(function () {
				$.get('{% url "verificationcode-new-key" %}', function(data) {
					var image_url = '{% url "verificationcode-image"  0 %}';
					image_url = image_url.replace('/0', '/' + data);
					$('.verificationcode').attr('src', image_url);
				});
			});
		});

</pre>

### Advanced Configuration
#### Generators and modifiers <br/>

* Random chars <br/>
Classic captcha that picks four random chars. This is case insensitive.
<pre>
CAPTCHA_CHALLENGE_FUNCT = 'captcha.helpers.random_char_challenge'
</pre>
* Simple Math <br/>
Another classic, that challenges the user to resolve a simple math challenge by randomly picking two numbers between one and nine, and a random operator among plus, minus, times.
<pre>
CAPTCHA_CHALLENGE_FUNCT = 'captcha.helpers.math_challenge'
</pre>
* Dictionary Word  <br/>
Picks a random word from a dictionary file. Note, you must define CAPTCHA_WORDS_DICTIONARY in your cofiguration to use this generator.
<pre>
CAPTCHA_CHALLENGE_FUNCT = 'captcha.helpers.word_challenge'
</pre>

