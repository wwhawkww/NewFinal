from django.conf.urls import patterns, url,include
from django.views.generic import ListView, DetailView

from Login.models import Entry, Profile
from Login.forms import EntryForm, ProfileForm
from Login.views import AddEntryView, ProfileView, EntryListView
from registration.views import register
from django.contrib.auth.models import User

urlpatterns = patterns('',
    # List view for all posts:
    url(r'^$',
        ListView.as_view(
            queryset=Entry.objects.all(),
            context_object_name="entries",
            template_name="Login/entry_list.html"
        ),
        name="entry_list"),
    url(r'^add/$',
        AddEntryView.as_view(
            model=Entry,
            form_class=EntryForm,
            template_name="Login/entry_form.html",
            success_url="/added_entry/",
        ),
        name="add_entry"),
        
    url(r'^added_entry/$',
        EntryListView.as_view(
            queryset=Entry.objects.all(),
            context_object_name="entries",
            template_name="Login/added_entry.html",
        ),
        name="added_entry"),
        
    url(r'^success/$',
    	ListView.as_view(
    		queryset=Entry.objects.all(),
            context_object_name="entries",
            template_name="registration/registration_complete.html",
        ),
        name = "register_success"),

    url(r'^profile/$',
        ProfileView.as_view(
            model=Profile,
            form_class=ProfileForm,
            template_name="Login/profile_form.html",
            success_url="/view_profile/",
        ),
        name="profile"),

    url(r'^view_profile/$',
        ListView.as_view(
            queryset=Profile.objects.all(),
            context_object_name="profiles",
            template_name="registration/view_profile.html",
        ),
        name = "view_profile"),
)