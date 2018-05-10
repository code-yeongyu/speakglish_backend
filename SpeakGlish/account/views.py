from django.http import JsonResponse
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.models import User
from django.contrib.auth.forms import PasswordChangeForm
from django.views.decorators.csrf import ensure_csrf_cookie

@ensure_csrf_cookie
def change_password(request) :
    if request.method=="POST" :
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)
            return JsonResponse({'password_updated':True})
        else :
            return JsonResponse({'password_updated':False})

@ensure_csrf_cookie
def change_username(request) :
    if request.method=="POST" :
        try :
            user = User.objects.get(username = request.user.username)
            user.username = request.POST['new_username']
            user.save()
            return JsonResponse({'username_updated':True})
        except :
            return JsonResponse({'username_updated':False})