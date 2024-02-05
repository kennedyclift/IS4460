from django.views import View
from django.shortcuts import render, redirect

def title_name(the_name: str):
    new_name = the_name.title()
    return the_name


class HomePageView(View):
    def get(self, request):

        my_name = "KENNEDY"

        new_name = title_name(my_name)
     
        return render(request, 'my_app/index.html',{'hi':'HELLO WORLD!', 'name':new_name})