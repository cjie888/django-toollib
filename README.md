Django-toollib is a common module building on top of django, include sending email, rendering template, pagination, verification code etc.
 
If you have any question, please contact **dev-web-sys@funshion.com** 
### Sending Email <br/>
You should change the email configuration in setting.py file first.
<pre>
EMAIL_HOST = "mail.XXXXX.com"
EMAIL_HOST_USER = "email_user"
EMAIL_HOST_PASSWORD = "email_password"
EMAIL_PORT = 25
EMAIL_USE_TLS = False
EMAIL_FROM = "email_from"
</pre>
* Sending normal email  <br/>
<br/>
Programing interface: 
<pre>
send_mail(subject, body, to, cc, use_thread=True) </pre>
Parameters: 
<pre>
subject - the email subject
body  - the email body
to - the recipients (a list)
cc - copy to(a list)
use_thread - whether to start a thread to send email </pre> <br/>
<br/>
A simple example demonstrating the use of the programmatic interface:
<pre>
from toollib.email import send_mail
send_mail("subject_not_use_thread", "body_not_use_thread", ["xxx@domain.com"], [], False)
</pre>
* Sending html template email <br/>
<br/>
Programing interface:
<pre> 
send_html_template_email(subject, template_name, data, to, cc, use_thread=True)</pre>
Parameters: 
<pre>
template_name - the email template
data  - the data render the template(a dictionary)
the parameters of subject, to, cc, use_thread is the same as sending noraml email.</pre> <br/>
<br/>            
A simple example demonstrating the use of the programmatic interface:
<pre>
from toollib.email import send_html_template_email
send_html_template_email("template_subject_not_use_thread", 'email.html', {'username':'test'}, ["xxx@domain.com"], [], False)
</pre>

### Rendering template and json <br/>
* render json <br/>
It is a decorator which wrapping the json or data to http response.
* render template  <br/>
<br/>
Programing interface:
<pre> 
render_template(template, request, **kwargs)</pre>
Parameters: 
<pre>
template - the template name
request - the http request
kwargs - the template parameter</pre> <br/>           
A simple example demonstrating the use of the programmatic interface:
<pre>
from toollib.render import render_template
response = render_template('email.html', None, username = 'render_test')
</pre>

### Pagination <br/>
<br/>
Programing interface:
<pre> 
get_page(query_set, page_no, page_size)</pre>
Parameters: 
<pre>
query_set - the query set
page_no  - the page no (int)
page_size - the page size of every page</pre> <br/>
<br/>            
A simple example demonstrating the use of the programmatic interface:
<pre>
from toollib.page import get_page
query_set = MyModel.objects.all()
page = get_page(query_set, 2, 3)
</pre>
### Get Client(user) IP Address <br/>
A simple example demonstrating the use of the programmatic interface:
<pre>
from toollib.client import get_client_ip
clinet_ip = get_client_ip(request)
</pre>
If you use nginx as a proxy, you should add configuration in nginx.conf.
<pre>
proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
</pre>
If you use haproxy as a proxy, you should add configuration in haproxy.cfg.
<pre>
option forwardfor
</pre>
### [Verification Code](code.md) <br/>
