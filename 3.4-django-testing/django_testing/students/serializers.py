from rest_framework import serializers

from students.models import Course, Student


class StudentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Student
        fields = ("name", "birth_date")

    def __str__(self):
        return self.name


class CourseSerializer(serializers.ModelSerializer):
    students = StudentSerializer(many=True)

    class Meta:
        model = Course
        fields = ("id", "name", "students")

    def __str__(self):
        return self.name

    def create(self, validated_data):
        # достаем связанные данные для других таблиц
        students = validated_data.pop('students')

        # создаем склад по его параметрам
        course = super().create(validated_data)
        # здесь вам надо заполнить связанные таблицы
        # в нашем случае: таблицу StockProduct
        # с помощью списка positions
        for stud in students:
            Course.objects.get_or_create(course=course, **stud)
        return course


