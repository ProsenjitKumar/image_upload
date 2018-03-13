from django.shortcuts import render
from .models import Profile
from .forms import ProfileForm
# Create your views here.


def SaveProfile(request):
    saved = False

    if request.method == 'POST':
        my_profile_form = ProfileForm(request.POST, request.FILES)

        if my_profile_form.is_valid():
            profile = Profile()
            profile.name = my_profile_form.cleaned_data['name']
            profile.picture = my_profile_form.cleaned_data['picture']
            profile.save()
            saved = True

    else:
        my_profile_form = ProfileForm()

    return render(request, 'image/saved.html', locals())
