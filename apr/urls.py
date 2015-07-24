from django.conf import settings
from django.conf.urls import include, url
from django.contrib import admin
from django.contrib.auth.decorators import login_required

from apr.views import HomeView, DashboardView, CustomerRedirect, DayView, PricingView
from apr.views import SupportView
from appointments.views import AppointmentClientConfirm, AppointmentClientCancel
from customers.views import NewCustomer

urlpatterns = [
    url(r'^$', HomeView.as_view(), name='home'),
    url(r'^pricing/$', PricingView.as_view(), name='pricing'),
    url(r'^support/$', SupportView.as_view(), name='support'),
    url(r'^help/$', SupportView.as_view(template_name="core/help.html"), name='help'),
    url(r'^dashboard/$', login_required(DashboardView.as_view()), name='dashboard'),
    url(r'^day/$', login_required(DayView.as_view()), name='day'),
    url(r'^new/$', login_required(NewCustomer.as_view()), name='new_customer'),
    url(r'^appointments/', include('appointments.urls', namespace='appointments')),
    url(r'^users/', include('users.urls', namespace='users')),
    url(r'^schedules/', include('venues.urls', namespace='venues')),
    url(r'^customer/', include('customers.urls', namespace='customer')),

    url(r'^admin/', include(admin.site.urls)),

    # third party
    url(r'^select2/', include('django_select2.urls')),
    url(r'^accounts/', include('allauth.urls')),

    # utils
    url(r'^customer-redirector/$', CustomerRedirect.as_view(), name='customer_redirect'),

    # client actions
    url(r'^confirm/(?P<slug>[\w-]+)/$', AppointmentClientConfirm.as_view(), name='confirm_appointment'),
    url(r'^cancel/(?P<slug>[\w-]+)/$', AppointmentClientCancel.as_view(), name='cancel_appointment'),

    # flat pages
    url(r'^$', include('django.contrib.flatpages.urls')),
]

if settings.DEBUG:
    # static files (images, css, javascript, etc.)
    urlpatterns += [
        url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT})
    ]
