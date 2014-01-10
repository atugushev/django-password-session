from django.contrib.auth.decorators import login_required
from django.http import HttpResponse

from password_session.signals import password_changed


@login_required(login_url='/admin/')
def change_password_view(request):
    user = request.user
    user.set_password(request.POST.get('password'))
    user.save()
    password_changed.send(sender=user.__class__, user=user, request=request)
    return HttpResponse("Hello, %s! Your password has been changed!" % user.username)