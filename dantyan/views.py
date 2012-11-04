# -*- coding: utf-8 -*-
from django.shortcuts import render_to_response
from django.http import HttpResponse

from django.conf import settings
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import ObjectDoesNotExist
from django.http import Http404, HttpResponseRedirect
from django.shortcuts import redirect
from django.utils.translation import ugettext_lazy as _
#from django.views.generic.list_detail import object_list
from django.utils import translation

from decorators import render_to

#from .import forms
#from .import models

@render_to('welcome/home.html')
def home(request):
    data = {}
    return data
