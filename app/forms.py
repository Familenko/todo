from django.forms import ModelForm

from app.models import Task, Tag


class TaskForm(ModelForm):
    class Meta:
        model = Task
        fields = "__all__"


class TagForm(ModelForm):
    class Meta:
        model = Tag
        fields = "__all__"
