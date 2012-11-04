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
# from django.views.generic.list_detail import object_list
from django.utils import translation
from django.contrib.auth.models import User

from django.core.paginator import Paginator, InvalidPage, EmptyPage
from dantyan.decorators import render_to
from models import Post, Category
from . forms import BlogEditForm

# import the logging library
import logging

# Get an instance of a logger
logger = logging.getLogger(__name__)

# from  import forms
# from . import models

@render_to('blog/home.html')
def home(request):

    data = {
        'posts':Post.objects.all(),
        'nodes':Category.objects.all(),
    }
    return data

@render_to('blog/category.html')
def category(request, id, slug = None):

    id = int(id)

    try:
        category = Category.objects.get(pk = id)
    except Category.DoesNotExist:
        raise Http404

    if category.slug() != slug:
        return redirect('blog-category', id = id, slug = category.slug(), permanent = True)

    data = {
        'category':category,
        'posts':Post.objects.filter(category = id)[:10],
        'nodes':Category.objects.all(),
    }
    return data


@render_to('blog/post.html')
def post(request, id, slug = None):
    id = int(id)

    try:
        post = Post.objects.get(pk = id)
    except Post.DoesNotExist:
        raise Http404

    if post.slug() != slug:
        return redirect('blog-post', id = id, slug = post.slug(), permanent = True)

    data = {
        'post':post,
        'nodes':Category.objects.all(),
    }

    return data

@login_required
def add(request):

    if request.session.get('blog-draft-id', '') and int(request.session['blog-draft-id']) > 0:
        return redirect('blog-edit', id = request.session['blog-draft-id'])
    else:
        post = Post(status = 'draft', author = User.objects.get(pk = request.user.id))
        post.save()
        request.session['blog-draft-id'] = post.id
        return redirect('blog-edit', id = post.id)


@login_required
@render_to('blog/edit.html')
def edit(request, id):

    id = int(id)

    try:
        post = Post.objects.get(pk = id)
    except Post.DoesNotExist:
        raise Http404

	form = BlogEditForm(request.POST or None, instance = post)
	print form
	assert False

# 	if form.is_valid():
# 		form.save()
# 		post.status = 'active'
# 		post.save()
#
# 		if request.session['blog-draft-id']:
# 			del request.session['blog-draft-id']

    data = {
        'form':form
    }

    return data

# @render_to('blog/category.html')
# def cat(request):
#    data = {
#        'posts':Post.objects.all(),
#        'nodes':Category.objects.all(),
#    }
#    return data
