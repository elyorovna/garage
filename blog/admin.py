from django.contrib import admin

from blog.models import Categories, Cars, Joylashish, Email, Contact

# Register your models here.
admin.site.register(Categories)
admin.site.register(Cars)
admin.site.register(Joylashish)
admin.site.register(Email)
admin.site.register(Contact)