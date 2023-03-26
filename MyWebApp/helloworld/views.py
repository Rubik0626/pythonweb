from django.views.generic import TemplateView


class IndexView(TemplateView):
    template_name = 'helloworld/index.html'

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        context['message'] = 'Hello Seiji!'
        return context


index = IndexView.as_view()