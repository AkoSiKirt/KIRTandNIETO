from django.shortcuts import render, redirect
from .forms import PoliceReportForm
from django.contrib import messages

def home(request):
    return render(request, 'reports/home.html')

def about(request):
    return render(request, 'reports/about.html')

def contact(request):
    return render(request, 'reports/contact.html')

def submit_report(request):
    if request.method == 'POST':
        form = PoliceReportForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Your report has been successfully submitted.")
            return redirect('submit_report')  # Redirect to the same page to show the success message
        else:
            messages.error(request, "There was an error submitting your report. Please try again.")
    else:
        form = PoliceReportForm()

    return render(request, 'reports/submit_report.html', {'form': form})