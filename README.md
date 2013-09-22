Django-toollib is a common module building on top of django, include sending email, rendering template, pagination etc. 

### Sending Email <br/>
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
cc - (a list)
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
send_html_template_email("template_subject_not_use_thread", 'email.html', {'username':'test'}, ["xxx@funshion.com"], [], False)
</pre>
### Rendering template and json <br/>
* render json <br/>

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
<br/>            
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
query_set = ['data1', 'data2', 'data3', 'data4', 'data5', 'data6', 'data7']
page = get_page(query_set, 2, 3)
</pre>