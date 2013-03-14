from django.db import models
from django.conf import settings
from django.contrib.auth.models import User, Group
from django.utils import timezone

Form_Choices = (('Choose Me', 'Choose Me'),('Crazy','Crazy'),('Middle','Middle'),('Low Key','Low Key'), )
# -----------------------------------------#

class Profile(models.Model):
	first_name = models.CharField(max_length=20)
	groups = models.CharField(max_length = 20)
	location = models.CharField(max_length=20)
	username = models.ForeignKey(User, null=True)

	class Meta:
		ordering = ['first_name', ]
		verbose_name_plural = "profiles"

	def __unicode__(self):
		return self.username

# -----------------------------------------#

class Entry(models.Model):
	title = models.CharField(max_length=128)
	location = models.CharField(max_length=128)
	links = models.URLField()
	level = models.CharField(max_length=10, choices = Form_Choices, default='Choose Me')
	description = models.TextField()
	private = models.BooleanField(default=False)
	author = models.ForeignKey(User, null=True)
	pub_date = models.DateTimeField()
	entry_groups = models.TextField(blank=True)

	class Meta:
		ordering = ['pub_date', ]
		verbose_name_plural = "entries"

	def __unicode__(self):
		return self.title

	def save(self):
		if not self.pk:
            # this object is new, set pub_date
			self.pub_date = timezone.now()
		super(Entry, self).save()

	def split_groups(self):
		lister = self.entry_groups.strip('[').strip(']').split(',')
		outlist = []
		for i in lister:
			outlist.append(i.split("'")[1])
		return outlist

# -----------------------------------------#
