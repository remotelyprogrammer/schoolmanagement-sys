from django import forms
from django.forms import inlineformset_factory
from .models import Student, Contact, Address

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['first_name','middle_name', 'last_name', 'country_of_birth', 'birth_place','suffix', 'birth_date', 'nationality', 'civil_status', 'sex', 'religion', 'mobile_number', 'telephone_number', 'personal_email']


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['full_name', 'relationship', 'mobile_number']

ContactFormSet = inlineformset_factory(
    Student, Contact, form=ContactForm,
    fields=['full_name', 'relationship', 'mobile_number'], extra=1, can_delete=True
)

class AddressForm(forms.ModelForm):
    class Meta:
        model = Address
        fields = ['province', 'city', 'house_number', 'barangay', 'postal_code']
        # Or use '__all__' to include all fields

AddressFormSet = inlineformset_factory(
    Student, Address, form=AddressForm,
    fields=['province', 'city', 'house_number', 'barangay', 'postal_code'], extra=1, can_delete=False
)

class StudentDetailForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = '__all__'
    
    def __init__(self, *args, **kwargs):
        super(StudentDetailForm, self).__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['disabled'] = True


class AddressDetailForm(forms.ModelForm):
    class Meta:
        model = Address
        fields = '__all__'
    
    def __init__(self, *args, **kwargs):
        super(AddressDetailForm, self).__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['disabled'] = True


class ContactDetailForm(forms.ModelForm):
    class Meta:
        model = Address
        fields = '__all__'
    
    def __init__(self, *args, **kwargs):
        super(ContactDetailForm, self).__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['disabled'] = True