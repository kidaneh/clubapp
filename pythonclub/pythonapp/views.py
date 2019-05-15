from django.shortcuts import render, get_object_or_404
from .models import Meeting, Minute, Resource, event
from .forms import meetingForm
# Create your views here.
def index (request):
    return render (request, 'pythonapp/index.html')

def getResource(request):
    resource_list=Resource.objects.all()
    return render(request, 'pythonapp/Resource.html',{'resource_list':resource_list})

def getmeetings(request):
    meetings_list=Meeting.objects.all()
    return render(request, 'pythonapp/meetings.html',{'meetings_list':meetings_list})

def meetingdetails(request, id):
    meetd=get_object_or_404(Meeting, pk=id)
    context={
        'meetd' : meetd
    }
    return render(request,'pythonapp/meetdetails.html', context=context)

def newMeeting(request):
    form=meetingForm
    if request.method=='POST':
        form =meetingForm(request.POST)
        if form.is_valid():
            post=form.save(commit=True)
            post.save
            form=meetingForm
    return render(request, 'pythonapp/newmeeting.html', {'form': form})

    