import math

from django.utils.safestring import mark_safe


class Pagination(object):
    def __init__(self, request, data_list, search='id', page_size=3, params="index", sub=2):
        self.page_index = int(request.GET.get(params, 1) if request.GET.get(params, 1) != '' else 1)
        search_txt = request.GET.get(search)
        self.search = search
        self.search_query = search_txt if search_txt is not None else ''
        self.page_size = page_size
        self.total_page_nums = math.ceil(data_list.count() / page_size)
        self.page_index = self.page_index if 0 < self.page_index <= self.total_page_nums else 1
        self.params = params
        self.data_start = (self.page_index - 1) * page_size
        self.data_end = self.page_index * page_size
        self.number_list = data_list[self.data_start: self.data_end]

        self.sub = sub
        self.page_list = []
        import copy

        query_dict = request.GET
        query_dict._mutable = True
        self.query_dict = query_dict
        self.html()

    def html(self):
        self.query_dict.setlist(self.params, [1])
        # print(self.query_dict.urlencode())
        self.query_dict.setlist(self.search, [self.search_query])
        first = max(self.page_index - self.sub, 1)
        self.page_list.append('<li class=""><a href="?{}" aria-label="Previous">'
                              '<span aria-hidden="true">First</span></a></li>'.format(self.query_dict.urlencode()))
        if self.page_index <= 1:
            self.page_list.append('<li class="disabled"><a href="?{}" aria-label="Previous">'
                                  '<span aria-hidden="true">«</span></a></li>'.format(self.query_dict.urlencode()))
        else:
            self.query_dict.setlist(self.params, [self.page_index - 1])
            self.page_list.append('<li class=""><a href="?{}" aria-label="Previous">'
                                  '<span aria-hidden="true">«</span></a></li>'.format(self.query_dict.urlencode()))
        end = min(self.page_index + self.sub, self.total_page_nums)
        for i in range(first, end + 1):
            self.query_dict.setlist(self.params, [i])
            if i == self.page_index:
                self.page_list.append(
                    '<li class=active><a href="?{}">{}</a></li>'.format(self.query_dict.urlencode(), i))
            else:
                self.page_list.append(
                    '<li><a href="?{}">{}</a></li>'.format(self.query_dict.urlencode(), i))
        if self.page_index >= self.total_page_nums:
            self.query_dict.setlist(self.params, [self.total_page_nums])
            self.page_list.append('<li class="disabled"><a href="?{}" aria-label="Next">'
                                  '<span aria-hidden="true">»</span></a></li>'.format(self.query_dict.urlencode()))
        else:
            self.query_dict.setlist(self.params, [self.page_index + 1])
            self.page_list.append('<li class=""><a href="?{}" aria-label="Next">'
                                  '<span aria-hidden="true">»</span></a></li>'.format(self.query_dict.urlencode()))
        self.query_dict.setlist(self.params, [self.total_page_nums])
        self.page_list.append('<li class=""><a href="?{}" aria-label="Previous">'
                              '<span aria-hidden="true">End</span></a></li>'.format(self.query_dict.urlencode()))
        self.page_list.append("""
                    <form method="get">
                    <div class="input-group" style="width: 200px">
                        <input type="text" name="index" class="form-control" placeholder="page number">
                        <span class="input-group-btn">
                        <button class="btn btn-default" type="submit">jump</button>
                    </span>
                    </div>
                </form>
                """)
        self.page_list = mark_safe("".join(self.page_list))
