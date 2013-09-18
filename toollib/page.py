# -*- coding: UTF-8 -*-
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

def get_page(query_set, page_no, page_size):
    paginator = Paginator(query_set, page_size) 
    try:
        page = paginator.page(page_no)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        page = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver first page.
        page = paginator.page(1)
    return page