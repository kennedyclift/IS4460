from django.views import View
from django.shortcuts import render, redirect
from . import my_functions,my_objects

def title_name(the_name: str):

    return the_name.title()

def title_names(names: list):
    new_names = [x.title() for x in names]
    return new_names

class HomePageView(View):
    def get(self, request):

        my_name ="KENNEDY!"

        new_name = title_name(my_name)

        the_names = ['KENNEDY', "REECE", "KENNEDY"]

        other_names = the_names
        
        the_names.append('KLOEE')

        new_names = my_functions.title_names(the_names)

        car1 = my_objects.Car(color='green', sound='honk honk')

        car2 = my_objects.Car(color='blue', sound='beep beep')

        #titled_named = title_names(the_names)

        the_context = {'hi':'hello CLASS!',
                       'name':new_name, 
                       'names_list': other_names,
                       'car1':car1,
                       'car2':car2,
                       }

        return render(request,'my_app/index.html',the_context)
    
