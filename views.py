from django.shortcuts import render, get_object_or_404, redirect
from .forms import ReviewForm
# imports data from the model Review
from .models import Review


# Displays the Home page
def InlineSpeedSkates_Home(request):
    return render(request, 'skates_home.html')

# Creates a new Record
def Review_Create(request):
    form = ReviewForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('Review_Create')
    else:
        print(form.errors)
        form = ReviewForm()
        context = {
            'form': form,
        }
    return render(request, 'skates_create.html', context)


# Displays all Resources add to database
def Review_Display(request):
    # gets objects of from database
    records = Review.objects.all().order_by('overall_rating')
    return render(request, 'skates_display.html', {'records': records})