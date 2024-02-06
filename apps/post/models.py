from django.db import models
from django.urls import reverse


class Post(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey("accounts.CustomUser", on_delete=models.CASCADE)
    content = models.TextField()

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("post_detail", kwargs={"pk": self.pk})


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="comments")  # default related_name is FOO_set
    author = models.ForeignKey("accounts.CustomUser", on_delete=models.CASCADE)
    content = models.TextField()

    def __str__(self):
        return self.content

    def get_absolute_url(self):
        return reverse("post_detail", kwargs={"pk": self.post.pk})
