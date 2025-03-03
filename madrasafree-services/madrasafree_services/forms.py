from .models import ExtraInfo
from django.forms import ModelForm, BooleanField, CharField


class ExtraInfoForm(ModelForm):
    """
    The fields on this form are derived from the ExtraInfo model in models.py.
    """
    def __init__(self, *args, **kwargs):
        super(ExtraInfoForm, self).__init__(*args, **kwargs)
        self.fields['last_name'].error_messages = {
            "required": u"שם משפחה",
            "invalid": u"להגדיר שם משפחה",
        }
        self.fields['last_name'].required = True
        self.fields['first_name'].error_messages = {
            "required": u"שם פרטי",
            "invalid": u"להגדיר שם פרטי",
        }
        self.fields['first_name'].required = True


    last_name = CharField(
    label=u"שם משפחה")
    first_name = CharField(
    label=u"שם פרטי")


    support_is_donor = BooleanField(
        required=False,
        label='אני רוצה לתמוך במיזם ובתנועה',
    )

    class Meta:
        model = ExtraInfo
        fields = ('support_is_donor','last_name','first_name')
