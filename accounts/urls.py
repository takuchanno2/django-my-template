from django.conf.urls import patterns, include, url
from django.contrib import admin
from accounts.views import LoginView, LogoutView
from django.core.urlresolvers import reverse_lazy

admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'loginform.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^login/$', LoginView.as_view(), name="accounts/login"),
    url(r'^logout/$', LogoutView.as_view(), { "next_page": reverse_lazy("top") }, name="accounts/logout"),
)

