import os
import django
from datetime import date

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mysite.settings')
django.setup()

from django.contrib.auth.models import User
from courses.models import Instructor, Course, Lesson, Question, Choice

# Get admin user
admin_user = User.objects.get(username='admin')

# Add admin as an Instructor
instructor, created = Instructor.objects.get_or_create(
    user=admin_user,
    defaults={'full_time': True, 'total_learners': 0}
)
if created:
    print(f"✅ Instructor created: {instructor}")
else:
    print(f"ℹ️ Instructor already exists: {instructor}")

# Create Learning Django course
course, created = Course.objects.get_or_create(
    name='Learning Django',
    defaults={
        'description': 'Django is an extremely popular and fully featured server-side web framework, written in Python',
        'pub_date': date.today(),
        'total_enrollment': 0
    }
)

if created:
    course.instructors.add(instructor)
    print(f"✅ Course created: {course.name}")
else:
    print(f"ℹ️ Course already exists: {course.name}")

# Create Lesson #1
lesson, created = Lesson.objects.get_or_create(
    title='What is Django',
    course=course,
    defaults={
        'order': 0,
        'content': 'Django is a high-level Python web framework that encourages rapid development and clean, pragmatic design. Built by experienced developers, it takes care of much of the hassle of web development, so you can focus on writing your app without needing to reinvent the wheel. It is free and open source.'
    }
)
if created:
    print(f"✅ Lesson created: {lesson.title}")
else:
    print(f"ℹ️ Lesson already exists: {lesson.title}")

# Create Test Question
question, created = Question.objects.get_or_create(
    content='Is Django a Python framework',
    course=course,
    defaults={'grade': 100}
)

if created:
    print(f"✅ Question created: {question.content}")
    
    # Create Choice #1 - Yes (Correct)
    choice1 = Choice.objects.create(
        question=question,
        content='Yes',
        is_correct=True
    )
    print(f"✅ Choice created: {choice1.content} (Correct)")
    
    # Create Choice #2 - No (Incorrect)
    choice2 = Choice.objects.create(
        question=question,
        content='No',
        is_correct=False
    )
    print(f"✅ Choice created: {choice2.content} (Incorrect)")
else:
    print(f"ℹ️ Question already exists: {question.content}")

print("\n" + "="*50)
print("✅ TEST DATA CREATION COMPLETED!")
print("="*50)
print(f"\nCourse: {course.name}")
print(f"Instructor: {instructor.user.username}")
print(f"Lessons: {course.lesson_set.count()}")
print(f"Questions: {course.question_set.count()}")
print(f"Total Choices: {sum([q.choice_set.count() for q in course.question_set.all()])}")
print("\n🌐 Open the course front end at: http://127.0.0.1:8000/")
