#!/usr/bin/python
# -*- coding: UTF-8 -*-
import time
import os
from django.core import mail
from django.test import TestCase
from toollib.email import send_mail, send_html_template_email



class EmailTestCases(TestCase):
    """test email

    """

    def test_send_email_not_use_thread(self):
        send_mail("subject_not_use_thread", "body_not_use_thread", ["test@funshion.com"], [], False)
        self.assertEquals(len(mail.outbox), 1)
        self.assertEquals(mail.outbox[0].subject, 'subject_not_use_thread')
        self.assertEquals(mail.outbox[0].body, 'body_not_use_thread')

    def test_send_email_use_thread(self):
        send_mail("subject_use_thread", "body_use_thread", ["test@funshion.com"], [], True)
        time.sleep(1)
        self.assertEquals(len(mail.outbox), 1)
        self.assertEquals(mail.outbox[0].subject, 'subject_use_thread')
        self.assertEquals(mail.outbox[0].body, 'body_use_thread')

    def test_send_html_template_email(self):
        send_html_template_email("template_subject_not_use_thread", 'email.html', {'username':'test'}, ["hucj@funshion.com"], [], False)
        self.assertEquals(len(mail.outbox), 1)
        self.assertEquals(mail.outbox[0].subject, 'template_subject_not_use_thread')
        self.assertEquals(mail.outbox[0].body, u'<html>\r\n<body>\r\nhello <strong>test</strong>\r\nyour account activated.\r\n</body>')

    def test_send_html_template_email_use_thread(self):
        send_html_template_email("template_subject_use_thread", 'email.html', {'username':'test'}, ["hucj@funshion.com"], [], True)
        time.sleep(1)
        self.assertEquals(len(mail.outbox), 1)
        self.assertEquals(mail.outbox[0].subject, 'template_subject_use_thread')
        self.assertEquals(mail.outbox[0].body, u'<html>\r\n<body>\r\nhello <strong>test</strong>\r\nyour account activated.\r\n</body>')

class RenderTestCases(TestCase):

    def test_render_json(self):
        pass