from django.shortcuts import render, redirect
from .forms import SignUpForm
from django.contrib.auth import login as auth_login
from django.views.generic import UpdateView
from django.contrib.auth.models import User
from django.urls import reverse_lazy


def signup(request):
    form = SignUpForm()
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request, user)
            return redirect('login')
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})


class UserUpdateView(UpdateView):
    model = User
    fields = ['username', 'first_name', 'last_name', 'email']
    template_name = 'my_account.html'
    success_url = reverse_lazy('home:todo_list')

    def get_object(self):
        return self.request.user
