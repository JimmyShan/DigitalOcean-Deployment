from django.shortcuts import render, redirect
from django.views import View
from .forms import UserRegisterForm

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from time import sleep

class RegisterView(View):
    def get(self, request):
        form = UserRegisterForm()
        return render(request, 'users/register.html', {'form':form})
    def post(self, request):
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')

def test_chrome():
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    driver = webdriver.Chrome(options=chrome_options)
    driver.maximize_window()
    driver.get("https://www.google.com")
    print(driver.service.path)
    print(driver.title)
    print("ok")

    sleep(10)
    driver.close()
