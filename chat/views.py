from django.shortcuts import render
from django.http import JsonResponse
from .models import chatMessages
from hospital.models import *
from django.views.decorators.csrf import csrf_exempt


def get_chats(request):
    chats = chatMessages.objects.all()
    chat_list = []
    for message in chats:
        chat_list.append({
            'user_to': message.user_to.username,
            # Assuming 'user_from' has a 'username' field
            'user_from': message.user_from.username,
            'content': message.message,
            # Convert to string
            'timestamp': message.date_created.strftime("%b-%d-%Y %H:%M"),
        })
    request.session['chats'] = chat_list
    return JsonResponse(chat_list, safe=False)


@csrf_exempt
def send_chat(request):
    if request.method == 'POST':
        print("sender", request.session['cur_user'].get('username'))
        sender = UserP.objects.get(
            email=request.session['cur_user'].get('email'))
        content = request.POST.get('message')
        # Replace with the actual receiver's username
        print(request.POST.get('user_to'), "user_to")
        user_to = UserP.objects.get(username=request.POST.get('user_to'))
        message = chatMessages.objects.create(
            user_from=sender,
            user_to=user_to,
            message=content,
        )
        return JsonResponse({'success': True})
    return JsonResponse({'success': False})
