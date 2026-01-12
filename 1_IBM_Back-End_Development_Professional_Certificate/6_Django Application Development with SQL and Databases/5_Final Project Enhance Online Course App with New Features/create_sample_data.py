import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mysite.settings')
django.setup()

from django.contrib.auth.models import User
from courses.models import Instructor, Course, Lesson, Question, Choice
from datetime import date

# Create instructor
admin_user = User.objects.get(username='admin')
instructor, created = Instructor.objects.get_or_create(
    user=admin_user,
    defaults={'full_time': True, 'total_learners': 0}
)
print(f"Instructor created: {instructor}")

# Create a sample course
course, created = Course.objects.get_or_create(
    name='Introduction to Python Programming',
    defaults={
        'description': 'Learn Python programming from scratch. This course covers basic syntax, data structures, functions, and object-oriented programming.',
        'pub_date': date.today(),
        'total_enrollment': 0
    }
)
if created:
    course.instructors.add(instructor)
    print(f"Course created: {course.name}")
else:
    print(f"Course already exists: {course.name}")

# Create lessons
lessons_data = [
    {'title': 'Getting Started with Python', 'order': 1, 'content': 'In this lesson, you will learn how to install Python and write your first program.'},
    {'title': 'Variables and Data Types', 'order': 2, 'content': 'Learn about different data types in Python including strings, integers, floats, and booleans.'},
    {'title': 'Control Flow', 'order': 3, 'content': 'Understanding if statements, loops, and how to control the flow of your program.'},
]

for lesson_data in lessons_data:
    lesson, created = Lesson.objects.get_or_create(
        title=lesson_data['title'],
        course=course,
        defaults={'order': lesson_data['order'], 'content': lesson_data['content']}
    )
    if created:
        print(f"Lesson created: {lesson.title}")

# Create exam questions
questions_data = [
    {
        'content': 'What is the correct file extension for Python files?',
        'grade': 5,
        'choices': [
            {'content': '.pyth', 'is_correct': False},
            {'content': '.py', 'is_correct': True},
            {'content': '.pt', 'is_correct': False},
            {'content': '.python', 'is_correct': False},
        ]
    },
    {
        'content': 'Which of the following are valid Python data types? (Select all that apply)',
        'grade': 10,
        'choices': [
            {'content': 'int', 'is_correct': True},
            {'content': 'string', 'is_correct': False},
            {'content': 'str', 'is_correct': True},
            {'content': 'float', 'is_correct': True},
        ]
    },
    {
        'content': 'How do you start a comment in Python?',
        'grade': 5,
        'choices': [
            {'content': '//', 'is_correct': False},
            {'content': '#', 'is_correct': True},
            {'content': '/*', 'is_correct': False},
            {'content': '--', 'is_correct': False},
        ]
    },
]

for q_data in questions_data:
    question, created = Question.objects.get_or_create(
        content=q_data['content'],
        course=course,
        defaults={'grade': q_data['grade']}
    )
    
    if created:
        print(f"Question created: {question.content}")
        for choice_data in q_data['choices']:
            Choice.objects.create(
                question=question,
                content=choice_data['content'],
                is_correct=choice_data['is_correct']
            )

print("\n✅ Sample data created successfully!")
print(f"Course: {course.name}")
print(f"Lessons: {course.lesson_set.count()}")
print(f"Questions: {course.question_set.count()}")
