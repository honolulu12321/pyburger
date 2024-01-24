from django.contrib import admin
from burgers.models import burger

# Register your models here.
# 기초문법 정리, 함수 데코레이터


@admin.register(burger)
class BurgerAdmin(admin.ModelAdmin):
    pass