from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.http import HttpResponse
from datetime import datetime
from django.views import View
from django.contrib import messages
from django.views.generic import *
from strona.models import TypeOfSpot, Spot, Smart, Service, Room
from strona.forms import ServiceModelForm, RoomModelForm, SmartModelForm, TypeOfSpotModelForm, SpotModelForm


# Create your views here.

class IndexView(View):

    def get(self, request):
        response = render(request, 'login.html')
        return response


class ServiceView(LoginRequiredMixin, View):
    def get(self, request):
        services = Service.objects.all()
        response = render(request, 'service.html', {'service': services})
        return response


class DetailServiceView(LoginRequiredMixin, DetailView):
    model = Service
    template_name = 'detail_service.html'


class RoomView(LoginRequiredMixin, ListView):
    model = Room
    template_name = 'room.html'


class ContactView(View):

    def get(self, request):
        response = render(request, 'contact.html')
        return response


class ServiceAddView(LoginRequiredMixin, CreateView):
    model = Service
    template_name = 'form.html'
    form_class = ServiceModelForm


#    success_url = 'service_list_view'


class ServiceDeleteView(LoginRequiredMixin, DeleteView):
    model = Service
    success_url = '/services/'
    template_name = 'form.html'


class ServiceUpdateView(LoginRequiredMixin, UpdateView):
    model = Service
    template_name = 'form.html'
    # fields = '/square_meters/'
    form_class = ServiceModelForm
    success_url = '/services/'

    # def get(self, request, id):
    #     self.object = self.get_object()
    #     return super().get(request)


class RoomDetailView(LoginRequiredMixin, DetailView):
    model = Room
    template_name = 'room_detail.html'


class RoomAddView(LoginRequiredMixin, CreateView):
    model = Room
    template_name = 'form.html'
    form_class = RoomModelForm


class RoomDeleteView(LoginRequiredMixin, DeleteView):
    model = Room
    success_url = '/rooms/'
    template_name = 'form.html'


class SmartView(LoginRequiredMixin, ListView):
    model = Smart
    template_name = 'smart.html'


class SmartDetailView(LoginRequiredMixin, DetailView):
    model = Smart
    template_name = 'smart_detail.html'


class SmartAddView(LoginRequiredMixin, CreateView):
    model = Smart
    template_name = 'form.html'
    form_class = SmartModelForm


class SmartDeleteView(LoginRequiredMixin, DeleteView):
    model = Smart
    success_url = '/smarts/'
    template_name = 'form.html'


class TypeOfSpotView(LoginRequiredMixin, ListView):
    model = TypeOfSpot
    template_name = 'typeofspot.html'


class TypeOfSpotDetailView(LoginRequiredMixin, DetailView):
    model = TypeOfSpot
    template_name = 'typeofspot_detail.html'


class TypeOfSpotAddView(LoginRequiredMixin, CreateView):
    model = TypeOfSpot
    template_name = 'form.html'
    form_class = TypeOfSpotModelForm


class TypeOfSpotDeleteView(LoginRequiredMixin, DeleteView):
    model = TypeOfSpot
    success_url = '/typeofspots/'
    template_name = 'form.html'


class SpotView(LoginRequiredMixin, ListView):
    model = Spot
    template_name = 'spot.html'


class SpotDetailView(LoginRequiredMixin, DetailView):
    model = Spot
    template_name = 'spot_detail.html'


class SpotAddView(LoginRequiredMixin, CreateView):
    model = Spot
    template_name = 'form.html'
    form_class = SpotModelForm


class SpotDeleteView(LoginRequiredMixin, DeleteView):
    model = Spot
    success_url = '/spots/'
    template_name = 'form.html'


class RoomUpdateView(LoginRequiredMixin, UpdateView):
    model = Room
    template_name = 'form.html'
    form_class = RoomModelForm
    success_url = "/rooms/"


class SmartUpdateView(LoginRequiredMixin, UpdateView):
    model = Smart
    template_name = 'form.html'
    form_class = SmartModelForm
    success_url = "/smarts/"


class TypeOfSpotUpdateView(LoginRequiredMixin, UpdateView):
    model = TypeOfSpot
    template_name = 'form.html'
    form_class = TypeOfSpotModelForm
    success_url = "/typeofspots/"


class SpotUpdateView(LoginRequiredMixin, UpdateView):
    model = Spot
    template_name = 'form.html'
    form_class = SpotModelForm
    success_url = "/spots/"
