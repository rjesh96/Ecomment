from django.http import HttpResponse
from django.shortcuts import redirect, render
from .models import Comment
from django.contrib import messages


def saveComment(request):
    email = request.POST.get("t1")
    comment = request.POST.get("t2")

    # Writing session
    request.session["status"] = True

    Comment(email=email,comment=comment).save()
    messages.success(request,"Comment is Saved")
    return redirect('/index/')


def openIndex(request):

    return render(request, "index.html")

def showallcomments(request):
    return render(request,"index.html")