from django.conf.urls import url


urlpatterns = [
    url(r'^$', 'blog.views.index', name='index'),
    url(r'^category/(?P<pk>\d+)/$', 'blog.views.category_detail', name='category_detail'),
    url(r'^(?P<pk>\d+)/$', 'blog.views.shop_detail', name='shop_detail'),
    url(r'^(?P<shop_pk>\d+)/reviews/new/$', 'blog.views.review_new', name='review_new'),
    url(r'^(?P<shop_pk>\d+)/reviews/(?P<pk>\d+)/edit/$', 'blog.views.review_edit', name='review_edit'),
    url(r'^newcategory/$', 'blog.views.category_new', name='category_new'),
    url(r'^newshop/$', 'blog.views.shop_new', name='shop_new'),


]
