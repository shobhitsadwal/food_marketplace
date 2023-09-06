from django.shortcuts import render , redirect
from django.http import HttpResponse
from .forms import UserRegisterationForm
from .models import User
from django.contrib import messages

# Create your views here.



def register_user_view(request):
    if request.method == "POST":
        form = UserRegisterationForm(request.POST)
        if form.is_valid():
            # user = form.save(commit=False)
            # user.role =  User.CUSTOMER
            # user.save()

            first_name = form.cleaned_data["first_name"]
            last_name = form.cleaned_data['last_name']
            email = form.cleaned_data['email']
            phone_number  = form.cleaned_data['phone_number']
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            # creating the new user here 

            user = User.objects.create_user(first_name = first_name,
                                last_name = last_name,
                                email = email,
                                username = username,
                                password = password
                                )
            
            user.role = User.CUSTOMER
            user.phone_number = phone_number

            user.save()

            messages.success(request,"message has been sent")
            return redirect ('registeruser') 
           
        else:
            messages.error(request,'there seems to be some error in your form')
            return render(request, 'accounts/registeruser.html', {'form': form})
            
    else:
        form = UserRegisterationForm()
    return render(request, "accounts/registeruser.html",context={
        'form':form
    })
