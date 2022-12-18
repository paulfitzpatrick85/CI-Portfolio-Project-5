from django.shortcuts import render, get_object_or_404, redirect
from django.views import generic, View
from .models import Review
from .forms import ReviewForm
from django.contrib import messages


# render reviews page
def reviews_list(request):
    reviews = Review.objects.filter(review_approved=True)
    context = {
        'reviews': reviews
    }

    return render(request, 'reviews.html', context)


# render add review page
def add_review(request):
    form = ReviewForm(request.POST)

    if request.method == "POST":
        form = ReviewForm(request.POST)
        if form.is_valid():
            form.instance.customer_email = request.user.email
            form.instance.name = request.user.username
            review = form.save(commit=False)
            review.save()        
            messages.success(request, 'Thank your for reviewing our service, \
            your review will be displayed shortly.')
        else:
            form = ReviewForm()

        return redirect('reviews.html')  # directed here after adding review
    form = ReviewForm()
    context = {
        'form': form, 'review_added': True,
    }
    return render(request, 'add_review.html', context)


# render edit review page
def edit_review(request, review_id):
    review = get_object_or_404(Review, id=review_id)
    if review.customer_email != request.user.email:
        messages.success(request, 'Sorry, this is not your view to edit.')
        return redirect('/reviews.html')
    else:
        form = ReviewForm(data=request.GET)
        if request.method == 'POST':                      
            form = ReviewForm(request.POST, request.FILES,
                              instance=review)
            if form.is_valid():
                form.instance.customer_email = request.user.email
                review.save()
                messages.success(request,
                                 'Your review was edited successfully.'
                                 'Please return to the "Reviews".')
            else:
                # Prepopulation happens here:
                data = {"customer_name": review.customer_name,
                        "customer_email": review.customer_email,
                        "customer_review": review.customer_review, }             
                form = ReviewForm(initial=data) 
        context = {"form": ReviewForm(instance=review)}
        return render(request, 'edit_review.html', context, )    


# delete review
def delete_review(request, review_id):
    review = get_object_or_404(Review, id=review_id)
    # Authenticated user can delete only their own reviews
    if review.customer_email != request.user.email:
        messages.success(request, 'Sorry, this is not your review to delete.')
        return redirect('/reviews.html')
    else:
        review.delete()
        messages.success(request,
                         'Your Review Has Been Deleted.')
    return redirect('/')
