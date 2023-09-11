from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from authentication.forms import CreateUserForm
from django.contrib.auth import authenticate, login, logout
# from django.core.mail import send_mail
# from core import settings
from django.template.loader import render_to_string
from django.core.mail import EmailMessage
from product.models import Product
# from django.utils.html import strip_tags


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
            new_user_email = form.cleaned_data['email']
            form.save()
            html_template = 'authentication/signup_email.html'
            html_message = render_to_string(html_template)
            # plain_message = strip_tags(html_message)   #method 2

            def send_email(
                    to_list,
                    subject,
                    message,
                    sender='jainsagar619@gmail.com'
                    ):
                msg = EmailMessage(subject, message, sender, to_list)
                msg.content_subtype = "html"
                return msg.send()

            send_email(
                subject='Registration Successful',
                message=html_message,
                to_list=[new_user_email],
            )

            # send_mail(                                #method 2
            #     subject='Registration Successful',
            #     message=plain_message,
            #     from_email='jainsagar619@gmail.com',
            #     recipient_list=[new_user_email]
            # )
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

        electrical_appliances = Product.objects.filter(
            category__name__iexact='Electrical Appliances'
            )[:5]
        clothes = Product.objects.filter(
            category__name__iexact='clothes'
            )[:5]
        footwares = Product.objects.filter(
            category__name__iexact='footwares'
            )[:5]
        home_appliances = Product.objects.filter(
            category__name__iexact='home appliances'
            )[:5]

        return render(
            request,
            template_name='home.html',
            context={
                "electrical_appliances": electrical_appliances,
                "clothes": clothes,
                "footwares": footwares,
                "home_appliances": home_appliances,
            }
        )


class DefaultView(TemplateView):

    def get(self, request, *args, **kwargs):

        if request.user.is_authenticated:
            return redirect('/home')
        else:
            return redirect('/login')
