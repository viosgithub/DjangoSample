from django.conf.urls.defaults import *
from django.contrib.auth.views import login,logout

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Example:
    # (r'^chapter14_2/', include('chapter14_2.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # (r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # (r'^admin/', include(admin.site.urls)),
    (r"^accounts/login/$",login),
    (r"^accounts/logout/$",logout),
)
