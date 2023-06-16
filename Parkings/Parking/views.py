from django.shortcuts import render
from django.http import HttpResponse 
from django.contrib.auth import login
from django.shortcuts import render, redirect
from django.shortcuts import render, redirect
from .forms import LoginForm, RegistrationForm, ReservationParkingForm
from time import sleep
import qrcode
import os
from PIL import Image
from django.conf import settings
from django.urls import reverse
from django.contrib.auth import authenticate, login
from .forms import LoginForm



def my_viewA(request):
    context = {'name': 'accueil'}  # A context dictionary with values for the template
    return render(request, 'accueil.html', context)
def my_viewB(request):
    context = {'name': 'reservation'}  # A context dictionary with values for the template
    return render(request, 'reservation.html', context)
# views.py

def my_viewC(request):
    if request.method == 'POST':
        form = LoginForm(data=request.POST)
        if form.is_valid():
            user = authenticate(request, username=form.cleaned_data['username'], password=form.cleaned_data['password'])
            if user is not None:
                login(request, user)
                return redirect('reservation')  # Redirect to the desired page after successful login
    else:
        form = LoginForm()
    return render(request, 'Connexion.html', {'form': form})


def my_viewD(request):
    context = {'name': 'Tarifs'}  # A context dictionary with values for the template
    return render(request, 'tarifs.html', context)
def my_viewE(request):
    context = {'name': 'Contact'}  # A context dictionary with values for the template
    return render(request, 'contact.html', context)
def my_viewF(request):
    context = {'name': 'Enregistrer'}  # A context dictionary with values for the template
    return render(request, 'enregistrer.html', context)
# views.py

def my_viewG(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('Connexion')  # Redirect to the desired page after successful registration
    else:
        form = RegistrationForm()
    return render(request, 'enregistrer.html', {'form': form})
from django.shortcuts import render, redirect
from .forms import ReservationParkingForm


# ... Existing code ...

def my_viewB(request):
    if request.method == 'POST':
        form = ReservationParkingForm(request.POST)
        if form.is_valid():
            reservation = form.save(commit=False)
            reservation.user = request.user  # Assign the current user to the reservation
            reservation.save()
            return redirect('paiement')  # Redirect to a success page
    else:
        form = ReservationParkingForm()
    return render(request, 'reservation.html', {'form': form})



def process_payment(amount, card_number, expiration_date, cvv):
    # Simulate payment processing time
    sleep(2)
    # Add logic for handling the payment (e.g., connecting to a payment gateway)
    return True  # Return True to indicate successful payment
def my_viewJ(request):
    payment_success = request.session.get('my_viewJ', False)
    
    if payment_success:
        qr_code_data = "Your QR code data"  # Replace with your QR code data
        qr_code_img = generate_qr_code(qr_code_data)
        return render(request, 'success.html', {'my_viewJ': True, 'qr_code_img': qr_code_img})
    else:
        return render(request, 'success.html', {'my_viewJ': False})


def my_viewI(request):
    if request.method == 'POST':
        amount = float(request.POST.get('amount'))
        card_number = request.POST.get('card_number')
        expiration_date = request.POST.get('expiration_date')
        cvv = request.POST.get('cvv')

        request.session['payment_in_progress'] = True
        sleep(1)

        if len(card_number) == 16 and len(expiration_date) == 5 and len(cvv) == 3:
            success = process_payment(amount, card_number, expiration_date, cvv)
            if success:
                qr_code_img = generate_qr_code_with_cvv(cvv)
                request.session['my_viewJ'] = True
                return render(request, 'success.html', {'my_viewJ': True, 'qr_code_img': qr_code_img})
            else:
                request.session['my_viewJ'] = False
        else:
            request.session['my_viewJ'] = False

    return render(request, 'paiement.html')


def generate_qr_code(data):
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(data)
    qr.make(fit=True)
    qr_code_img = qr.make_image(fill_color="black", back_color="white")

    image_path = os.path.join(settings.MEDIA_ROOT, 'qr_code.png')
    qr_code_img.save(image_path)

    image_url = os.path.join(settings.MEDIA_URL, 'qr_code.png')
    return image_url

def generate_qr_code_with_cvv(cvv):
    qr_code_data = f"Your QR code data with CVV: {cvv}"
    return generate_qr_code(qr_code_data)
