from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    # Examples:
    # url(r'^$', 'demo.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^report/$', 'todoApp.views.status'),
    url(r'^admin/', include(admin.site.urls)),
]
