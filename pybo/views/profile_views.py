from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User

@login_required(login_url='common:login')
def profile_detail(request, user_id):
    '''
    User의 프로필
    '''
    # 다른 user 프로필에 접근하는 경우
    if request.user.id != user_id:
        messages.error(request, '해당 프로필에 접근할 수 없습니다')
        return redirect('index')

    user = get_object_or_404(User, pk=user_id)
    context = {'user': user}
    return render(request, 'pybo/user_detail.html', context)