from django.contrib import admin
from MyTodo_App.models import Status, TodoList
import datetime
from django.utils import timezone
from django.contrib.admin.filters import DateFieldListFilter
from django.utils.translation import gettext_lazy as _
import csv
from django.http import HttpResponse



class MyDateTimeFilter(DateFieldListFilter):
    ''' This class is for adding extra date filter of Next 7 days in admin'''

    def __init__(self, *args, **kwargs):
        super(MyDateTimeFilter, self).__init__(*args, **kwargs)

        now = timezone.now()
        if timezone.is_aware(now):
            now = timezone.localtime(now)

        today = now.date()

        self.links += ((
            (_('Next 7 days'), {
                self.lookup_kwarg_since: str(today),
                self.lookup_kwarg_until: str(today + datetime.timedelta(days=7)),
            }),
        ))




class ExportCsvMixin:

    '''This class is for adding download action'''

    def export_as_csv(self, request, queryset):

        meta = self.model._meta
        field_names = [field.name for field in meta.fields]

        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename=todos.csv'
        writer = csv.writer(response)

        writer.writerow(field_names)
        for obj in queryset:
            row = writer.writerow([getattr(obj, field) for field in field_names])

        return response

    export_as_csv.short_description = "Download selected Todos in CSV"



@admin.register(Status)
class StatusAdmin(admin.ModelAdmin):
    list_display = ['id','name']


@admin.register(TodoList)
class TodoListAdmin(admin.ModelAdmin, ExportCsvMixin):
    list_display    = ['id','title', 'description', 'status', 'created', 'modified', 'due_date']
    list_filter     = ('status',('due_date', MyDateTimeFilter))
    search_fields   = ['title']
    actions         = ['export_as_csv']
