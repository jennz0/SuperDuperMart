from django.db import models
from django.urls import reverse

class Order(models.Model):
    user = models.ForeignKey("accounts.CustomUser", on_delete=models.CASCADE)
    order_status = models.CharField(max_length=100)
    date_placed = models.DateTimeField()

class Product(models.Model):
    name = models.CharField(max_length=300)
    description = models.TextField()
    retail_price = models.DecimalField(max_digits=7, decimal_places=2)
    wholesale_price = models.DecimalField(max_digits=7, decimal_places=2)
    quantity = models.IntegerField()

class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    purchased_price = models.DecimalField(max_digits=7, decimal_places=2)
    wholesale_price = models.DecimalField(max_digits=7, decimal_places=2)
    quantity = models.IntegerField()

class WatchList(models.Model):
    user = models.ForeignKey("accounts.CustomUser", on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)

# class Post(models.Model):
#     title = models.CharField(max_length=200)
#     author = models.ForeignKey("accounts.CustomUser", on_delete=models.CASCADE)
#     content = models.TextField()
#
#     def __str__(self):
#         return self.title
#
#     def get_absolute_url(self):
#         return reverse("post_detail", kwargs={"pk": self.pk})
#
#
# class Comment(models.Model):
#     post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="comments")  # default related_name is FOO_set
#     author = models.ForeignKey("accounts.CustomUser", on_delete=models.CASCADE)
#     content = models.TextField()
#
#     def __str__(self):
#         return self.content
#
#     def get_absolute_url(self):
#         return reverse("post_detail", kwargs={"pk": self.post.pk})
