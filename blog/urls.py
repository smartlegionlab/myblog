# -*- coding: utf-8 -*-
# --------------------------------------------------------
# Licensed under the terms of the BSD 3-Clause License
# (see LICENSE for details).
# Copyright © 2018-2021, A.A Suvorov
# All rights reserved.
# --------------------------------------------------------
# https://github.com/smartlegionlab
# smartlegiondev@gmail.com
# --------------------------------------------------------
from django.urls import path
from django.contrib.sitemaps.views import sitemap
from blog.sitemaps import PostSiteMap

from . import views
from .feeds import LatestPostFeed

sitemaps = {'posts': PostSiteMap, }

app_name = 'blog'
urlpatterns = [
    path('search/', views.post_search, name='post_search'),
    path('sitemap.xml', sitemap, {'sitemaps': sitemaps}, name='django.contrib.sitemaps.views.sitemap'),
    path('feed/', LatestPostFeed(), name='post_feed'),
    path('tag/<slug:tag_slug>/', views.post_list, name='post_list_by_tag'),
    path('<int:post_id>/share/', views.post_share, name='post_share'),
    path('<int:year>/<int:month>/<int:day>/<slug:post>/', views.post_detail, name='post_detail'),
    path('', views.post_list, name='post_list'),
]
