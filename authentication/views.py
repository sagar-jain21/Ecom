from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from authentication.forms import CreateUserForm
from django.contrib.auth import authenticate, login, logout

# Create your views here.


class RegisterView(TemplateView):

    def get(self, request, *args, **kwargs):

        if request.user.is_authenticated:
            return redirect('/home')

        form = CreateUserForm()

        return render(
            request,
            template_name='authentication/signup.html',
            context={
                "signupform": form,
            }
        )

    def post(self, request, *args, **kwargs):

        form = CreateUserForm(request.POST, request.FILES)
        if form.is_valid():
            # new_user = form.save(commit=False)
            # password = form.cleaned_data['password1']
            # new_user.set_password(password)
            # new_user.save()
            form.save()
            return redirect('/login')

        return render(
            request,
            template_name='authentication/signup.html',
            context={
                "signupform": form,
            }
        )


class LoginView(TemplateView):

    def get(self, request, *args, **kwargs):

        if request.user.is_authenticated:
            return redirect('/home')

        form = CreateUserForm()

        return render(
            request,
            template_name='authentication/login.html',
            context={
                "loginform": form,
            }
        )

    def post(self, request, *args, **kwargs):

        form = CreateUserForm()

        email = request.POST.get('email')
        password = request.POST.get('password1')

        user = authenticate(request, username=email, password=password)

        if user:
            login(request, user)
            return redirect('/home')
        else:
            error_message = "Email or Password is Incorrect"

        return render(
            request,
            template_name='authentication/login.html',
            context={
                "error_message": error_message,
                "loginform": form,
            }
        )


class LogoutView(TemplateView):

    def get(self, request, *args, **kwargs):

        logout(request)
        return redirect('/login')


class HomeView(TemplateView):

    def get(self, request, *args, **kwargs):

        if not request.user.is_authenticated:
            return redirect('/login')

        return render(
            request,
            template_name='home.html',
        )
