from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone
from .models import Club, Comment

def home(request):
    clubs = Club.objects.all()
    return render(request, 'home.html', {'clubs':clubs})

def detail(request, id):
    club = get_object_or_404(Club, pk = id)
    return render(request, 'detail.html', {'club':club})

def new(request):
    return render(request, 'new.html')

def create(request):
    new_club = Club()
    new_club.clubname = request.POST['clubname']
    new_club.personnel = request.POST['personnel']
    new_club.clubinfo = request.POST['clubinfo']
    new_club.save()
    return redirect('detail', new_club.id)

def edit(request, id):
    edit_club = Club.objects.get(id=id)
    return render(request, 'edit.html', {'club':edit_club})

def update(request, id):
    update_club = Club.objects.get(id=id)
    update_club.clubname = request.POST['clubname']
    update_club.personnel = request.POST['personnel']
    update_club.clubinfo = request.POST['clubinfo']
    update_club.save()
    return redirect('detail', update_club.id)

def delete(request, id):
    delete_club = Club.objects.get(id=id)
    delete_club.delete()
    return redirect('home')

def comment(request, club_id):
    if request.method == 'POST':
        new_comment = Comment()
        new_comment.club = get_object_or_404(Club, pk=club_id)
        new_comment.comment = request.POST['comment']
        new_comment.created_at = timezone.now()
        new_comment.save()
    return redirect('detail', club_id)