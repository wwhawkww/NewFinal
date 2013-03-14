from django import forms
from Login.models import Entry, Profile
from django.contrib.auth.models import User

# -----------------------------------------#

class EntryForm(forms.ModelForm):

    Group_Choices = (("All Users","All Users"),)
    for i in range(1,100):
        try:
            choices = Profile.objects.get(pk=i).groups
            Group_Choices = Group_Choices + ((choices.lower(),choices),)
        except: 
            choices = ""
            Group_Choices = Group_Choices + ((choices.lower(),choices),)
            break
    entry_groups = forms.MultipleChoiceField(choices = Group_Choices)

    class Meta:
        model = Entry
        fields = ('title', 'links', 'location','entry_groups', 'level','description', 'private',)
        	
# -----------------------------------------#

class ProfileForm(forms.ModelForm):
    """allow entry profile data"""

    class Meta:
        model = Profile
        fields = ('first_name', 'groups', 'location', )