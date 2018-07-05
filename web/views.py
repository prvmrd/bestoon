from django.shortcuts import render

# Create your views here.
def submit_expense(request):
    """user submit an expense"""
    print ("We was here!")

import winsound
def beep(request):
    """Play beep sound"""
    winsound.Beep(440, 250)

def index(request):
    """dispaly index"""
    winsound.Beep(550, 250)

