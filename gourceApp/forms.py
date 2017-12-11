from django import forms
from django.forms import ModelForm
from .models import *
from gourceApp.choices import *

class HierarquiaForm(forms.ModelForm):
    class Meta:
        model = Hierarquia
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(HierarquiaForm, self).__init__(*args, **kwargs)
        new_fields = {}
        for data in Hierarquia.objects.all():
            field_name = 'mytext'.format(data.name.lower())
            new_fields[field_name] = field
            self.fields.update(new_fields)

class DadosForm(ModelForm):

    class Meta:
        model = Arvore
        fields = ('nome', 'escola', 'serie', 'cidade')

    def __init__(self, *args, **kwargs):
        super(DadosForm, self).__init__(*args, **kwargs)
        self.fields['nome'].widget.attrs['class']='form-control'
        self.fields['escola'].widget.attrs['class']='form-control'
        self.fields['serie'] = forms.ChoiceField(choices = SERIES, label="Série", initial='', widget=forms.Select(), required=True)
        self.fields['cidade'].widget.attrs['class']='form-control'

class DadosGource(ModelForm):

    class Meta:
        model = Gource
        fields = ('titulo', 'cor', 'fonte', 'elasticidade')

    def __init__(self, *args, **kwargs):
        super(DadosGource, self).__init__(*args, **kwargs)
        self.fields['titulo'].widget.attrs['class']='form-control'
        self.fields['cor'].widget.attrs['class']='form-control'
        self.fields['fonte'].widget.attrs['class']='form-control'
        self.fields['elasticidade'].widget.attrs['class']='form-control'
