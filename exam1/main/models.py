from django.db import models

class Author(models.Model):
	name = models.CharField(max_length=20)
	last_name = models.CharField(max_length=20)
	birthday = models.DateField()
	
	def __unicode__(self):
	    	return 'Author: %s - %s' % (self.pk, self.last_name,)

class Article(models.Model):
	title = models.CharField(max_length=50)
	author = models.ForeignKey('Author')
	body = models.CharField(max_length=300)
	created_at = models.DateTimeField(auto_now_add=True)
	labels = models.ManyToManyField('Labels')

	def __unicode__(self):
			return 'Article: %s - %s' % (self.pk, self.title,)

class Comment(models.Model):
	article = models.ForeignKey('Article')
	name = models.CharField(max_length=25)
	text = models.CharField(max_length=60)
	created_at = models.DateTimeField(auto_now_add=True)

	def __unicode__(self):
			return 'Comment: %s - %s' % (self.pk, self.article,)

class Labels(models.Model):
	name = models.CharField(max_length=15)

	def __unicode__(self):
			return 'Labels: %s - %s' % (self.pk, self.name,)






