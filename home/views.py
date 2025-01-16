from django.shortcuts import get_object_or_404, render, HttpResponse, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from home.models import feedback
from home.models import Company_profile
from home.models import tender
from home.models import create_progress
from home.models import applications
from django.contrib.auth.validators import UnicodeUsernameValidator
from django.core.exceptions import ValidationError
from django.core.mail import send_mail
import random
# from twilio.rest import Client
# Create your views here.

def index(request):
    # return HttpResponse("This is home page")
    return render(request,'index.html')

# def handlesignup(request):
#     if request.method =='POST':
#         username = request.POST['username']
#         email = request.POST['email']
#         password1 = request.POST['password1']
#         password2 = request.POST['password1']

#         # checks for error
#         if password1 != password2:
#             messages.error(request,"Password do not match")
#             return redirect('home')
#         #create the user
#         myuser = User.objects.create_user(username,email,password1)
#         myuser.save()
#         messages.success(request,'Company is Registered successfull...!')
#         return redirect('home')
#     else:
#         return HttpResponse('404 - Not Found')








def handlesignup(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        # mob = request.POST['mobno']
        password1 = request.POST['password1']
        password2 = request.POST['password2']  
        
     
    
        if password1 != password2:
            messages.error(request, "Passwords do not match")
            return redirect('home')

        
        try:
            UnicodeUsernameValidator()(password1)
        except ValidationError as e:
            messages.error(request, f"Invalid password: {', '.join(e.messages)}")
            return redirect('home')
        # length = 6
        # otp = ' '.join(random.choice('0123456789') for i in range(length))

        myuser = User.objects.create_user(username, email, password1)
        myuser.save()
        messages.success(request, 'Company is registered successfully!')
       
        send_mail(
            'System Generated Mail',
            'Your Company has been Reristered successfully, Thank You',
            'govtender78@gmail.com',
            [email],
            fail_silently=False,
            
        )
        return redirect('home')
#         account_sid = 'AC40fcfdf7336795eaf2db60a98a74991e'
#         auth_token = 'b5c6f503f91e3b8218eb9dffdce8854b'

# # Twilio phone number associated with WhatsApp (use the format 'whatsapp:+[country code][phone number]')
#         twilio_phone_number = 'whatsapp:+18036368622'

# # Recipient's phone number (use the format 'whatsapp:+[country code][phone number]')
#         recipient_number = 'whatsapp:+'+ mob

# # Your message
#         message_body = 'Your Company has been Reristered successfully, Thank you.'

# # Initialize Twilio client
#         client = Client(account_sid, auth_token)

# # Send message
#         message = client.messages.create(
#             body=message_body,
#             from_=twilio_phone_number,
#             to=recipient_number
#         )

#         print(f"Message sent successfully! SID: {message.sid}")
           
        
        
        
        
    else:
        return HttpResponse('404 - Not Found')



def handlelogin(request):
    if request.method =='POST':
        loginusername = request.POST['loginusername']
        loginpassword = request.POST['loginpass']
     
        user = authenticate(username =loginusername, password=loginpassword)

        if user is not None:
            login(request,user)
            messages.success(request,"Successfully logged In")
            return render(request,'company.html')
            # return redirect('home')
        else:
            messages.error(request,"Invalid Credentials, Please try again")
           
            return redirect('home')

def handlelogout(request):
    logout(request)
    messages.success(request,'Successfully logout')
    return redirect('home')

    return HttpResponse('hendlelogout')

def feedback(request):
    if request.method =="POST":
        name = request.POST.get('name')
        suggestion = request.POST.get('suggestions')
        rating = request.POST.get('rating')
        Feedback = feedback(name=name, suggestions=suggestion, rating=rating)
        Feedback.save()
    return render(request,'feedback.html')

def company(request):
    return render(request,'company.html')

def c_profile(request):
    if request.method =="POST":
        comp_id = request.POST.get('company_id')
        comp_name = request.POST.get('company_name')
        comp_phno = request.POST.get('company_phone')
        comp_add = request.POST.get('company_add')
        comp_email = request.POST.get('company_email')
        comp_Username = request.POST.get('company_name')
        Profile = Company_profile(C_id=comp_id,C_name = comp_name,C_phone=comp_phno,C_add=comp_add,C_email=comp_email,C_username=comp_Username)
        Profile.save()
        return render(request,'company.html')


def progress(request):
    return render(request,'progress.html')



def govlogin(request):
    if request.method =="POST":
        username = request.POST.get('loginusername')
        password = request.POST.get('loginpass')
        if username =="govind" and password =="govind":
            return render(request,'govofficial.html')
        else:
            return render(request,'index.html')

       
def managet(request):
    allTenders = tender.objects.all()
    return render(request,'managet.html',{"allTenders":allTenders})

def addtender(request):
    if request.method == "POST":
        # t_id = request.POST.get('tender_id')
        sector_name = request.POST.get("sector_name")
        time = request.POST.get("time")
        price = request.POST.get("price")
        s_date = request.POST.get("start_date")
        e_date = request.POST.get("end_date")
        address = request.POST.get("address")
        city = request.POST.get("city")
        state = request.POST.get("state")
        pin = request.POST.get("pin")
        Descreption = request.POST.get("descreption")
       
        tenders = tender(sector_name = sector_name,Time_dur = time,
        price = price,Start_date =s_date, end_date = e_date, Address = address,
        city = city,state = state, pin = pin , descreption = Descreption)
        tenders.save()

        return render(request,'managet.html')

def viewtender(request):
    if request.method == "POST":
        t_id = request.POST.get("tid")
        tend = tender.objects.get(t_id=t_id)
        return render(request,'viewtender.html',{'tend':tend})

     
def handletender(request):
    alltenders = tender.objects.all()
    return render(request,'tenders.html',{"alltenders":alltenders})
     
def comp_apply(request):
     if request.method == "POST":
        t_id = request.POST.get("tid")

     alert_message = "You have applied successfully."
     response_content = f"""
        <html>
        <head>
            <script>
                window.onload = function() {{
                    alert("{alert_message}");
                }};
            </script>
        </head>
        <body>
            <p>{alert_message}</p>
        </body>
        </html>
    """
     return HttpResponse(response_content, status=200)



def chat(request):
    return render(request, "chat.html")
     
def create_progress(request):
    if request.method == "POST":
        tid_value = request.POST.get("tid")
        desc = request.POST.get("desc")
        
        progres = create_progress(tid = tid_value,descreption = desc)
        progres.save()
        return render(request,'tender.html')
    

def mail(request):
    if request.method == "POST":
        mailid = request.POST.get("cmailid")
        content = request.POST.get("mailcont")
        send_mail(
            'System Generated Mail',
            content,
            'govtender78@gmail.com',
            [mailid],
            fail_silently=False,
        )
        return render(request,'Comp_appli.html')
    











def application(request):
    if request.method == "POST":
        t_id=request.POST.get("tid")
        c_email=request.POST.get("c_email")
        q_pri = request.POST.get("q_price")
        q_exp = request.POST.get("q_exp")
        q_dur = request.POST.get("q_duration")

        apply = applications(tid=t_id, q_price =q_pri, q_exp = q_exp, q_duration = q_dur,c_email = c_email)
        
        apply.save()
        return render(request,'tenders.html')

def comp_apply(request):
    allapplis = applications.objects.all()
    return render(request,'Comp_appli.html',{"allapplis":allapplis})

def deltender(request):
    
    

    if request.method =="POST":
        id = request.POST.get("tid")
        obj = get_object_or_404(tender,pk=id)
        obj.delete()
        return render(request,'managet.html')
