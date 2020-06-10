from . import models
import django_filters

class DeptFilter(django_filters.FilterSet):
    model = models.Department
    department = django_filters.CharFilter(lookup_expr='icontains', label='')
    # class Meta:
    #     model = models.Department
    #     fields = {
    #         'department' : ['icontains']
    #     }
