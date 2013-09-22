Django-toollib is a common module building on top of django, include sending email, rendering template, pagination etc. 

### Sending Email
<br/>
* Sending normal email  <br/>
<br/>
Programing interface: <pre> send_mail(subject, body, to, cc, use_thread=True)</pre> <br/>
Parameters: 
<pre>
subject - the email subject <br/>
body  - the email body <br/>
to - the recipients (a list) <br/>
cc - (a list) <br/>
use_thread - whether to start a thread to send email </pre> <br/>
<br/>
A simple example demonstrating the use of the programmatic interface:
<pre>
from toollib.email import send_mail
send_mail("subject_not_use_thread", "body_not_use_thread", ["xxx@funshion.com"], [], False)
</pre>
* Sending html template email <br/>
<br/>
Programing interface:
<pre> 
send_html_template_email(subject, template_name, data, to, cc, use_thread=True)</pre> <br/>
Parameters: 
<pre>
template_name - the email template <br/>
data  - the data render the template(a dictionary) <br/>
the parameters of subject, to, cc, use_thread is the same as sending noraml email.</pre> <br/>
<br/>            
A simple example demonstrating the use of the programmatic interface:
<pre>
from toollib.email import send_html_template_email
 send_html_template_email("template_subject_not_use_thread", 'email.html', {'username':'test'}, ["xxx@funshion.com"], [], False)
</pre>
### Rendering template and json
<br/>
* render json <br/>

* render template  <br/>

### Pagination 
<br/>