from django.shortcuts import render
from .models import COUNT_TB
# Create your views here.
def index_view(request):
    if request.method == 'POST':
        try:
            COUNT_TB.objects.get()
        except:
            first_row = COUNT_TB()
            first_row.save()
        else:
            upgrade_row = COUNT_TB.objects.get()
            upgrade_row.count_num +=1
            upgrade_row.save()
    
    
    return render(request,'mtvtest/index.html')