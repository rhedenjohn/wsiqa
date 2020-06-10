from django import forms
from . models import Exams
from durationwidget.widgets import TimeDurationWidget

class ExamForm(forms.ModelForm):
    # timeDuration = forms.DurationField(widget=TimeDurationWidget(show_days=False, show_hours=True, show_minutes=True, show_seconds=True), required=False)
    class Meta():
        model = Exams
        fields = '__all__'
