from django import forms
from .models import Category, Shop, Review

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name']

class ShopForm(forms.ModelForm):
    class Meta:
        model = Shop
        fields = '__all__'
        exclude = ['created_at', 'updated_at', 'category']

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['comment', 'photo1']
