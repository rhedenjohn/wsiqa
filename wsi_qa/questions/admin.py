from django.contrib import admin
from . models import Questions, Choice, Process, Category, Area, Skill, Difficulty
# Register your models here.
admin.site.register(Questions)
admin.site.register(Choice)
admin.site.register(Process)
admin.site.register(Category)
admin.site.register(Area)
admin.site.register(Skill)
admin.site.register(Difficulty)
