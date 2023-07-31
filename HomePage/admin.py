from django.contrib import admin
from .models import Contact, AboutUs

# username: samundra
# email: aaerik534@gmail.com
# password: aaerik534

# Register your models here.
admin.site.site_header = "Everest momo | Admin"

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ['id','fname','email','subject','added_on','is_approved']

@admin.register(AboutUs)
class AboutAdmin(admin.ModelAdmin):
    list_display = ['title1','desc1','ceo_name']