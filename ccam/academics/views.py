from django.views.generic import TemplateView

from ccam.academics.models import Course


class CourseSubjects(TemplateView):
    template_name = "academics/_course_subjects.html"

    def get_course_id(self):
        course_id = self.request.GET.get("teacher-course")
        # If a blank option is selected, course_id comes as '' (falsy value)
        return course_id if course_id else 0

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        course_id = self.get_course_id()
        course = Course.objects.filter(id=course_id)

        if course.exists():
            subjects = course.first().subjects.all()
        else:
            subjects = []
        context["course_subjects"] = subjects
        return context
