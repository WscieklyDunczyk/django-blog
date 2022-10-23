from django.shortcuts import render, redirect
from .forms import UserRegisterForm, UserUpdateForm, ProfilUpdateForm
from django.views import View
from django.contrib import messages
from django.contrib.auth.decorators import login_required


@login_required
def profile(request):
    if request.POST:
        user_form = UserUpdateForm(request.POST, instance=request.user)
        profil_form = ProfilUpdateForm(request.POST, request.FILES, instance=request.user.profil)
        if user_form.is_valid() and profil_form.is_valid():
            user_form.save()
            profil_form.save()
            messages.success(request, 'Profil zaktualizowany!')
    else:
        user_form = UserUpdateForm(instance=request.user)
        profil_form = ProfilUpdateForm(instance=request.user.profil)

    context = {
        'user': request.user,
        'user_form': user_form,
        'profil_form': profil_form,
    }
    return render(request, 'users/profil.html', context)


class Register(View):
    form_class = UserRegisterForm
    template_name = 'users/users_register.html'

    def get(self, request, *args, **kwargs):
        form = self.form_class()
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Konto zostało utworzone dla {username}!')
            return redirect('login')
        return render(request, self.template_name, {'form': form})
