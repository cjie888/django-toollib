Django-toollib is a common module building on top of django, include sending email, rendering template, pagination etc. 

### Sending Email

1. Sending normal email 
Programing interface: send_mail(subject, body, to, cc, use_thread=True)
Parameters: subject - the email subject
            body  - the email body
            to - the recipients (a list)
            cc - (a list)
            use_thread - whether to start a thread to send email
Example:
<pre>
send_mail("subject_not_use_thread", "body_not_use_thread", ["xxx@funshion.com"], [], False)
</pre>

2. Sending html template email 
Programing interface: send_html_template_email(subject, template_name, data, to, cc, use_thread=True)
Parameters: template_name - the email template
            data  - the data render the template(a dictionary)
            the parameters of subject, to, cc, use_thread is the same as sending noraml email.
Example:
<pre>
 send_html_template_email("template_subject_not_use_thread", 'email.html', {'username':'test'}, ["xxx@funshion.com"], [], False)
</pre>
### Rendering template and json

1. render json

2. render template

### Pagination 