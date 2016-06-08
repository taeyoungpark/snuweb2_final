from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect, render
from .models import Category, Shop, Review
from .forms import CategoryForm, ShopForm, ReviewForm
