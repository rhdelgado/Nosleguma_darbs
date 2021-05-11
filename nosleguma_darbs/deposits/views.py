from django.shortcuts import render, HttpResponse, redirect

from django.views.generic import View, ListView, FormView
from deposits.forms import DepositForm
from deposits.models import Deposit


class AddDepositView(FormView):
    form_class = DepositForm
    template_name = 'form.html'
    success_url = '/'

    def form_valid(self, form):
        form.save()

        response = super().form_valid(form=form)
        return response

class DepositListView(ListView):
    model = Deposit
    template_name = 'index.html'

class DepositDetailView(FormView):
    form_class = DepositForm
    template_name = 'deposit.html'
