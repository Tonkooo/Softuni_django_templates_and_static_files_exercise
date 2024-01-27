from django.shortcuts import render

class Person:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    @property
    def full_name(self):
        return f'{self.first_name} {self.last_name}'


def index(request):
    context = {
        'title': 'Employees list',
        'person': {
            'first_name': 'Doncho',
            'last_name': 'Minkov',
        },
        'person_obj': Person("Doncho", "Minkov"),

    }

    return render(request, 'employees/index.html', context)

