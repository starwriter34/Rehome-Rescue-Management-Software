from django.db import models

from .choices import States

# Create your models here.
class RescueInfo(models.Model):
	'''
	Rescue Information

		All the nessicary Information that can be displayed
	'''

	name = models.CharField(max_length=100, help_text='Name of your Rescue.', verbose_name='Rescue Name')

	display_poboxaddress = models.BooleanField(verbose_name='Display PO Box Address', help_text='Do you want the PO Box Address Shown on the Website?', default=True)
	display_regaddress = models.BooleanField(verbose_name='Display Regular Address', help_text='Do you want the Regular Address Shown on the Website?', default=True)

	pobox_number = models.CharField(max_length=100, help_text='', verbose_name='PO Box Number', null=True, blank=True)
	poboxcity = models.CharField(max_length=100, help_text='', verbose_name='PO Box City', null=True, blank=True)
	poboxstate = models.CharField(max_length=2, help_text='Use two letter State Abbreviation.',choices=States, verbose_name='PO Box State', null=True, blank=True)
	poboxzip = models.CharField(max_length=10, help_text='', verbose_name='PO Box Zip', null=True, blank=True)

	address1 = models.CharField(max_length=100, help_text='', verbose_name='Address 1', null=True, blank=True)
	address2 = models.CharField(max_length=100, help_text='', verbose_name='Address 2', null=True, blank=True)
	city = models.CharField(max_length=100, help_text='', verbose_name='City', null=True, blank=True)
	state = models.CharField(max_length=2, help_text='Use two letter State Abbreviation.',choices=States, verbose_name='State', null=True, blank=True)
	zipcode = models.CharField(max_length=10, help_text='', verbose_name='Zipcode', null=True, blank=True)

	nonprofit_ein = models.CharField(max_length=100, help_text='', verbose_name='Nonprofit EIN', null=True, blank=True)

	website = models.URLField(max_length=200, help_text='', verbose_name='Website Link', null=True, blank=True)
	email = models.CharField(max_length=100, help_text='', verbose_name='Rescue Email', null=True, blank=True)

	class Meta:
		verbose_name = 'Rescue Infomation'
		verbose_name_plural = 'Rescue Infomation'

	def __str__(self):
		return self.name

class SocialMedia(models.Model):
	'''
	The Rescues Social Media Accounts with Links
	'''
	name = models.CharField(max_length=100, help_text='Name of Social Media')
	url = models.URLField(max_length=200, help_text='Link to Social Media')

	class Meta:
		verbose_name = 'Social Media Links'
		verbose_name_plural = 'Social Media Links'

	def __str__(self):
		return self.name