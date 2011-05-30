from django.conf.urls.defaults import *
from chapter7.books import views

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Example:
    # (r'^chapter5/', include('chapter5.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # (r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    (r'^admin/', include(admin.site.urls)),
    (r"^hello/$","chapter7.views.hello"),
    (r"^url/$","chapter7.views.currentUrlView"),
    (r"^agent/$","chapter7.views.uaDisplay2"),
    (r"^meta/$","chapter7.views.displayMeta"),
    (r"^search-form/$",views.searchForm),
    (r"^search/$",views.search),
    (r"^contact/$","chapter7.contact.views.contact"),
)
