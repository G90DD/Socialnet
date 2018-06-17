from django.shortcuts import render, render_to_response
from django.http import HttpResponse
from django.template import loader
from .models import Group

# Create your views here.

def index(request):
    #template = loader.get_template('socialnet/index.html')
    #return HttpResponse(template.render())
    return render(request, 'socialnet/index.html')

def profile(request):
    return HttpResponse("Yo, this is your profile.")

def front_page(request):
    return render(request, 'socialnet/front_page.html')

def groups(request):
    #show total number of groups:
    total_groups = Group.objects.all().count()
    groups_user1 = Group.objects.filter(group_owner='user1').count()
    groups_user2 = Group.objects.filter(group_owner='user2').count()
    
    #return render(request, 'socialnet/groups.html')
    return render(request, 'socialnet/groups.html', context={'total_groups':total_groups, 'groups_user1':groups_user1, 'groups_user2':groups_user2},)
