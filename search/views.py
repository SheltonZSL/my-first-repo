import faker
from django.views.generic import TemplateView, ListView
from django.db.models import Q
from .models import Movie
from faker import Faker
from django.http import HttpResponse

fake = Faker()


class HomePageView(TemplateView):
    template_name = 'home.html'


class SearchResultsView(ListView):
    model = Movie
    template_name = 'search_results.html'

    def get_queryset(self):
        query = self.request.GET.get('q')
        object_list = Movie.objects.filter(
            Q(movie_id__icontains=query)
            | Q(movie__icontains=query)
            | Q(other_name__icontains=query)
            | Q(director__icontains=query)
            | Q(actor__icontains=query)
            | Q(first_introduction__icontains=query)
        )
        print(object_list.query)
        print('fuck you executed')
        print(object_list)
        return object_list


def generate_fake_data(request):
    for i in range(100):
        Movie.objects.create(
            movie_id=fake.uuid4(),
            movie=fake.name(),
            other_name=fake.name() + 'other',
            director=fake.name(),
            actor=fake.name(),
            year=fake.date(),
            rate=fake.random_int(),
            first_introduction=fake.paragraph()
        )
    rendered = "<div>100 fake data generated</div>" \
               "list of fake data: <br>"

    return HttpResponse(rendered)
