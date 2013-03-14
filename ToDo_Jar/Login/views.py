from django.contrib import messages
from django.shortcuts import redirect
from django.views.generic import CreateView, ListView

from Login.forms import EntryForm, ProfileForm
from Login.models import Entry, Profile
from django.core.exceptions import PermissionDenied

class AddEntryView(CreateView):
    """Generic view for creating a new entry

    Django generic views are instantiated with a reference to the current 
    request (self.request).  We can use this to get hold of the currently 
    authenticated user and use that to tie the new entry to a User object
    """

    def form_valid(self, form):
        self.object = form.save(commit=False)
        try:
            self.object.author = self.request.user
            self.object.save()
            msg = "Your adventure, %s, has been posted"
            messages.add_message(self.request, messages.INFO, msg % self.object)
            return super(AddEntryView, self).form_valid(form)
        except:
            return redirect('/login/', no_login = True)

class ProfileView(CreateView):
    """Generic view for creating a new profile entry"""
    def form_valid(self, form):
        self.object = form.save(commit=False)
        try:
            self.object.username = self.request.user
            self.object.save()
            return super(ProfileView, self).form_valid(form)
        except:
            return redirect('/login/', no_login = True)

class EntryListView(ListView):
    def get_queryset(self):
        queryset = super(EntryListView, self).get_queryset()
        Group_Choices = ("All Users",)
        for i in range(1,100):
            try:
                choices = Profile.objects.get(pk=i).groups
                Group_Choices = Group_Choices + choices
            except: 
                choices = choices
        queryset = queryset.filter(entry_groups__icontains= 'group1')
        return queryset
