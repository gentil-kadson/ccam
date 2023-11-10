from django.forms import widgets


class CCAMFileWidget(widgets.FileInput):
    template_name = "core/widgets/_ccam_file_input.html"
