# -*- coding: UTF-8 -*-
import threading

from django.core.mail import EmailMessage
from django.conf import settings
from django.core.mail import EmailMultiAlternatives
from django.template.loader import get_template
from django.template import Context



def send_mail(subject, body, to, cc, use_thread=True):
    if use_thread:
        thread = threading.Thread(target=_send_mail,
                                  name="send_email_cli",
                                  args=(subject, body, to, cc))
        thread.setDaemon(True)
        thread.start()
    else:
        _send_mail(subject, body, to, cc)

def send_html_template_email(subject, template_name, data, to, cc, use_thread=True):
    if use_thread:
        thread = threading.Thread(target=_send_html_template_email,
                                  name="send_template_email_cli",
                                  args=(subject, template_name, data, to, cc))
        thread.setDaemon(True)
        thread.start()
    else:
        _send_html_template_email(subject, template_name, data, to, cc)

def _send_mail(subject, msg, to, cc):

    message = EmailMessage(subject, msg, settings.EMAIL_FROM, to, [], cc=cc)
    message.send()

def _send_html_template_email(subject, template_name, data, to, cc):
    
    html_template = get_template(template_name)
    content = Context(data)
    html_content = html_template.render(content)

    message = EmailMultiAlternatives(subject, html_content, settings.EMAIL_FROM, to=to)
    message.attach_alternative(html_content, "text/html")
    message.send()