from django.db import models
from mptt.models import MPTTModel, TreeForeignKey
from django.contrib.auth.models import User
from tinymce import models as tinymce_models
from slugify import slugify
from tagging.fields import TagField
from tagging.models import Tag
from django.conf import settings

# Create your models here.

STATUS_CHOICES = (
    ('active', 'active'),
    ('inactive', 'inactive'),
    ('draft', 'draft'),
    ('deleted', 'deleted'),
 )

if 'south' in settings.INSTALLED_APPS:
    from south.modelsinspector import add_introspection_rules
    add_introspection_rules([], ["^tinymce\.models.\HTMLField"])

class Category(MPTTModel):
    title = models.CharField(max_length = 100)
    parent = TreeForeignKey('self', null = True, blank = True, related_name = 'children')

    class MPTTMeta:
        order_insertion_by = ['title']

    def __unicode__(self):
        return self.title

    def slug(self):
        return slugify(self.title)

class Post(models.Model):
    title = models.CharField(max_length = 200)
    content = tinymce_models.HTMLField()
    category = models.ManyToManyField(Category)
    author = models.ForeignKey(User)
    date_add = models.DateTimeField(auto_now_add = True)
    date_edit = models.DateTimeField(auto_now = True)
    status = models.CharField(max_length = 15, choices = STATUS_CHOICES, default = 'active', db_index = True)
    source = models.URLField(blank = True, null = True)
    tags = TagField()

    class Meta:
        ordering = ['pk']

    def __unicode__(self):
        return self.title

    def slug(self):
        return slugify(self.title)

class PostImage(models.Model):
    post = models.ForeignKey(Post)
    date_add = models.DateTimeField(auto_now_add = True)
#    file_name = models.FileField()
