from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import *
from .forms import *
# Create your views here.
@login_required
def chat(req):
    chat_group = get_object_or_404(ChatGroup, group_name = "test-chat")
    chat_messages = chat_group.chat_messages.all()[:30]
    form = ChatmessageCreateForm()

    if req.method == "POST":
        form = ChatmessageCreateForm(req.POST)
        if form.is_valid:
            message = form.save(commit=False)
            message.author = req.user
            message.group = chat_group
            message.save()
            return redirect('home')

    return render(req, "chat/chat.html", {
        "chat_messages" : chat_messages,
        "form": form
    })