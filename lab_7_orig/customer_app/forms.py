from django import forms
from customer_app.models import Customer, Order, Contact

class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ['name', 'logo', 'address', 'city', 'state', 'zipcode', 'notes', 'linkedin_url']

class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = '__all__'

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = '__all__'

    