# accounts/views.py

from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import login
import json
from .models import UserProfile, CurrencyAlert
from .forms import UserProfileForm, SignUpForm

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # 회원가입 후 자동 로그인
            return redirect('profile_setup')  # 회원가입 후 프로필 설정 페이지로 이동
    else:
        form = SignUpForm()
    return render(request, 'accounts/signup.html', {'form': form})

def profile_setup(request):
    if request.method == 'POST':
        form = UserProfileForm(request.POST)
        if form.is_valid():
            profile = form.save(commit=False)
            profile.user = request.user
            profile.save()
            return redirect('investment_analysis')
    else:
        form = UserProfileForm()
    return render(request, 'accounts/profile_setup.html', {'form': form})

def investment_analysis(request):
    profile = UserProfile.objects.get(user=request.user)
    investment_tendency = profile.investment_tendency
    recommended_strategy = "안정형 포트폴리오" if investment_tendency == "stable" else (
        "공격형 포트폴리오" if investment_tendency == "aggressive" else "균형형 포트폴리오"
    )
    return render(request, 'accounts/investment_analysis.html', {'strategy': recommended_strategy})

@csrf_exempt
def set_alert(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        CurrencyAlert.objects.create(
            user=request.user,
            currency=data['currency'],
            target_rate=data['target_rate']
        )
        return JsonResponse({'status': 'success'})
    return JsonResponse({'status': 'fail'}, status=400)
