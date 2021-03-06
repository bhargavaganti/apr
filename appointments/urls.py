from django.conf.urls import url
from django.contrib.auth.decorators import login_required

from appointments.ajax import venue_event_feed, printable_event_feed, calendar_event_feed
from appointments.ajax import process_add_client_form, process_select_client_form, process_add_event_form
from appointments.ajax import process_edit_client_form, edit_event, add_event, process_edit_event_form, delete_appointment
from appointments.ajax import edit_appointment_status, process_generic_event_form, process_edit_generic_event_form
from appointments.views import AddEventView, AppointmentView, AppointmentDelete, AddAppointmentSnippetView
from appointments.views import AppointmentEdit, AppointmentDatatableView, AppointmentSnippetView
from appointments.views import TagAdd, TagUpdate, TagDatatableView, TagDelete
from venues.views import VenueCalendarView


urlpatterns = [
    # ajax
    url(r'^feed/venue/(?P<pk>\d+)/$', venue_event_feed, name='venue_event_feed'),
    url(r'^printable-feed/$', login_required(printable_event_feed), name='printable_event_feed'),
    url(r'^calendar-feed/$', login_required(calendar_event_feed), name='calendar_event_feed'),
    url(r'^add-client-form/$', login_required(process_add_client_form), name='process_add_client_form'),
    url(r'^edit-client-form/(?P<pk>\d+)/$', login_required(process_edit_client_form), name='process_edit_client_form'),
    url(r'^select-client-form/$', login_required(process_select_client_form), name='process_select_client_form'),
    url(r'^add-event-form/$', login_required(process_add_event_form), name='process_add_event_form'),
    url(r'^generic-event-form/$', login_required(process_generic_event_form), name='process_generic_event_form'),
    url(r'^edit-generic-event-form/$', login_required(process_edit_generic_event_form), name='process_edit_generic_event_form'),
    # regular
    url(r'^add/', login_required(AddEventView.as_view()), name='add'),
    # url(r'^appointments/$', login_required(AppointmentListView.as_view()), name='appointments'),
    url(r'^appointments/$', login_required(AppointmentDatatableView.as_view()), name='appointments'),
    url(r'^view/(?P<pk>\d+)/$', login_required(AppointmentView.as_view()), name='appointment'),
    url(r'^edit/(?P<pk>\d+)/$', login_required(AppointmentEdit.as_view()), name='appointment_edit'),
    url(r'^delete/(?P<pk>\d+)/$', login_required(AppointmentDelete.as_view()), name='appointment_delete'),
    url(r'^schedule/(?P<pk>\d+)/$', login_required(VenueCalendarView.as_view()), name='venue'),
    # edit
    url(r'^add-event/$', login_required(add_event), name='add_event'),
    url(r'^edit-event/(?P<pk>\d+)/$', login_required(edit_event), name='edit_event'),
    url(r'^delete-appointment-form/(?P<pk>\d+)/$', login_required(delete_appointment), name='delete_appointment'),
    url(r'^edit-appointment-status/(?P<pk>\d+)/$', login_required(edit_appointment_status), name='edit_appointment_status'),
    url(r'^edit-event-form/(?P<pk>\d+)/$', login_required(process_edit_event_form), name='process_edit_event_form'),
    url(r'^snippet/(?P<pk>\d+)/$', login_required(AppointmentSnippetView.as_view()), name='appointment_snippet'),
    url(r'^client-snippet/$', login_required(AddAppointmentSnippetView.as_view()), name='appointment_client_snippet'),
    # tags
    url(r'^tags/$', login_required(TagDatatableView.as_view()), name='tag_list'),
    url(r'^tags/add/$', login_required(TagAdd.as_view()), name='tag_add'),
    url(r'^tags/edit/(?P<pk>\d+)/$', login_required(TagUpdate.as_view()), name='tag_edit'),
    url(r'^tags/delete/(?P<pk>\d+)/$', login_required(TagDelete.as_view()), name='tag_delete'),
]
