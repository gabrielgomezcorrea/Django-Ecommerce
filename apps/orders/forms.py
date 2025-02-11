from django import forms
from .models import Order


class OrderCreateForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ["full_name", "email", "address"]
        widgets = {
            "full_name": forms.TextInput(
                attrs={
                    "class": " mb-3 border border-gray-300 rounded w-full py-2 px-3 text-gray-700 focus:outline-none focus:ring-2 focus:ring-blue-500",
                }
            ),
            "email": forms.EmailInput(
                attrs={
                    "class": " mb-3 border border-gray-300 rounded w-full py-2 px-3 text-gray-700 focus:outline-none focus:ring-2 focus:ring-blue-500",
                }
            ),
            "address": forms.Textarea(
                attrs={
                    "class": " mb-3 border border-gray-300 rounded w-full py-2 px-3 text-gray-700 focus:outline-none focus:ring-2 focus:ring-blue-500",
                    "placeholder": "Shipping Address",
                    "rows": 3,
                }
            ),
        }
