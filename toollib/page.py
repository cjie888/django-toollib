# -*- coding: UTF-8 -*-
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

class ExtensionPaginator(Paginator):
    def __init__(self, object_list, per_page, range_num=4, orphans=0, allow_empty_first_page=True):
        Paginator.__init__(self, object_list, per_page, orphans, allow_empty_first_page)
        self.range_num = range_num

    def page(self, number):
        self.page_num = number
        return super(ExtensionPaginator, self).page(number)

    def _page_range_extension(self):
        num_count = 2 * self.range_num + 1
        if self.num_pages <= num_count:
            return range(1, self.num_pages + 1)
        num_list = []
        self.page_num = int(self.page_num)
        num_list.append(self.page_num)

        for i in range(1, self.range_num + 1):
            if self.page_num - i <= 0:
                num_list.append(num_count + self.page_num - i)
            else:
                num_list.append(self.page_num - i)
            if self.page_num + i <= self.num_pages:
                num_list.append(self.page_num + i)
            else:
                num_list.append(self.page_num + i - num_count)

        num_list.sort()
        return num_list
    page_range_extension = property(_page_range_extension)

def get_page(query_set, page_no, page_size):
    paginator = ExtensionPaginator(query_set, page_size) 
    try:
        page = paginator.page(page_no)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        page = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver first page.
        page = paginator.page(1)
    return page