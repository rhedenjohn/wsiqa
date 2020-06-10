from import_export import resources
from .models import Questions

class QuestionsResource(resources.ModelResource):
    class Meta:
        model = Questions
