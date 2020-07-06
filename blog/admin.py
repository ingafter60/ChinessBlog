from django.contrib import admin
from blog.models import Category, Tag, Post

# Register your models here.

class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'created_time', 'modified_time', 'category', 'author']
    fields = ['title', 'body', 'excerpt', 'category', 'tags']

    """
	Postadmin inherits from ModelAdmin, it has a save_model method, 
	this method has only one line of code: obj.save(). 
	Its role is to save the model instance associated with this Modeladmin 
	(here the Modeladmin is registered with Post) to the database. 
	This method receives four parameters, the first two of which 
	are request, which is the HTTP request object, and the second is obj, 
	which is the instance of the associated object created this time, 
	so by rewriting this method, you can request .user is associated 
	with the created Post instance, and then save the Post data to the 
	database:
    """
    def save_model(self, request, obj, form, change):
        obj.author = request.user
        super().save_model(request, obj, form, change)


admin.site.register(Category)
admin.site.register(Tag)
admin.site.register(Post, PostAdmin)
