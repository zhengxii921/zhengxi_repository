from django import forms
from .models import Place


class PlaceCreateForm(forms.ModelForm):
    opentime = forms.TimeField(
        label="開店時刻",
        widget=forms.DateInput(attrs={"type":"time"})
    )
    closetime = forms.TimeField(
        label="閉店時刻",
        widget=forms.DateInput(attrs={"type":"time"})
    )

    class Meta:
        model = Place
        fields = "__all__"