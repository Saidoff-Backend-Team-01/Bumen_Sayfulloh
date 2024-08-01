from django.contrib import admin

from .models import (
    Category,
    Club,
    ClubMeetings,
    Step,
    StepLesson,
    StepTest,
    Subject,
    SubjectTitle,
    TestAnswer,
    TestQuestion,
    UserClub,
    UserSubject,
    UserTestResult,
    UserTotalResult,
    Vacancy,
)

    
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display_fields = ["name", "clicked_count"]
    list_filter = ["name", "clicked_count"]
    search_fields = ["name"]


@admin.register(SubjectTitle)
class SubjectTitleAdmin(admin.ModelAdmin):
    list_display_fields = ["name", "category"]
    list_filter = ["name", "category"]
    search_fields = ["name"]


@admin.register(Subject)
class SubjectAdmin(admin.ModelAdmin):
    list_display_fields = ["name", "subject_type", "subject_title"]
    list_filter = ["name", "subject_type", "subject_title"]
    search_fields = ["name"]


@admin.register(UserSubject)
class UserSubjectAdmin(admin.ModelAdmin):
    list_display_fields = ["user", "subject", "total_test_ball"]
    list_filter = ["user", "subject", "total_test_ball"]
    search_fields = ["user"]


@admin.register(Vacancy)
class VacancyAdmin(admin.ModelAdmin):
    list_display_fields = ["name", "category", "description"]
    list_filter = ["name", "category", "description"]
    search_fields = ["name"]


@admin.register(Step)
class StepAdmin(admin.ModelAdmin):
    list_display_fields = ["title", "order", "subject", "description"]
    list_filter = ["title", "order", "subject", "description"]
    search_fields = ["title"]


@admin.register(Club)
class ClubAdmin(admin.ModelAdmin):
    list_display_fields = ["name", "subject" "description"]
    list_filter = ["name", "subject", "description"]
    search_fields = ["name"]


@admin.register(UserClub)
class UserClubAdmin(admin.ModelAdmin):
    list_display_fields = ["user", "club"]
    list_filter = ["user", "club"]
    search_fields = ["user"]


@admin.register(ClubMeetings)
class ClubMeetingsAdmin(admin.ModelAdmin):
    list_display_fields = ["name", "location", "date", "club"]
    list_filter = ["name", "location", "date", "club"]
    search_fields = ["name"]


@admin.register(StepLesson)
class StepLessonAdmin(admin.ModelAdmin):
    list_display_fields = ["step", "title", "file"]
    list_filter = ["step", "title", "file"]
    search_fields = ["title"]


@admin.register(StepTest)
class StepTestAdmin(admin.ModelAdmin):
    list_display_fields = [
        "step",
        "ball_for_each_test",
        "question_count",
        "question_type",
        "step_test_type",
        "time_for_question",
    ]
    list_filter = ["step", "ball_for_each_test"]
    search_fields = ["step"]


@admin.register(TestQuestion)
class TestQuestionAdmin(admin.ModelAdmin):
    list_display_fields = ["steptest", "text"]
    list_filter = ["steptest", "text"]


@admin.register(TestAnswer)
class TestAnswerAdmin(admin.ModelAdmin):
    list_display_fields = ["test_question", "answer_text", "is_correct"]
    list_filter = ["test_question", "answer_text", "is_correct"]


@admin.register(UserTestResult)
class UserTestResultAdmin(admin.ModelAdmin):
    list_display_fields = ["test_question", "user", "test_answer"]
    list_filter = ["test_question", "user", "test_answer"]
    search_fields = ["user"]


@admin.register(UserTotalResult)
class UserTotalResultAdmin(admin.ModelAdmin):
    list_display_fields = ["step_test", "user", "ball", "correct_ans"]
    list_filter = ["step_test", "user", "ball", "correct_ans"]
    search_fields = ["user"]
