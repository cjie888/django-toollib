#!/usr/bin/python
# -*- coding: UTF-8 -*-
import time

from django.core import mail
from django.test import TestCase
from toollib.email import send_mail, send_html_template_email
from toollib.render import render_json, render_template
from toollib.page import get_page


class EmailTestCases(TestCase):
    """test email

    """

    def test_send_email_not_use_thread(self):
        send_mail("subject_not_use_thread", "body_not_use_thread", ["hucj@funshion.com"], [], False)
        self.assertEquals(len(mail.outbox), 1)
        self.assertEquals(mail.outbox[0].subject, 'subject_not_use_thread')
        self.assertEquals(mail.outbox[0].body, 'body_not_use_thread')

    def test_send_email_use_thread(self):
        send_mail("subject_use_thread", "body_use_thread", ["hucj@funshion.com"], [], True)
        time.sleep(1)
        self.assertEquals(len(mail.outbox), 1)
        self.assertEquals(mail.outbox[0].subject, 'subject_use_thread')
        self.assertEquals(mail.outbox[0].body, 'body_use_thread')

    def test_send_html_template_email(self):
        send_html_template_email("template_subject_not_use_thread", 'email.html', {'username':'test'}, ["hucj@funshion.com"], [], False)
        self.assertEquals(len(mail.outbox), 1)
        self.assertEquals(mail.outbox[0].subject, 'template_subject_not_use_thread')
        self.assertEquals(mail.outbox[0].body, u'<html>\r\n<body>\r\nhello <strong>test</strong>\r\nyour account activated.\r\n</body>\r\n</html>')

    def test_send_html_template_email_use_thread(self):
        send_html_template_email("template_subject_use_thread", 'email.html', {'username':'test_use_thread'}, ["hucj@funshion.com"], [], True)
        time.sleep(1)
        self.assertEquals(len(mail.outbox), 1)
        self.assertEquals(mail.outbox[0].subject, 'template_subject_use_thread')
        self.assertEquals(mail.outbox[0].body, u'<html>\r\n<body>\r\nhello <strong>test_use_thread</strong>\r\nyour account activated.\r\n</body>\r\n</html>')

class RenderTestCases(TestCase):
    """test render

    """
    def test_render_json(self):
        pass
    
    def test_render_template(self):
        response = render_template('email.html', None, username = 'render_test')
        self.assertEquals(response.content, '<html>\r\n<body>\r\nhello <strong>render_test</strong>\r\nyour account activated.\r\n</body>\r\n</html>')
class PageTestCases(TestCase):
    """test render

    """
    def test_get_page_first(self):
        query_set = ['data1', 'data2', 'data3', 'data4']
        page = get_page(query_set, 1, 2)
        self.assertEqual(page.number, 1)
        self.assertEqual(page.start_index(), 1)
        self.assertEqual(page.end_index(), 2)
        self.assertEqual(page.object_list, ['data1', 'data2'])
        
    def test_get_page_last(self):
        query_set = ['data1', 'data2', 'data3', 'data4']
        page = get_page(query_set, 2, 2)
        self.assertEqual(page.number, 2)
        self.assertEqual(page.start_index(), 3)
        self.assertEqual(page.end_index(), 4)
        self.assertEqual(page.object_list, ['data3', 'data4'])

    def test_get_page_middile(self):
        query_set = ['data1', 'data2', 'data3', 'data4', 'data5', 'data6', 'data7']
        page = get_page(query_set, 2, 3)
        self.assertEqual(page.number, 2)
        self.assertEqual(page.start_index(), 4)
        self.assertEqual(page.end_index(), 6)
        self.assertEqual(page.object_list, ['data4', 'data5', 'data6'])

    def test_get_page_first_not_exact(self):
        query_set = ['data1', 'data2', 'data3', 'data4']
        page = get_page(query_set, 1, 3)
        self.assertEqual(page.number, 1)
        self.assertEqual(page.start_index(), 1)
        self.assertEqual(page.end_index(), 3)
        self.assertEqual(page.object_list, ['data1', 'data2', 'data3'])
        
    def test_get_page_last_not_exact(self):
        query_set = ['data1', 'data2', 'data3', 'data4']
        page = get_page(query_set, 2, 3)
        self.assertEqual(page.number, 2)
        self.assertEqual(page.start_index(), 4)
        self.assertEqual(page.end_index(), 4)
        self.assertEqual(page.object_list, ['data4'])
        
    def test_get_page_empty_data(self):
        query_set = []
        page = get_page(query_set, 2, 2)
        self.assertEqual(page.number, 1)
        self.assertEqual(page.start_index(), 0)
        self.assertEqual(page.end_index(), 0)
        self.assertEqual(page.object_list, [])
        
    def test_get_page_out_page(self):
        query_set = ['data1', 'data2', 'data3', 'data4']
        page = get_page(query_set, 3, 3)
        self.assertEqual(page.number, 1)
        self.assertEqual(page.start_index(), 1)
        self.assertEqual(page.end_index(), 3)
        self.assertEqual(page.object_list, ['data1', 'data2', 'data3'])