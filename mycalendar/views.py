from django.shortcuts import render

# Create your views here.
def mycalendar(request):
    return render(request , 'calendar.html') 
    