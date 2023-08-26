from django.shortcuts import render
from django.http import JsonResponse
from .models import chatMessages
from hospital.models import *
from doctors.models import *
from django.views.decorators.csrf import csrf_exempt
from django.db.models import Q


def get_chats(request):
    chat_list = []

    sender = UserP.objects.get(
        email=request.session['cur_user'].get('email'))
    print(request.session['to'], 'sent_to')
    email = request.session['to']
    print(email)
    sent_to = UserP.objects.get(email=email)
    print(sent_to)
    chats = chatMessages.objects.filter(
        Q(user_from=sender, user_to=sent_to) |
        Q(user_from=sent_to, user_to=sender)
    )
    print('chat->', chats)
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
        # MUST change herer
        content = request.POST.get('message')
        # Replace with the actual receiver's username
        print(request.session['to'], "user_to")
        user_to = UserP.objects.get(email=request.session['to'])
        message = chatMessages.objects.create(
            user_from=sender,
            user_to=user_to,
            message=content,
        )
        return JsonResponse({'success': True})
    return JsonResponse({'success': False})


def chatIndividual(request):
    chat_list = []

    sender = UserP.objects.get(
        email=request.session['cur_user'].get('email'))
    print(request.GET.get('to'), 'sent_to')
    email = request.GET.get('to')
    request.session['to'] = email
    print(email)
    sent_to = UserP.objects.get(email=email)
    print(sent_to)
    chats = chatMessages.objects.filter(
        Q(user_from=sender, user_to=sent_to) |
        Q(user_from=sent_to, user_to=sender)
    )
    print('chat->', chats)
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
    return render(request, "chatfrontend/each_user_chat.html")
