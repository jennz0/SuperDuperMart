from django.contrib import admin
# from .models import Post, Comment
#
#
# class CommentInline(admin.TabularInline):
#     model = Comment
#     extra = 0  # default is 3
#
#
# class PostAdmin(admin.ModelAdmin):
#     inlines = [CommentInline]
#
#
# admin.site.register(Post, PostAdmin)
# admin.site.register(Comment)

from apps.shop.models import Product, Order, OrderItem, WatchList

admin.site.register(Product)
admin.site.register(Order)
admin.site.register(OrderItem)
admin.site.register(WatchList)


