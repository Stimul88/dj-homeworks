import pytest
from django.urls import reverse

from students.filters import CourseFilter
from students.models import Course, Student


def test_example():
    assert True, "Just test example"


@pytest.mark.django_db
def test_get_course(client):
    # Arrange
    Course.objects.create(id=1, name='Python')

    # Act
    response = client.get('/api/v1/courses/')

    # Assert
    assert response.status_code == 200
    data = response.json()
    assert len(data) == 1
    assert data[0]['name'] == 'Python'


@pytest.mark.django_db
def test_get_list_course(client, course_factory):
    # Arrange
    course = course_factory(_quantity=10)

    # Act
    response = client.get('/api/v1/courses/')

    # Assert
    assert response.status_code == 200
    data = response.json()
    assert len(data) == len(course)
    for i, c in enumerate(data):
        assert c['name'] == course[i].name


@pytest.mark.django_db
def test_filter_id_course(client, course_factory):
    # Arrange
    course = course_factory(_quantity=10)

    # Act
    for i, j in enumerate(course):
        data = {'id': j.id}
        response = client.get('/api/v1/courses/', data=data)
        # Assert
        assert response.status_code == 200
        res = response.json()
        assert j.id == res[0].get('id')


@pytest.mark.django_db
def test_filter_name_course(client, course_factory):
    # Arrange
    course = course_factory(_quantity=10)

    # Act
    for i, j in enumerate(course):
        data = {'name': j.name}
        response = client.get('/api/v1/courses/', data=data)
        # Assert
        assert response.status_code == 200
        res = response.json()
        assert j.name == res[0].get('name')


@pytest.mark.django_db
def test_create_course(client):
    data = {'name': 'Python'}
    response = client.post('/api/v1/courses/', data=data)

    assert response.status_code == 201


@pytest.mark.django_db
def test_update_course(client, course_factory):
    course = course_factory(name="Социолгия")
    url = reverse("courses-detail", args=(course.id,))
    data = {'name': 'Python'}
    response = client.patch(url, data)

    assert response.status_code == 200


@pytest.mark.django_db
def test_delete_course(client, course_factory):
    course = course_factory(name='Нетология')
    url = reverse("courses-detail", args=(course.id,))
    resp = client.delete(url)

    assert resp.status_code == 204
