# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect

# Create your views here.

def index(request):
    return render(request, 'index.html')

def buy(request):
    print request.POST['id']
    print request.POST['num']
    if 'totalnum' not in request.session:
        request.session['totalnum'] = 0
        request.session['totalsum'] = 0
    if request.POST['id'] == '101':
        request.session['totalnum'] += int(request.POST['num'])
        new_charge = 19.99 * int(request.POST['num'])
        request.session['totalsum'] += new_charge
        request.session['charge'] = new_charge
        request.session['item'] = 'Dojo Tshirt'
    if request.POST['id'] == '102':
        request.session['totalnum'] += int(request.POST['num'])
        new_charge = 29.99 * int(request.POST['num'])
        request.session['totalsum'] += new_charge
        request.session['charge'] = new_charge
        request.session['item'] = 'Dojo Sweater'
    if request.POST['id'] == '103':
        request.session['totalnum'] += int(request.POST['num'])
        new_charge = 4.99 * int(request.POST['num'])
        request.session['totalsum'] += new_charge
        request.session['charge'] = new_charge
        request.session['item'] = 'Dojo Cup'
    if request.POST['id'] == '104':
        request.session['totalnum'] += int(request.POST['num'])
        new_charge = 49.99 * int(request.POST['num'])
        request.session['totalsum'] += new_charge
        request.session['charge'] = new_charge
        request.session['item'] = 'Algorithm Book'
    return redirect('/checkout')

def checkout(request):
    return render(request,'checkout.html')