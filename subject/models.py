from django.db import models
from account.models import User
from common.models import Media
from django.utils.translation import gettext_lazy as _


class Category(models.Model):
    name = models.CharField(_('name'), max_length=255)
    clicked_count = models.PositiveBigIntegerField(_('Clicked count'), default=0)
    
    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.name


class SubjectTitle(models.Model):
    name = models.CharField(_('name'), max_length=255)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True)
    
    class Meta:
        verbose_name = "Subject Title"
        verbose_name_plural = "Subject Titles"

    def __str__(self):
        return self.name


class Subject(models.Model):
    SUBJECT_TYPE_CHOICES = [
        ('local', 'LOCAL'),
        ('global', 'GLOBAL'),
    ]
    name = models.CharField(_('name'), max_length=255)
    subject_type = models.CharField(_('Subject type'), max_length=255, choices=SUBJECT_TYPE_CHOICES, default='local')
    subject_title = models.ForeignKey(SubjectTitle, on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Subject"
        verbose_name_plural = "Subjects"
   
    def __str__(self):
        return self.name


class UserSubject(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    subject = models.ForeignKey(Subject, on_delete=models.SET_NULL, null=True, blank=True)
    total_test_ball = models.FloatField(null=True, blank=True)

    def __str__(self):
        return f"{self.user} - {self.subject}"
    
    class Meta:
        verbose_name = "User Subject"
        verbose_name_plural = "User Subjects"


class Vacancy(models.Model):
    name = models.CharField(_('name'), max_length=255)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True)
    description = models.TextField()
    
    class Meta:
        verbose_name = "Vacancy"
        verbose_name_plural = "Vacancies"

    def __str__(self):
        return self.name


class Step(models.Model):
    title = models.CharField(_('Title'), max_length=255)
    order = models.PositiveIntegerField(_('Order'), default=0)
    subject = models.ForeignKey(Subject, on_delete=models.SET_NULL, null=True, blank=True)
    description = models.TextField(_('Description'))

    class Meta:
        verbose_name = "Step"
        verbose_name_plural = "Steps"
        
    def __str__(self):
        return self.title


class Club(models.Model):
    name = models.CharField(_('name'), max_length=255)
    subject = models.ForeignKey(Subject, on_delete=models.SET_NULL, null=True, blank=True)
    description = models.TextField(_('Description'))
    
    class Meta:
        verbose_name = "Club"
        verbose_name_plural = "Clubs"

    def __str__(self):
        return self.name


class UserClub(models.Model):
    user = models.ManyToManyField(User, related_name="users")
    club = models.ForeignKey(Club, on_delete=models.SET_NULL, null=True, blank=True)
    
    class Meta:
        verbose_name = "User Club"
        verbose_name_plural = "User Clubs"

    def __str__(self):
        return f"{self.user} - {self.club}"

class ClubMeetings(models.Model):
    name = models.CharField(_('name'), max_length=255)
    location = models.CharField(_('Location'), max_length=255)
    date = models.DateField()
    club = models.ForeignKey(Club, on_delete=models.SET_NULL, null=True, blank=True)

    class Meta:
        verbose_name = "Club Meeting"
        verbose_name_plural = "Club Meetings"

    def __str__(self):
        return self.name


class StepLesson(models.Model):
    step = models.ForeignKey(Step, on_delete=models.SET_NULL, null=True, blank=True)
    title = models.CharField(max_length=255)
    file = models.ForeignKey(Media, on_delete=models.SET_NULL, null=True, blank=True)
    
    class Meta:
        verbose_name = "Step Lesson"
        verbose_name_plural = "Step Lessons"

    def __str__(self):
        return self.title


class StepTest(models.Model):
    QUESTION_TYPE_CHOICES = [
        ('multiple', 'MULTIPLE'),
        ('single', 'SINGLE'),
    ]
    STEP_TEST_TYPE_CHOICES = [
        ('midterm', 'MIDTERM'),
        ('final', 'FINAL'),
    ]
    step = models.ForeignKey(Step, on_delete=models.SET_NULL, null=True, blank=True)
    ball_for_each_test = models.FloatField(null=True)
    question_count = models.PositiveIntegerField(default=0)
    question_type = models.CharField(max_length=255, choices=QUESTION_TYPE_CHOICES, default='single')
    step_test_type = models.CharField(max_length=255, choices=STEP_TEST_TYPE_CHOICES, default='midterm')
    time_for_question = models.PositiveIntegerField(default=0)
    
    class Meta:
        verbose_name = "Step Test"
        verbose_name_plural = "Step Tests"
        ordering = ['step_test_type']

    def __str__(self):
        return f"{self.step} - {self.step_test_type}"


class TestQuestion(models.Model):
    steptest = models.ForeignKey(StepTest, on_delete=models.SET_NULL, null=True, blank=True)
    text = models.TextField(_('Text'))

    class Meta:
        verbose_name = "Test Question"
        verbose_name_plural = "Test Questions"

    def __str__(self):
        return f"{self.steptest} - {self.id}"


class TestAnswer(models.Model):
    test_question = models.ForeignKey(TestQuestion, on_delete=models.SET_NULL, null=True, blank=True)
    answer_text = models.TextField(_('Answer Text'))
    is_correct = models.BooleanField(default=False)

    class Meta:
        verbose_name = "Test Answer"
        verbose_name_plural = "Test Answers"

    def __str__(self):
        return f"{self.test_question} - {self.answer_text}"


class UserTestResult(models.Model):
    test_question = models.ForeignKey(TestQuestion, on_delete=models.SET_NULL, null=True, blank=True)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    test_answer = models.ForeignKey(TestAnswer, on_delete=models.SET_NULL, null=True, blank=True)
    
    class Meta:
        verbose_name = "User Test Result"
        verbose_name_plural = "User Test Results"

    def __str__(self):
        return f"{self.user} - {self.test_question}"


class UserTotalResult(models.Model):
    step_test = models.ForeignKey(StepTest,on_delete=models.SET_NULL, null=True, blank=True)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    ball = models.FloatField(default=0)
    correct_ans = models.PositiveBigIntegerField(default=0)

    class Meta:
        verbose_name = "User Total Result"
        verbose_name_plural = "User Total Results"
        
    def __str__(self):
        return f"{self.user} - {self.step_test}"