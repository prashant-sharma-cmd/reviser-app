from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, CreateView, UpdateView, DeleteView


class OwnerListView(LoginRequiredMixin, ListView):
    pass

class OwnerCreateView(LoginRequiredMixin, CreateView):
    pass

class OwnerUpdateView(LoginRequiredMixin, UpdateView):
    pass

class OwnerDeleteView(LoginRequiredMixin, DeleteView):
    pass