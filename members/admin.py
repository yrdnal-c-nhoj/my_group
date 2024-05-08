from django.contrib import admin
from .models import Member

""" Set list_display

We can control the fields to display by specifying them 
in a list_display property in the admin.py file.

First create a MemberAdmin() class and specify the list_display tuple: 

 

Remember to add the MemberAdmin as an argumet in the 
admin.site.register(Member, MemberAdmin)."""

class MemberAdmin(admin.ModelAdmin):
  list_display = ("firstname", "lastname", "joined_date", "phone")
admin.site.register(Member, MemberAdmin)