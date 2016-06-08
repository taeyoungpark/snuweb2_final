from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect, render
from .models import Category, Shop, Review
from .forms import CategoryForm, ShopForm, ReviewForm
from datetime import date
from django.core.urlresolvers import reverse


def index(request):
    category_list = Category.objects.all()
    recent_reviews = Review.objects.filter(updated_at=date.today()).all()
    #최근 = 오늘 작성된
    return render(request, 'blog/index.html', {
        'category_list': category_list, 'recent_reviews': recent_reviews,
    })

def category_new(request):
    if request.method == 'POST':
        form = CategoryForm(request.POST, request.FILES)
        if form.is_valid():
            category = form.save()
            url = reverse('blog:category_detail', args=[category.pk])
            messages.success(request, '새로운 포스팅을 등록했습니다.')

            return redirect(url)
    else:
        form = CategoryForm()
    return render(request, 'blog/category_form.html', {
        'form': form,
    })

def category_edit(request, pk):
    category = get_object_or_404(Category, pk=pk)
    if request.method == 'POST':
        form = CategoryForm(request.POST, instance=category)
        if form.is_valid():
            category = form.save()
            messages.success(request, '카테고리가 수정되었습니다.')
            return redirect('blog:category_detail', pk)
    else:
        form = CategoryForm(instance=comment)
    return render(request, 'blog/category_form.html', {
        'form': form,
    })


def category_detail(request, pk):
    category = get_object_or_404(Category, pk=pk)
    return render(request, 'blog/category_detail.html', {
        'category': category,
    })



def shop_new(request):
    if request.method == 'POST':
        form = ShopForm(request.POST, request.FILES)
        if form.is_valid():
            shop = form.save()
            url = reverse('blog:shop_detail', args=[shop.pk])
            messages.success(request, '새로운 샵을 등록했습니다.')
            return redirect(url)
    else:
        form = ShopForm()
    return render(request, 'blog/shop_form.html', {
        'form': form,
    })

def shop_edit(request, pk):
    shop = get_object_or_404(Shop, pk=pk)
    if request.method == 'POST':
        form = ShopForm(request.POST, instance=shop)
        if form.is_valid():
            shop = form.save()
            messages.success(request, '샵이 수정되었습니다.')
            return redirect('blog:shop_detail', pk)
    else:
        form = ShopForm(instance=shop)
    return render(request, 'blog/shop_form.html', {
        'form': form,
    })


def shop_detail(request, pk):
    shop = get_object_or_404(Shop, pk=pk)
    return render(request, 'blog/shop_detail.html', {
        'shop': shop,
    })

@login_required
def review_new(request, shop_pk):
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.shop = get_object_or_404(Shop, pk=shop_pk)
            review.user = request.user
            review.save()
            messages.success(request, '새로운 리뷰가 등록되었습니다.')
            return redirect('blog:shop_detail', shop_pk)
    else:
        form = ReviewForm()
    return render(request, 'blog/review_form.html', {
        'form': form,
    })


@login_required
def review_edit(request, shop_pk, pk):
    review = get_object_or_404(Review, pk=pk)

    if request.method == 'POST':
        form = ReviewForm(request.POST, request.FILES, instance=review)
        if form.is_valid():
            review = form.save(commit=False)
            review.post = get_object_or_404(Post, pk=post_pk)
            review.user = request.user
            review.save()
            messages.success(request, '댓글이 수정되었습니다.')
            return redirect('blog:shop_detail', shop_pk)
    else:
        form = ReviewForm(instance=review)
    return render(request, 'blog/review_form.html', {
        'form': form,
    })
