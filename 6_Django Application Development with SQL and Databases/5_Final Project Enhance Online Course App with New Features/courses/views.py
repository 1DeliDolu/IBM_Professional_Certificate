from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from django.views import generic
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, HttpResponse
import logging
from datetime import datetime
from .models import Course, Enrollment, Question, Choice, Submission

logger = logging.getLogger(__name__)


def registration_request(request):
    context = {}
    if request.method == 'GET':
        return render(request, 'courses/user_registration_bootstrap.html', context)
    elif request.method == 'POST':
        # Check if user exists
        username = request.POST['username']
        password = request.POST['psw']
        first_name = request.POST['firstname']
        last_name = request.POST['lastname']
        user_exist = False
        try:
            User.objects.get(username=username)
            user_exist = True
        except:
            logger.error("New user")
        if not user_exist:
            user = User.objects.create_user(username=username, first_name=first_name, last_name=last_name,
                                            password=password)
            login(request, user)
            return redirect("courses:index")
        else:
            context['message'] = "User already exists."
            return render(request, 'courses/user_registration_bootstrap.html', context)


def login_request(request):
    context = {}
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['psw']
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('courses:index')
        else:
            context['message'] = "Invalid username or password."
            return render(request, 'courses/user_login_bootstrap.html', context)
    else:
        return render(request, 'courses/user_login_bootstrap.html', context)


def logout_request(request):
    logout(request)
    return redirect('courses:index')


def check_if_enrolled(user, course):
    is_enrolled = False
    if user.id is not None:
        # Check if user enrolled
        num_results = Enrollment.objects.filter(user=user, course=course).count()
        if num_results > 0:
            is_enrolled = True
    return is_enrolled


class CourseListView(generic.ListView):
    template_name = 'courses/course_list_bootstrap.html'
    context_object_name = 'course_list'

    def get_queryset(self):
        user = self.request.user
        courses = Course.objects.order_by('-total_enrollment')[:10]
        for course in courses:
            if user.is_authenticated:
                course.is_enrolled = check_if_enrolled(user, course)
        return courses


class CourseDetailView(generic.DetailView):
    model = Course
    template_name = 'courses/course_detail_bootstrap.html'


@login_required
def enroll(request, course_id):
    course = get_object_or_404(Course, pk=course_id)
    user = request.user

    is_enrolled = check_if_enrolled(user, course)
    if not is_enrolled and user.is_authenticated:
        # Create an enrollment
        Enrollment.objects.create(user=user, course=course, mode='honor')
        course.total_enrollment += 1
        course.save()

    return HttpResponseRedirect(reverse(viewname='courses:course_details', args=(course.id,)))


@login_required
def submit(request, course_id):
    course = get_object_or_404(Course, pk=course_id)
    user = request.user
    
    # Check if user is enrolled, if not enroll them
    enrollment, created = Enrollment.objects.get_or_create(
        user=user, 
        course=course,
        defaults={'mode': 'honor'}
    )
    
    if created:
        course.total_enrollment += 1
        course.save()
    
    submission = Submission.objects.create(enrollment=enrollment)
    choices = extract_answers(request)
    submission.choices.set(choices)
    submission_id = submission.id
    return HttpResponseRedirect(reverse(viewname='courses:exam_result',
                                        args=(course_id, submission_id,)))


def extract_answers(request):
    submitted_answers = []
    for key in request.POST:
        if key.startswith('choice'):
            value = request.POST[key]
            choice_id = int(value)
            submitted_answers.append(choice_id)
    return submitted_answers


@login_required
def show_exam_result(request, course_id, submission_id):
    context = {}
    course = get_object_or_404(Course, pk=course_id)
    submission = Submission.objects.get(id=submission_id)
    choices = submission.choices.all()

    total_score = 0
    questions = course.question_set.all()  # Assuming course has related questions

    for question in questions:
        correct_choices = question.choice_set.filter(is_correct=True)  # Get all correct choices for the question
        selected_choices = choices.filter(question=question)  # Get the user's selected choices for the question

        # Check if the selected choices are the same as the correct choices
        if set(correct_choices) == set(selected_choices):
            total_score += question.grade  # Add the question's grade only if all correct answers are selected

    context['course'] = course
    context['grade'] = total_score
    context['choices'] = choices

    return render(request, 'courses/exam_result_bootstrap.html', context)
