import pytest
from django.contrib.auth.models import User
from django.test import TestCase, Client
from django.urls import reverse

from accounts.models import CustomUser
from strona.models import Service, Room, Smart, TypeOfSpot, Spot


@pytest.mark.django_db
def test_user_create(user):
    count = CustomUser.objects.all().count()
    print(count)
    assert CustomUser.objects.count() == 1


@pytest.mark.django_db
def test_get_main_view():
    client = Client()
    response = client.get(reverse("home"))
    assert response.status_code == 200


@pytest.mark.django_db
def test_get_contact_view_no_login():
    client = Client()
    response = client.get(reverse("contact"))
    assert response.status_code == 200


@pytest.mark.django_db
def test_get_contact_view(user):
    client = Client()
    client.force_login(user)
    response = client.get(reverse("contact"))
    assert response.status_code == 200


@pytest.mark.django_db
def test_get_service_view_no_login():
    client = Client()
    response = client.get(reverse("service_list_view"))
    assert response.status_code == 302


@pytest.mark.django_db
def test_get_service_view(services, user):
    client = Client()
    client.force_login(user)
    response = client.get(reverse("service_list_view"))
    assert response.status_code == 200
    service_list = response.context['object_list']
    assert service_list.count() == len(services)
    for service in services:
        assert service in service_list


@pytest.mark.django_db
def test_get_room_view_no_login():
    client = Client()
    response = client.get(reverse("room_list_view"))
    assert response.status_code == 302


@pytest.mark.django_db
def test_get_room_view(rooms, user):
    client = Client()
    client.force_login(user)
    response = client.get(reverse("room_list_view"))
    assert response.status_code == 200
    room_list = response.context['object_list']
    assert room_list.count() == len(rooms)
    for room in rooms:
        assert room in room_list


@pytest.mark.django_db
def test_get_smart_view_no_login():
    client = Client()
    response = client.get(reverse("smart_list_view"))
    assert response.status_code == 302


@pytest.mark.django_db
def test_get_smart_view(smarts, user):
    client = Client()
    client.force_login(user)
    response = client.get(reverse("smart_list_view"))
    assert response.status_code == 200
    smart_list = response.context['object_list']
    assert smart_list.count() == len(smarts)
    for item in smarts:
        assert item in smart_list


@pytest.mark.django_db
def test_get_typeofspot_view_no_login():
    client = Client()
    response = client.get(reverse("typeofspot_list_view"))
    assert response.status_code == 302


@pytest.mark.django_db
def test_get_typeofspot_view(typeofspots, user):
    client = Client()
    client.force_login(user)
    response = client.get(reverse("typeofspot_list_view"))
    assert response.status_code == 200
    typeofspot_list = response.context['object_list']
    assert typeofspot_list.count() == len(typeofspots)
    for typeofspot in typeofspots:
        assert typeofspot in typeofspot_list


@pytest.mark.django_db
def test_get_spot_view_no_login():
    client = Client()
    response = client.get(reverse("spot_list_view"))
    assert response.status_code == 302


@pytest.mark.django_db
def test_get_service_view(spots, user):
    client = Client()
    client.force_login(user)
    response = client.get(reverse("spot_list_view"))
    assert response.status_code == 200
    spot_list = response.context['object_list']
    assert spot_list.count() == len(spots)
    for spot in spots:
        assert spot in spot_list


@pytest.mark.django_db
def test_get_detail_service_view_no_login(service):
    client = Client()
    response = client.get(reverse("detail_service_view", args=(service.pk,)))
    assert response.status_code == 302


@pytest.mark.django_db
def test_get_detail_service_view(service, user):
    client = Client()
    client.force_login(user)
    response = client.get(reverse("detail_service_view", args=(service.pk,)))
    assert response.status_code == 200


@pytest.mark.django_db
def test_get_room_detail_view(room, user):
    client = Client()
    client.force_login(user)
    response = client.get(reverse("room_detail_view", args=(room.pk,)))
    assert response.status_code == 200


@pytest.mark.django_db
def test_get_room_detail_view_no_login(room):
    client = Client()
    response = client.get(reverse("room_detail_view", args=(room.pk,)))
    assert response.status_code == 302


@pytest.mark.django_db
def test_get_smart_detail_view(smart, user):
    client = Client()
    client.force_login(user)
    response = client.get(reverse("smart_detail_view", args=(smart.pk,)))
    assert response.status_code == 200


@pytest.mark.django_db
def test_get_smart_detail_view_no_login(smart):
    client = Client()
    response = client.get(reverse("smart_detail_view", args=(smart.pk,)))
    assert response.status_code == 302


@pytest.mark.django_db
def test_get_typeofspot_detail_view(typeofspots, user):
    client = Client()
    client.force_login(user)
    response = client.get(reverse("typeofspot_detail_view", kwargs={'pk': typeofspots[0].pk}))
    assert response.status_code == 200


@pytest.mark.django_db
def test_get_typeofspot_detail_view_no_login(typeofspots):
    client = Client()
    response = client.get(reverse("typeofspot_detail_view", kwargs={'pk': typeofspots[0].pk}))
    assert response.status_code == 302


@pytest.mark.django_db
def test_get_spot_detail_view(spot, user):
    client = Client()
    client.force_login(user)
    response = client.get(reverse("spot_detail_view", args=(spot.pk,)))
    assert response.status_code == 200


@pytest.mark.django_db
def test_get_spot_detail_view_no_login(spot):
    client = Client()
    response = client.get(reverse("spot_detail_view", args=(spot.pk,)))
    assert response.status_code == 302


@pytest.mark.django_db
def test_get_service_add_view_no_login():
    client = Client()
    response = client.get(reverse("service_add_view"))
    assert response.status_code == 302


@pytest.mark.django_db
def test_get_service_add_view(user):
    client = Client()
    client.force_login(user)
    response = client.get(reverse("service_add_view"))
    assert response.status_code == 200


@pytest.mark.django_db
def test_post_service_add_view(user):
    client = Client()
    client.force_login(user)
    a = {
        'name': 'testService',
        'square_meters': '50m2'
    }
    response = client.post(reverse("service_add_view"), data=a)
    assert response.status_code == 302
    Service.objects.get(**a)


@pytest.mark.django_db
def test_get_room_add_view_no_login():
    client = Client()
    response = client.get(reverse("room_add_view"))
    assert response.status_code == 302


@pytest.mark.django_db
def test_get_room_add_view(user):
    client = Client()
    client.force_login(user)
    response = client.get(reverse("room_add_view"))
    assert response.status_code == 200


@pytest.mark.django_db
def test_post_room_add_view(service, user):
    client = Client()
    client.force_login(user)
    a = {
        'name': 'Garaż',
        'service': service.pk
    }
    response = client.post(reverse("room_add_view"), data=a)
    assert response.status_code == 302
    Room.objects.get(**a)


@pytest.mark.django_db
def test_get_smart_add_view_no_login():
    client = Client()
    response = client.get(reverse("smart_add_view"))
    assert response.status_code == 302


@pytest.mark.django_db
def test_get_smart_add_view(user):
    client = Client()
    client.force_login(user)
    response = client.get(reverse("smart_add_view"))
    assert response.status_code == 200


@pytest.mark.django_db
def test_post_smart_add_view(service, user):
    client = Client()
    client.force_login(user)
    a = {
        'name': 'testService',
        'description': 'testService',
        'smart': service.pk
    }
    response = client.post(reverse("smart_add_view"), data=a)
    assert response.status_code == 302
    Smart.objects.get(**a)


@pytest.mark.django_db
def test_get_typefospot_add_view_no_login():
    client = Client()
    response = client.get(reverse("typeofspot_add_view"))
    assert response.status_code == 302


@pytest.mark.django_db
def test_get_typefospot_add_view(user):
    client = Client()
    client.force_login(user)
    response = client.get(reverse("typeofspot_add_view"))
    assert response.status_code == 200


@pytest.mark.django_db
def test_post_typeofspot_add_view(user):
    client = Client()
    client.force_login(user)
    a = {
        'wall_type': 'pustak',
        'description': 'testService'
    }
    response = client.post(reverse("typeofspot_add_view"), data=a)
    assert response.status_code == 302
    TypeOfSpot.objects.get(**a)


@pytest.mark.django_db
def test_get_spot_add_view_no_login():
    client = Client()
    response = client.get(reverse("spot_add_view"))
    assert response.status_code == 302


@pytest.mark.django_db
def test_get_spot_add_view(user):
    client = Client()
    client.force_login(user)
    response = client.get(reverse("spot_add_view"))
    assert response.status_code == 200


@pytest.mark.django_db
def test_post_spot_add_view(typeofspot, room, user):
    client = Client()
    client.force_login(user)
    a = {
        'type': typeofspot.pk,
        'room': room.pk,
        'furrowing': 'pustak'
    }
    response = client.post(reverse("spot_add_view"), data=a)
    assert response.status_code == 302
    Spot.objects.get(**a)


@pytest.mark.django_db
def test_get_service_delete_view_no_login(service):
    client = Client()
    response = client.get(reverse("service_delete_view", args=(service.pk,)))
    assert response.status_code == 302


@pytest.mark.django_db
def test_get_service_delete_view(service, user):
    client = Client()
    client.force_login(user)
    response = client.get(reverse("service_delete_view", args=(service.pk,)))
    assert response.status_code == 200


@pytest.mark.django_db
def test_post_service_delete_view(service, user):
    client = Client()
    client.force_login(user)
    response = client.post(reverse("service_delete_view", args=(service.pk,)))
    assert response.status_code == 302
    with pytest.raises(Service.DoesNotExist):
        Service.objects.get(id=service.pk)


@pytest.mark.django_db
def test_get_room_delete_view_no_login(room):
    client = Client()
    response = client.get(reverse("room_delete_view", args=(room.pk,)))
    assert response.status_code == 302


@pytest.mark.django_db
def test_get_room_delete_view(room, user):
    client = Client()
    client.force_login(user)
    response = client.get(reverse("room_delete_view", args=(room.pk,)))
    assert response.status_code == 200


@pytest.mark.django_db
def test_post_room_delete_view(room, user):
    client = Client()
    client.force_login(user)
    response = client.post(reverse("room_delete_view", args=(room.pk,)))
    assert response.status_code == 302
    with pytest.raises(Room.DoesNotExist):
        Room.objects.get(id=room.pk)


@pytest.mark.django_db
def test_get_smart_delete_view_no_login(smart):
    client = Client()
    response = client.get(reverse("smart_delete_view", args=(smart.pk,)))
    assert response.status_code == 302


@pytest.mark.django_db
def test_get_smart_delete_view(smart, user):
    client = Client()
    client.force_login(user)
    response = client.get(reverse("smart_delete_view", args=(smart.pk,)))
    assert response.status_code == 200


@pytest.mark.django_db
def test_post_smart_delete_view(smart, user):
    client = Client()
    client.force_login(user)
    response = client.post(reverse("smart_delete_view", args=(smart.pk,)))
    assert response.status_code == 302
    with pytest.raises(Smart.DoesNotExist):
        Smart.objects.get(id=smart.pk)


@pytest.mark.django_db
def test_get_typeofspot_delete_view_no_login(typeofspot):
    client = Client()
    response = client.get(reverse("typeofspot_delete_view", args=(typeofspot.pk,)))
    assert response.status_code == 302


@pytest.mark.django_db
def test_get_typeofspot_delete_view(typeofspot, user):
    client = Client()
    client.force_login(user)
    response = client.get(reverse("typeofspot_delete_view", args=(typeofspot.pk,)))
    assert response.status_code == 200


@pytest.mark.django_db
def test_post_typeofspot_delete_view(typeofspot, user):
    client = Client()
    client.force_login(user)
    response = client.post(reverse("typeofspot_delete_view", args=(typeofspot.pk,)))
    assert response.status_code == 302
    with pytest.raises(TypeOfSpot.DoesNotExist):
        TypeOfSpot.objects.get(id=typeofspot.pk)


@pytest.mark.django_db
def test_get_spot_delete_view_no_login(spot):
    client = Client()
    response = client.get(reverse("spot_delete_view", args=(spot.pk,)))
    assert response.status_code == 302


@pytest.mark.django_db
def test_get_spot_delete_view(spot, user):
    client = Client()
    client.force_login(user)
    response = client.get(reverse("spot_delete_view", args=(spot.pk,)))
    assert response.status_code == 200


@pytest.mark.django_db
def test_post_spot_delete_view(spot, user):
    client = Client()
    client.force_login(user)
    response = client.post(reverse("spot_delete_view", args=(spot.pk,)))
    assert response.status_code == 302
    with pytest.raises(Spot.DoesNotExist):
        Spot.objects.get(id=spot.pk)


@pytest.mark.django_db
def test_get_service_update_view_no_login(service):
    client = Client()
    response = client.get(reverse("service_update_view", args=(service.pk,)))
    assert response.status_code == 302


@pytest.mark.django_db
def test_get_service_update_view(service, user):
    client = Client()
    client.force_login(user)
    response = client.get(reverse("service_update_view", args=(service.pk,)))
    assert response.status_code == 200


@pytest.mark.django_db
def test_post_service_update_view(user):
    client = Client()
    client.force_login(user)
    a = {
        'name': 'testService',
        'square_meters': '100m2'
    }
    response = client.post(reverse("service_add_view"), data=a)
    assert response.status_code == 302
    assert Service.objects.get(**a).name == "testService"
    assert Service.objects.get(**a).square_meters == "100m2"


@pytest.mark.django_db
def test_get_room_update_view_no_login(room):
    client = Client()
    response = client.get(reverse("room_update_view", args=(room.pk,)))
    assert response.status_code == 302


@pytest.mark.django_db
def test_get_room_update_view(room, user):
    client = Client()
    client.force_login(user)
    response = client.get(reverse("room_update_view", args=(room.pk,)))
    assert response.status_code == 200


@pytest.mark.django_db
def test_post_room_update_view(service, user):
    client = Client()
    client.force_login(user)
    a = {
        'name': 'Garaż',
        'service': service.pk
    }
    response = client.post(reverse("room_add_view"), data=a)
    assert response.status_code == 302
    assert Room.objects.get(**a).name == "Garaż"
    assert Room.objects.get(**a).service == service


@pytest.mark.django_db
def test_get_smart_update_view_no_login(smart):
    client = Client()
    response = client.get(reverse("smart_update_view", args=(smart.pk,)))
    assert response.status_code == 302


@pytest.mark.django_db
def test_get_smart_update_view(smart, user):
    client = Client()
    client.force_login(user)
    response = client.get(reverse("smart_update_view", args=(smart.pk,)))
    assert response.status_code == 200


@pytest.mark.django_db
def test_post_smart_update_view(service, user):
    client = Client()
    client.force_login(user)
    a = {
        'name': 'testService',
        'description': 'testService',
        'smart': service.pk
    }
    response = client.post(reverse("smart_add_view"), data=a)
    assert response.status_code == 302
    assert Smart.objects.get(**a).name == "testService"
    assert Smart.objects.get(**a).description == "testService"
    assert service in Smart.objects.get(**a).smart.all()


@pytest.mark.django_db
def test_get_typeofspot_update_view_no_login(typeofspot):
    client = Client()
    response = client.get(reverse("typeofspot_update_view", args=(typeofspot.pk,)))
    assert response.status_code == 302


@pytest.mark.django_db
def test_get_typeofspot_update_view(typeofspot, user):
    client = Client()
    client.force_login(user)
    response = client.get(reverse("typeofspot_update_view", args=(typeofspot.pk,)))
    assert response.status_code == 200


@pytest.mark.django_db
def test_post_typeofspot_update_view(user):
    client = Client()
    client.force_login(user)
    a = {
        'wall_type': 'drewno',
        'description': 'testService'
    }
    response = client.post(reverse("typeofspot_add_view"), data=a)
    assert response.status_code == 302
    assert TypeOfSpot.objects.get(**a).wall_type == "drewno"
    assert TypeOfSpot.objects.get(**a).description == "testService"


@pytest.mark.django_db
def test_get_spot_update_view_no_login(spot):
    client = Client()
    response = client.get(reverse("spot_update_view", args=(spot.pk,)))
    assert response.status_code == 302


@pytest.mark.django_db
def test_get_spot_update_view(spot, user):
    client = Client()
    client.force_login(user)
    response = client.get(reverse("spot_update_view", args=(spot.pk,)))
    assert response.status_code == 200


@pytest.mark.django_db
def test_post_spot_update_view(typeofspot, room, user):
    client = Client()
    client.force_login(user)
    a = {
        'type': typeofspot.pk,
        'room': room.pk,
        'furrowing': 'drewno'
    }
    response = client.post(reverse("spot_add_view"), data=a)
    assert response.status_code == 302
    assert Spot.objects.get(**a).type == typeofspot
    assert Spot.objects.get(**a).room == room
    assert Spot.objects.get(**a).furrowing == "drewno"


@pytest.mark.django_db
def test_post_sign_up_view():
    client = Client()
    a = {
        'username': 'testuser',
        'email': 'qwerty@qwerty.com',
        'password1': 'poiuytre1',
        'password2': 'poiuytre1'
    }
    response = client.post(reverse("signup"), data=a)
    assert response.status_code == 302
    CustomUser.objects.get(username='testuser')


@pytest.mark.django_db
def test_get_sign_up(user):
    client = Client()
    client.force_login(user)
    response = client.get(reverse("signup"))
    assert response.status_code == 200


@pytest.mark.django_db
def test_get_sign_up_view():
    client = Client()
    response = client.get(reverse("signup"))
    assert response.status_code == 200