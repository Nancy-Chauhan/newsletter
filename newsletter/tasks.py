from celery import shared_task

from newsletter.models import Issue, Subscription


@shared_task()
def send_issue(issue_id):
    issue = Issue.objects.get(pk=issue_id)
    for subscription in Subscription.objects.filter(newsletter=issue.newsletter):
        print("sending issue to", issue_id, subscription.subscriber.email, issue.title, issue.content)
