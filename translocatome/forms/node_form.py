from django import forms

class NodeForm(forms.Form):

    uni_prot_ac = forms.CharField(max_length=50, required=False)
    gene_name = forms.CharField(max_length=50, required=False)
