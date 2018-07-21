from django.conf.urls import include, url

from django.contrib import admin
admin.autodiscover()

from django.contrib.auth.views import login
from django.contrib.auth.views import logout

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^accounts/login/$', login, name='login'),
    url(r'^accounts/logout/$', logout, {'next_page': '/'}, name='logout'),
    url(r'', include('blog.urls')),
]