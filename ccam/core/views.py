from django_filters.views import FilterView


class FilteredListView(FilterView):
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        current_page = int(self.request.GET.get("page", 1))
        context.update({"current_page": current_page})
        return context
