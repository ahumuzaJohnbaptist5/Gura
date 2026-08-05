from django.shortcuts import render


def home(request):
    return render(request, "core/index.html") # <-- CORRECT


def about(request):
    return render(request, "core/about.html")

def how_it_works(request):
    return render(request, "core/how_it_works.html")

# ... (keep all your existing views) ...

def services_view(request):
    return render(request, 'core/services.html')

def providers_view(request):
    return render(request, 'core/providers.html')

def about_view(request):
    return render(request, 'core/about.html')

def contact_view(request):
    if request.method == 'POST':
        # Handle contact form submission
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')
        # In production, you would send an email or save to database
        return render(request, 'core/contact_success.html', {'name': name})
    return render(request, 'core/contact.html')

def contact_success_view(request):
    return render(request, 'core/contact_success.html')    