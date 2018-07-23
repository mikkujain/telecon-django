from django.db import models

# Create your models here.
class Pages(models.Model):

	tite 		= models.CharField(max_length=150, blank=False)
	description	= models.TextField(blank=True, null=False )
	price		= models.DecimalField(decimal_places=2, max_digits=1000)
	summary		= models.TextField()

	def __str__(self):
		return self.tite + "-" + self.summary