from django.contrib import admin
from .models import Subject, Course, Module

@admin.register(Subject)
class SubjectAdmin(admin.ModelAdmin):
    list_display = ['title', 'slug']
    prepopulated_fields = {'slug': ('title',)}


class ModuleInline(admin.StackedInline):
    model = Module
    extra = 0  # optional, removes extra empty forms


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ['title', 'subject', 'created']
    list_filter = ['created', 'subject']
    search_fields = ['title', 'overview']
    prepopulated_fields = {'slug': ('title',)}
    inlines = [ModuleInline]


from django.contrib import admin
from django.urls import path
from django.shortcuts import render
import memcache

mc = memcache.Client(['127.0.0.1:11211'])

# Dummy model just for the admin menu
from django.db import models
class DummyMemcache(models.Model):
    class Meta:
        managed = False
        verbose_name = "Memcached Stats"
        verbose_name_plural = "Memcached Stats"

@admin.register(DummyMemcache)
class MemcacheAdmin(admin.ModelAdmin):
    change_list_template = "memcache_stats.html"

    def changelist_view(self, request, extra_context=None):
        stats = mc.get_stats()
        context = {
            **(extra_context or {}),
            'memcache_stats': stats,
        }
        return super().changelist_view(request, extra_context=context)
