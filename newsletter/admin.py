from django.contrib import admin

from .models import Newsletter, Subscriber, Issue, Subscription

admin.site.register(Newsletter)
admin.site.register(Subscriber)
admin.site.register(Issue)
admin.site.register(Subscription)

