from django.db import models
from django.contrib.auth.models import User


class Instructor(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    full_time = models.BooleanField(default=True)
    total_learners = models.IntegerField()

    def __str__(self):
        return self.user.username


class Learner(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    OCCUPATION_CHOICES = [
        ('student', 'Student'),
        ('developer', 'Developer'),
        ('data_scientist', 'Data Scientist'),
        ('dba', 'Database Admin'),
    ]
    occupation = models.CharField(
        null=False,
        max_length=20,
        choices=OCCUPATION_CHOICES,
        default='student'
    )
    social_link = models.URLField(max_length=200)

    def __str__(self):
        return self.user.username + "," + self.occupation


class Course(models.Model):
    name = models.CharField(null=False, max_length=30, default='online course')
    image = models.ImageField(upload_to='course_images/')
    description = models.CharField(max_length=1000)
    pub_date = models.DateField()
    instructors = models.ManyToManyField(Instructor)
    users = models.ManyToManyField(User, through='Enrollment')
    total_enrollment = models.IntegerField(default=0)
    is_enrolled = False

    def __str__(self):
        return "Name: " + self.name + "," + "Description: " + self.description


class Lesson(models.Model):
    title = models.CharField(max_length=200, default="title")
    order = models.IntegerField(default=0)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    content = models.TextField()

    def __str__(self):
        return self.title


class Enrollment(models.Model):
    AUDIT = 'audit'
    HONOR = 'honor'
    BETA = 'BETA'
    COURSE_MODES = [
        (AUDIT, 'Audit'),
        (HONOR, 'Honor'),
        (BETA, 'BETA')
    ]
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    date_enrolled = models.DateField(auto_now_add=True)
    mode = models.CharField(max_length=5, choices=COURSE_MODES, default=AUDIT)
    rating = models.FloatField(default=5.0)


class Question(models.Model):
    # Has a One-to-Many relationship with the Course model (Foreign Key)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    # Has a One-to-Many relationship with Lesson model (Foreign Key) - optional
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE, null=True, blank=True)
    # question text
    content = models.CharField(max_length=200)
    # question grade/mark
    grade = models.IntegerField(default=50)

    def __str__(self):
        return "Question: " + self.content

    # method to calculate if the learner gets the score of the question
    def is_get_score(self, selected_ids):
        all_answers = self.choice_set.filter(is_correct=True).count()
        selected_correct = self.choice_set.filter(is_correct=True, id__in=selected_ids).count()
        if all_answers == selected_correct:
            return True
        else:
            return False


class Choice(models.Model):
    # Has a One-to-Many relationship with the Question model (Foreign Key)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    # choice text
    content = models.CharField(max_length=200)
    # Indicates if this choice is a correct answer or not
    is_correct = models.BooleanField(default=False)

    def __str__(self):
        return self.content


class Submission(models.Model):
    enrollment = models.ForeignKey(Enrollment, on_delete=models.CASCADE)
    choices = models.ManyToManyField(Choice)

    def __str__(self):
        return f"Submission for {self.enrollment.user.username} in {self.enrollment.course.name}"
