from django  import  forms
from testapp.models  import Report



class ReportForm(forms.ModelForm):
    class Meta:
        model = Report
        fields = "__all__"