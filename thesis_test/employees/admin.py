from django.contrib import admin

from .models import Employee, Department


@admin.register(Department)
class TargetAdmin(admin.ModelAdmin):
    list_display = ('uid', 'name', )
    fields = ('uid', 'name', )
    search_fields = ('name', )
    readonly_fields = ('uid', )


@admin.register(Employee)
class TargetAdmin(admin.ModelAdmin):
    list_display = ('uid', 'name', )
    fields = ('uid', 'name', 'surname', 'patronymic', 'position', 'salary', 'age', 'department', 'photo', )
    search_fields = ('uid', 'name', 'surname', 'patronymic', 'position', 'department', )
    readonly_fields = ('uid', )