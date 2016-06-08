from django import forms
from .models import Category, Shop, Review

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name']

class ShopForm(forms.ModelForm):
    class Meta:
        model = Shop
        fields = ['name','phone','address','description','photo1','photo2','photo3','category']


class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['comment', 'photo1']
