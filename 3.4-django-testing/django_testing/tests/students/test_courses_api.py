import pytest
from django.urls import reverse
from students.models import Course


def test_example():
    assert True, "Just test example"


@pytest.mark.django_db
def test_get_course(client):
    # Arrange
    Course.objects.create(id=1, name='Python')

    # Act
    response = client.get('/api/v1/courses/1/')

    # Assert
    assert response.status_code == 200
    data = response.json()
    assert data['id'] == 1


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
    # url = reverse("courses-detail", args=(course.id,))
    assert response.status_code == 201


@pytest.mark.django_db
def test_update_course(client, course_factory):
    course_factory(id=1, name="Социолгия")
    data = {'name': 'Python'}
    response = client.patch('/api/v1/courses/1/', data=data)

    assert response.status_code == 200


@pytest.mark.django_db
def test_delete_course(client, course_factory):
    course_factory(id=1, name='Нетология')
    response = client.delete('/api/v1/courses/1/')

    assert response.status_code == 204
