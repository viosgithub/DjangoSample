from django.conf.urls.defaults import *
from chapter3.views import *

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    ("^time/$",current_datetime),
    (r"^time/plus/(\d{1,2})/$",hours_ahead),
    ("\hello/$",hello),
    # Example:
    # (r'^showDate/', include('showDate.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # (r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # (r'^admin/', include(admin.site.urls)),
)
