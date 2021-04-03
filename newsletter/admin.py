from django.contrib import admin

from . import tasks
from .models import Newsletter, Subscriber, Issue, Subscription

admin.site.register(Subscription)


def send(modeladmin, request, queryset):
    for issue in queryset:
        tasks.send_issue.delay(issue.id)


send.short_description = "send"


class IssueInline(admin.StackedInline):
    model = Issue


@admin.register(Issue)
class IssueAdmin(admin.ModelAdmin):
    actions = [send]


class SubscriptionAdmin(admin.StackedInline):
    model = Subscription
    pass


@admin.register(Newsletter)
class NewsletterAdmin(admin.ModelAdmin):
    inlines = (IssueInline, SubscriptionAdmin)


@admin.register(Subscriber)
class SubscriberAdmin(admin.ModelAdmin):
    inlines = (SubscriptionAdmin,)
