from django import forms
from oneup.models import As

class AsForm(forms.ModelForm):
    class Meta:
        model = As
        fields = ['asname', 'ph', 'pronumber']
        labels = {
            'asname': '이름',
            'ph': '전화번호',
            'pronumber': '제품번호',
        }