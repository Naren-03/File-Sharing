from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login,logout



from django.views import View
from .models import UploadFile

# from .models import UploadedFile


def home(request):
    return render(request,'index.html')

def success(request):
    return render(request,'success.html')
    
# class Authentication():
def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        pass1 = request.POST['pass1']
        pass2 = request.POST['pass2']

        if pass1==pass2:
            if User.objects.filter(username=username).exists():
                messages.info(request,"Username Exists")
                return redirect('/register')
            
            
            else:
                myuser = User.objects.create_user(username=username,email=None,password=pass1)
                myuser.save()
                messages.success(request,"Registered Successfully")
                return redirect('/signin')

        else:
            messages.error(request,"Password Didn't Match")
            return redirect('/register')
        
    return render(request, "register_index.html")


def signin(request):

    if request.method == 'POST':
        username = request.POST['username']
        pass1 = request.POST['pass1']

        # print(username,pass1)

        user = authenticate(username=username, password=pass1)

        # print(user)
        if user is not None:
            login(request, user)
            return redirect('/home')
        else:
            messages.error(request, 'Invalid Data')
            return redirect('/signin')

    return render(request, "login_index.html")


def signout(request):
    logout(request)
    messages.success(request, "Logged Out Successfully!!")
    return redirect('/home')




# def upload_file(request):
#     if request.method == 'POST':
#         form = FileUploadForm(request.POST, request.FILES)
#         if form.is_valid():
#             uploaded_file = form.save(commit=False)
#             uploaded_file.save()
#             # return redirect('success_page')
#     else:
#         form = FileUploadForm()

#     return render(request, 'index.html', {'form': form})




def upload(request):

    # if request.method == 'POST':
        uploaded_file = request.get('file')
        print(uploaded_file)

        # if uploaded_file:
        new_file = UploadFile(user=request.user, file=uploaded_file)
        new_file.save()
        return redirect('/success')
        # else:
            # return redirect('/home')