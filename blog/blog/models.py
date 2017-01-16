from django.db import models
from django.urls import reverse
from django.utils import timezone
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.mail import send_mail


class Blog(models.Model):
    author = models.OneToOneField('auth.User', related_name="author")
    subscriber = models.ManyToManyField('auth.User', related_name="subscribers", blank=True, null=True)

    def __str__(self):
        return self.author.username


class Post(models.Model):
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE, related_name='blog')
    title = models.CharField(max_length=255)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    seen = models.BooleanField(default=False)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('detail_post', kwargs={'pk': self.pk})


@receiver(post_save, sender=Post, dispatch_uid="post_created")
def send_email(sender, instance, created, **kwargs):
    subscribers = Blog.objects.get(author=instance.blog.author).subscriber.all()
    senders_emails = []
    for s in subscribers:
        senders_emails.append(s.email)
    extract_sub = ", ".join(str(x) for x in senders_emails)
    sender = instance.blog.author.email
    send_mail("Your Subject", "This is a simple text email body.",
              "your email <{0}>".format(extract_sub), ["{0}".format(sender)])

