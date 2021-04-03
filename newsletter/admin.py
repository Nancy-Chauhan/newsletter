from django.contrib import admin

from .models import Newsletter, Subscriber, Issue, Subscription

admin.site.register(Issue)
admin.site.register(Subscription)


class IssueAdmin(admin.StackedInline):
    model = Issue
    pass


class SubscriptionAdmin(admin.StackedInline):
    model = Subscription
    pass


@admin.register(Newsletter)
class NewsletterAdmin(admin.ModelAdmin):
    inlines = (IssueAdmin, SubscriptionAdmin)


@admin.register(Subscriber)
class SubscriberAdmin(admin.ModelAdmin):
    inlines = (SubscriptionAdmin,)
