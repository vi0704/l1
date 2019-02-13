from django.shortcuts import render, redirect
import glob
import pandas as pd
from .models import LogData
from .forms import Sessioncountform

# Create your views here.
def LogView(request):
    form = Sessioncountform(request.POST)
    if request.method == 'POST':

        if form.is_valid():
            date = form.cleaned_data['date']
            if LogData.objects.filter(date=date).exists:
                data = LogData.objects.filter(date=date)
                return render(request, 'index.html', {'data': data})
            else:

                path = r'E:\Logs\Bdxw\Sep2018\Processed_files\clean_log'
                file = glob.glob(path + '*{}.log.gz'.format(date))
                for k in file:
                    clean_data = pd.read_csv(k)
                    users = clean_data['uniqueid'].nunique()
                    sessions = clean_data['sessionid'].nunique()
                    sessions_per_user = round(sessions/users, 2)
                    LogData.objects.create(date=date, users=users, sessions=sessions, sessions_per_user=sessions_per_user)
                    data = LogData.objects.filter(date=date)

                    return render(request, 'index.html', {'data': data})
    else:
        form = Sessioncountform()


    return render(request, 'form1.html', {'form':form})

