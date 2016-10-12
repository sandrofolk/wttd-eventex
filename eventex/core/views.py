from django.views.generic import DetailView
from django.views.generic.list import ListView

from eventex.core.models import Speaker, Talk

# class GenericHomeView(MultipleObjectMixin, TemplateView):
    # template_name = 'index.html'
    # object_list = speakers = Speaker.objects.all()
    # context_object_name = 'speakers'

    # def get(self, *args, **kwargs):
    #     context = self.get_context_data()
    #     return self.render_to_response(context)

    # def render_to_response(self, context):
    #     return render(self.request, self.template_name, context)

    # def get_context_data(self, **kwargs):
    #     context = {self.context_object_name: self.object_list}
    #     context.update(kwargs)
    #     return context


# class HomeView(ListView):
#     template_name = 'index.html'
#     model = Speaker


home = ListView.as_view(template_name = 'index.html',
                        model = Speaker)


# def speaker_detail(request, slug):
#     speaker = get_object_or_404(Speaker, slug=slug)
#     return render(request, 'core/speaker_detail.html', {'speaker': speaker})


speaker_detail = DetailView.as_view(model=Speaker)


# def talk_list(request):
#     context = {
#         'morning_talks': Talk.objects.at_morning(),
#         'afternoon_talks': Talk.objects.at_afternoon(),
#     }
#     return render(request, 'core/talk_list.html', context)


talk_list = ListView.as_view(model=Talk)