# -*- coding: utf-8 -*-
import os
import random
from datetime import date

import django
import sys

# 导入项目配置
project_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(project_path)
os.environ['DJANGO_SETTINGS_MODULE'] = 'mysite.settings'
django.setup()

from ormdemo.models import Teacher, Course, Student, TeacherAssistant


def import_data():
    # 讲师数据 create
    Teacher.objects.create(nickname="Jack", introduction="Python工程师", fans=666)
    Teacher.objects.create(nickname="Allen", introduction="Java工程师", fans=123)
    Teacher.objects.create(nickname="Henry", introduction="Golang工程师", fans=881)

    # 课程数据 bulk_create
    data = [
        Course(title=f"Python系列教程{i}",
               teacher=Teacher.objects.get(nickname="Jack"),
               type=random.choice([0, 1, 2]),
               price=random.randint(200, 300),
               volume=random.randint(100, 10000),
               online=date(2018, 10, 1)
               )
        for i in range(1, 5)
    ]

    Course.objects.bulk_create(data)

    data = [
        Course(title=f"Java系列教程{i}",
               teacher=Teacher.objects.get(nickname="Allen"),
               type=random.choice([0, 1, 2]),
               price=random.randint(200, 300),
               volume=random.randint(100, 10000),
               online=date(2018, 10, 1)
               )
        for i in range(1, 5)
    ]

    Course.objects.bulk_create(data)

    data = [
        Course(title=f"Golang系列教程{i}",
               teacher=Teacher.objects.get(nickname="Henry"),
               type=random.choice([0, 1, 2]),
               price=random.randint(200, 300),
               volume=random.randint(100, 10000),
               online=date(2018, 10, 1)
               )
        for i in range(1, 5)
    ]

    Course.objects.bulk_create(data)

    # 学生数据 update_or_create
    Student.objects.update_or_create(
        nickname="A同学",
        defaults={
            "age": random.randint(18, 58),
            "gender": random.choice([0, 1, 2]),
            "study_time": random.randint(9, 999)
        }
    )

    Student.objects.update_or_create(
        nickname="B同学",
        defaults={
            "age": random.randint(18, 58),
            "gender": random.choice([0, 1, 2]),
            "study_time": random.randint(9, 999)
        }
    )

    Student.objects.update_or_create(
        nickname="C同学",
        defaults={
            "age": random.randint(18, 58),
            "gender": random.choice([0, 1, 2]),
            "study_time": random.randint(9, 999)
        }
    )

    Student.objects.update_or_create(
        nickname="D同学",
        defaults={
            "age": random.randint(18, 58),
            "gender": random.choice([0, 1, 2]),
            "study_time": random.randint(9, 999)
        }
    )

    # 正向添加
    # 销量大于等于1000的课程
    Student.objects.get(nickname="A同学").course.add(*Course.objects.filter(volume__gte=1000))
    # 销量大于500的课程
    Student.objects.get(nickname="B同学").course.add(*Course.objects.filter(volume__gt=500))

    # 反向添加
    # 学习时间大于等于500小时的同学
    Course.objects.get(title="Python系列教程1").student_set.add(*Student.objects.filter(
        study_time__gte=500
    ))

    # 学习时间小于等于500小时的同学
    Course.objects.get(title="Python系列教程1").student_set.add(*Student.objects.filter(
        study_time__lte=500
    ))

    # 助教数据 get_or_create()
    TeacherAssistant.objects.get_or_create(
        nickname="助教1",
        defaults={
            "hobby": "慕课网学习",
            "teacher": Teacher.objects.get(nickname="Jack")
        }
    )

    TeacherAssistant.objects.get_or_create(
        nickname="助教2",
        defaults={
            "hobby": "看书",
            "teacher": Teacher.objects.get(nickname="Allen")
        }
    )
    TeacherAssistant.objects.get_or_create(
        nickname="助教3",
        defaults={
            "hobby": "看电视",
            "teacher": Teacher.objects.get(nickname="Henry")
        }
    )


if __name__ == '__main__':
    import_data()
