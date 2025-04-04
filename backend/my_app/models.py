from django.db import models


class StudentInfo(models.Model):
    student_chat_id = models.BigIntegerField(unique=True, blank=True, null=True, verbose_name="Student Chat ID")
    full_name = models.CharField(max_length=100, blank=True, null=True, verbose_name="Full Name")
    course_name = models.CharField(max_length=50, blank=True, null=True, verbose_name="Course Name")
    teacher_course_name = models.CharField(max_length=50, blank=True, null=True, verbose_name="Teacher's Course Name")
    teacher_name = models.CharField(max_length=100, blank=True, null=True, verbose_name="Teacher Name")
    language = models.CharField(max_length=2, blank=True, null=True, verbose_name='Student language')

    class Meta:
        verbose_name = "Student Info"
        verbose_name_plural = "Students Info"
        ordering = ["full_name"]

    def __str__(self):
        return f"{self.full_name} - {self.course_name}"


class Question(models.Model):
    question_text = models.CharField(max_length=255, verbose_name="Question")

    class Meta:
        verbose_name = "Question"
        verbose_name_plural = "Questions"
        ordering = ["id"]
        db_table = "question"

    def __str__(self):
        return self.question_text


class Answer(models.Model):
    RATING_CHOICES = [(i, str(i)) for i in range(1, 6)]

    rating = models.PositiveSmallIntegerField(
        verbose_name="Rating",
        choices=RATING_CHOICES,
        default=3
    )
    question = models.ForeignKey(Question, on_delete=models.PROTECT, verbose_name="Related Question")
    student = models.ForeignKey(StudentInfo, on_delete=models.CASCADE, verbose_name="Answered By")

    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Created At")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Updated At")

    class Meta:
        verbose_name = "Answer"
        verbose_name_plural = "Answers"
        ordering = ["-created_at"]
        db_table = "answer"

    def __str__(self):
        return f"{self.student.full_name}'s Answer: {self.rating} to '{self.question.question_text}'"
