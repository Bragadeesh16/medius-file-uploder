from django.shortcuts import render
from .forms import *
import pandas as pd
from .models import *
from django.core.mail import send_mail
from django.conf import settings

def summary(file_name,type):

    type = type.lower()
    if type == 'csv':
        df = pd.read_csv(file_name)
        summary = df.groupby(['Cust State', 'DPD']).size().reset_index(name='Count')
    elif type == 'xlsx':
        df = pd.read_excel(file_name)
        summary = df.groupby(['Cust State', 'DPD']).size().reset_index(name='Count')
    else:
        summary = 'please do uplode only of extension support csv or excel file'

    return summary


def home(request):
    form = file_form()
    if request.method == 'POST':
        form = file_form(request.POST,request.FILES)
        if form.is_valid():
            file_name = request.FILES['file']
            data_type = str(file_name).split('.')
            datas  = summary(file_name,data_type[-1])
            datas = datas.to_string(index=False)
            send_mail(
                'Summary Report',
                datas,
                'bragadeesh03294@gmail.com',
                ['tech@themedius.ai', 'CC HR@themedius.ai'],)
            return render(request, 'summary.html',{'summary':datas})
    else:
        form = file_form()
    return render(request, 'index.html', {'form': form})