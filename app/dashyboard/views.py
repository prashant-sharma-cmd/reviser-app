from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import TemplateView, ListView, View, CreateView, \
    UpdateView, DeleteView

from .forms import CreateForm
from .models import Decks
from .owners import OwnerListView, OwnerDeleteView, OwnerUpdateView, \
    OwnerCreateView


class DeckListView(OwnerListView):
    model = Decks
    success_url = reverse_lazy('dashyboard:all')


class DeckCreateView(LoginRequiredMixin, View):
    template_name = 'dashyboard/decks_form.html'
    success_url = reverse_lazy('dashyboard:all')

    def get(self, request):
        form = CreateForm()
        ctx = {'form': form}
        return render(request, self.template_name, ctx)

    def post(self, request):
        form = CreateForm(request.POST)

        if not form.is_valid():
            ctx = {'form': form}
            return render(request, self.template_name, ctx)

        deck = form.save(commit=False)
        deck.owner = request.user
        deck.save()
        return redirect(self.success_url)


class DeckUpdateView(LoginRequiredMixin, View):
    template_name = 'dashyboard/decks_form.html'
    success_url = reverse_lazy('dashyboard:all')

    def get(self, request, pk):
        deck = get_object_or_404(Decks, pk=pk, owner=self.request.user)
        form = CreateForm(instance=deck)
        ctx = {'form': form}
        return render(request, self.template_name, ctx)

    def post(self, request, pk):
        deck = get_object_or_404(Decks, pk=pk, owner=self.request.user)
        form = CreateForm(request.POST, instance=deck)

        if not form.is_valid():
            ctx = {'form': form}
            return render(request, self.template_name, ctx)

        deck.save()
        return redirect(self.success_url)


class DeckDeleteView(OwnerDeleteView):
    model = Decks
    success_url = reverse_lazy('dashyboard:all')
