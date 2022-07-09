from django.contrib import admin
from .models import UserProfileinfo, Feedback

# Register your models here.

admin.site.register(UserProfileinfo)

class FeedbackAdmin(admin.ModelAdmin):
    list_display = ( 'name', 'date', 'happy',)
    list_filter = ('date',)
    search_fields = ('details',)

    class Meta:
        model = Feedback


admin.site.register(Feedback, FeedbackAdmin)