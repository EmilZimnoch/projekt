from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.db import models
from django.urls import reverse

# Create your models here.
ROOMS = (
    ('Kuchnia', 'kitchen'),
    ('Salon', 'living room'),
    ('Pokój', 'room'),
    ('Garaż', 'garage'),
    ('Przedpokój', 'hall'),
    ('Jadalnia', 'dining room'),
    ('Garderoba', 'walk-in wardrobe'),
    ('Spiżarnia', 'pantry'),
    ('Główna sypialnia', 'master bedroom'),
    ('Klatka schodowa', 'staircase'),
    ('Piwnica', 'basement'),
    ('Łazienka', 'bathroom')
)

METERS = (
    ('50m2', '50'),
    ('100m2', '100'),
    ('150m2', '150'),
    ('200m2', '200'),
    ('250m2', '250'),
    ('300m2', '300'),
    ('>300m2', '>300')
)


class Service(models.Model):
    name = models.CharField(max_length=125)
    square_meters = models.CharField(choices=METERS, max_length=6, default='')

#    rooms = models.CharField(choices=ROOMS, max_length=25, default='salon')
#    price = models.IntegerField()
    #room_set   //przylad s.room_set.all() -> Room.objects.filter(service=s)


    def get_absolute_url(self):
        return reverse('detail_service_view', args=(self.pk,))

    def get_delete_url(self):
        return reverse('service_delete_view', args=(self.pk,))

    def get_update_url(self):
        return reverse('service_update_view', args=(self.pk,))

    def __str__(self):
        return f"{self.name}  Powierzchnia: {self.square_meters}"



class Room(models.Model):
    name = models.CharField(choices=ROOMS, max_length=25, default='')
    service = models.ForeignKey(Service, on_delete=models.CASCADE)

    def get_absolute_url(self):
        return reverse('room_detail_view', args=(self.pk,))

    def get_delete_url(self):
        return reverse('room_delete_view', args=(self.pk,))

    def get_update_url(self):
        return reverse('room_update_view', args=(self.pk,))

    def __str__(self):
        return f"{self.name} Usługa:{self.service}"



class Smart(models.Model):
    name = models.CharField(max_length=256)
    description = models.TextField()
    smart = models.ManyToManyField(Service, null=True, blank=True)

    def get_absolute_url(self):
        return reverse('smart_detail_view', args=(self.pk,))

    def get_delete_url(self):
        return reverse('smart_delete_view', args=(self.pk,))

    def get_update_url(self):
        return reverse('smart_update_view', args=(self.pk,))

    def __str__(self):
        return f"{self.name} Usługa:{self.smart}"

TYPE_OF_WALL = (
    ('płyta karton-gips', 'plasterboard'),
    ('beton', 'concrete'),
    ('pustak', 'airbrick'),
    ('cegła', 'brick'),
    ('drewno', 'wood')
)


class TypeOfSpot(models.Model):
    wall_type = models.CharField(choices=TYPE_OF_WALL, max_length=20)
    description = models.TextField()

    def get_absolute_url(self):
        return reverse('typeofspot_detail_view', args=(self.pk,))

    def get_delete_url(self):
        return reverse('typeofspot_delete_view', args=(self.pk,))

    def get_update_url(self):
        return reverse('typeofspot_update_view', args=(self.pk,))

    def __str__(self):
        return f"{self.wall_type} Opis punktu:{self.description}"

#class Furrowing(models.Model):
#    wall_type = models.CharField(choices=TYPE_OF_WALL, max_length=2, default='PK')
#    price = models.IntegerField()


class Spot(models.Model):
    type = models.ForeignKey(TypeOfSpot, on_delete=models.CASCADE)
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    furrowing = models.CharField(choices=TYPE_OF_WALL, max_length=20)

    def get_absolute_url(self):
        return reverse('spot_detail_view', args=(self.pk,))

    def get_delete_url(self):
        return reverse('spot_delete_view', args=(self.pk,))

    def get_update_url(self):
        return reverse('spot_update_view', args=(self.pk,))

    def __str__(self):
        return f"{self.type} Pomieszczenie:{self.room}"