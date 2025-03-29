from django.contrib import admin
from .models import Course

@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display=["title","instructor","created_at","updated_at"]
    search_fields=["title","instructor__username"]
    list_filter=["created_at","updated_at","instructor"]

# What all things :
#list_display :what viewing when we display courses
#seacrhing field  : __username --reference of insturctor name search -FK



#createSuperUser --- createsuperuser
#runserver