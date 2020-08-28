""" Remote blob host forms
"""
from django import forms


class URLForm(forms.Form):
    """Remote blob host URL form"""

    url = forms.URLField(label="")
