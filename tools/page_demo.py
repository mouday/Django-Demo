# -*- coding: utf-8 -*-
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

book_list = ["语文", "数学", "英语", "生物", "音乐", "体育", "美术"]

paginator = Paginator(book_list, 2)  # 实例化出一个对象

# 属性
print("count:", paginator.count)  # 数据总数 7
print("num_pages", paginator.num_pages)  # 总页数 4 = 7/2
print("page_range", paginator.page_range)  # 页码的列表 range(1, 5) = 1, 2, 3, 4

# 方法
page1 = paginator.page(1)  # 第1页的page对象
for i in page1:  # 遍历第1页的所有数据对象 语文 数学
    print(i)

print(page1.object_list)  # 第1页的所有数据  ['语文', '数学']

print(page1.has_next())  # 是否有下一页 True
print(page1.next_page_number())  # 下一页的页码 2
print(page1.has_previous())  # 是否有上一页  False
# print(page1.previous_page_number())  # 上一页的页码  EmptyPage

# 异常
page12 = paginator.get_page(12)  # 超过最大值不会报错，取最大页码
print(page12)
# <Page 4 of 4>

# page = paginator.page(12)  # error:EmptyPage


pagez = paginator.get_page("z")  # 传递非整数不会报错，取最小页码 第一页
print(pagez)
# <Page 1 of 4>

# page=paginator.page("z")   # error:PageNotAnInteger
