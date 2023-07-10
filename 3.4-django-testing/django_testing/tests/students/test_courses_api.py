import pytest
from django.urls import reverse
from students.models import Course


def test_example():
    assert True, "Just test example"


@pytest.mark.django_db
def test_get_course(client, url_factory, course_factory):
    # Arrange
    course = course_factory()

    # Act
    url = reverse("courses-detail", args=(course.id,))
    response = client.get(url)
    # Assert
    assert response.status_code == 200
    data = response.json()
    assert course.name == data.get('name')


@pytest.mark.django_db
def test_get_list_course(client, url_factory, course_factory):
    # Arrange
    course = course_factory(_quantity=10)

    # Act
    response = client.get(url_factory)

    # Assert
    assert response.status_code == 200
    data = response.json()
    assert len(data) == len(course)
    for i, c in enumerate(data):
        assert c['name'] == course[i].name


@pytest.mark.django_db
def test_filter_id_course(client, url_factory, course_factory):
    # Arrange
    course = course_factory(_quantity=10)

    # Act
    for i, j in enumerate(course):
        data = {'id': j.id}
        response = client.get(url_factory, data=data)
        # Assert
        assert response.status_code == 200
        res = response.json()
        assert j.id == res[0].get('id')


@pytest.mark.django_db
def test_filter_name_course(client, url_factory, course_factory):
    # Arrange
    course = course_factory(_quantity=10)

    # Act
    for i, j in enumerate(course):
        data = {'name': j.name}
        response = client.get(url_factory, data=data)
        # Assert
        assert response.status_code == 200
        res = response.json()
        assert j.name == res[0].get('name')


@pytest.mark.django_db
def test_create_course(client, url_factory):
    data = {'name': 'Python'}
    response = client.post(url_factory, data=data)
    # url = reverse("courses-detail", args=(course.id,))
    assert response.status_code == 201


@pytest.mark.django_db
def test_update_course(client, url_factory, course_factory):
    course = course_factory()
    url = reverse("courses-detail", args=(course.id,))
    response = client.patch(url)

    assert response.status_code == 200


@pytest.mark.django_db
def test_delete_course(client, url_factory, course_factory):
    course = course_factory()
    url = reverse("courses-detail", args=(course.id,))
    response = client.delete(url)

    assert response.status_code == 204
