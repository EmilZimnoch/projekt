import pytest
from django.contrib.auth.models import User, Permission

from accounts.models import CustomUser
from strona.models import Service, Spot, Smart, TypeOfSpot, Room


@pytest.fixture
def user():
    #    p = Permission.objects.get(codename='add_service')
    u = CustomUser.objects.create(username='testowy', email='testowy@testowy.testowy')
    #    u.user_permissions.add(p)
    return u


@pytest.fixture
def services():
    lst = []
    for x in range(10):
        lst.append(Service.objects.create(name=x, square_meters=x))
    return lst


@pytest.fixture
def service():
    service = Service.objects.create(name='x', square_meters='150m2')
    return service


@pytest.fixture
def rooms(services):
    lst = []
    for x in range(10):
        lst.append(Room.objects.create(name=x, service=services[x]))
    return lst


@pytest.fixture
def room(service):
    room = Room.objects.create(name='Garaż', service=service)
    return room


@pytest.fixture
def smarts():
    lst = []
    for x in range(10):
        lst.append(Smart.objects.create(name=x, description=x))
    return lst


@pytest.fixture
def smart(service):
    smart = Smart.objects.create(name='x', description='x')
    smart.smart.add(service)
    return smart


@pytest.fixture
def typeofspots():
    lst = []
    for x in range(10):
        lst.append(TypeOfSpot.objects.create(wall_type=x, description=x))
    return lst


@pytest.fixture
def typeofspot():
    typeofspot = TypeOfSpot.objects.create(wall_type='x', description='x')
    return typeofspot


@pytest.fixture
def spots(typeofspot, room):
    lst = []
    for x in range(10):
        lst.append(Spot.objects.create(type=typeofspot, room=room, furrowing=x))
    return lst


@pytest.fixture
def spot(service, room, typeofspot):
    spot = Spot.objects.create(type=typeofspot, room=room, furrowing='x')
    return spot


@pytest.fixture
def add_service(x):
    return Service.objects.create(name=x, square_meters=x)


# @pytest.fixture
# def add_room(x, service):
#     return Room.objects.create(name=x, service=service)


# @pytest.fixture
# def add_smart(x):
#     return Smart.objects.create(name=x, description=x, smart=x)
#
#
# @pytest.fixture
# def add_typeofspot(x):
#     return TypeOfSpot.objects.create(wall_type=x, description=x)
#
#
# @pytest.fixture
# def add_spot(typeofspot, room, x):
#     return Spot.objects.create(type=typeofspot, room=room, furrowing=x)
