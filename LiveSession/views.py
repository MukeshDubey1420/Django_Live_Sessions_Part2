from django.http import HttpResponse
from django.shortcuts import render

#
# def Homepage(request):
#     # return HttpResponse("<p>Hello World !!!!!<p>")
#     my_html= """
#
#     <!doctype html>
#         <html lang="en">
#           <head>
#             <!-- Required meta tags -->
#             <meta charset="utf-8">
#             <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
#
#             <!-- Bootstrap CSS -->
#             <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.1.2/css/bootstrap.min.css" integrity="sha384-Smlep5jCw/wG7hdkwQ/Z5nLIefveQRIY9nfy6xoR1uRYBtpZgI6339F5dgvm/e9B" crossorigin="anonymous">
#
#             <title>Hello, world!</title>
#           </head>
#           <body>
#
#
#           <div class="jumbotron">
#               <h1 class="display-4">Hello, world!</h1>
#               <p class="lead">This is a simple hero unit, a simple jumbotron-style component for calling extra attention to featured content or information.</p>
#               <hr class="my-4">
#               <p>It uses utility classes for typography and spacing to space content out within the larger container.</p>
#               <a class="btn btn-primary btn-lg" href="#" role="button">Learn more</a>
#             </div>
#             <h1 class= "text-center">Hello, world!</h1>
#
#             <!-- Optional JavaScript -->
#             <!-- jQuery first, then Popper.js, then Bootstrap JS -->
#             <script src="https://code.jquery.com/jquery-3.3.1.slim.min.js" integrity="sha384-q8i/X+965DzO0rT7abK41JStQIAqVgRVzpbzo5smXKp4YfRvH+8abtTE1Pi6jizo" crossorigin="anonymous"></script>
#             <script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.14.3/umd/popper.min.js" integrity="sha384-ZMP7rVo3mIykV+2+9J3UJ46jBk0WLaUAdn689aCwoqbBJiSnjAK/l8WvCWPIPm49" crossorigin="anonymous"></script>
#             <script src="https://stackpath.bootstrapcdn.com/bootstrap/4.1.2/js/bootstrap.min.js" integrity="sha384-o+RDsa0aLu++PJvFqy8fFScvbHFLtbvScb8AjopnFD+iEQ7wo/CG0xlczd+2O/em" crossorigin="anonymous"></script>
#           </body>
#         </html>
#
#     """
#
#     return HttpResponse(my_html)


def Homepage(request):      # Request response ..
    context = {
        "title":"Hello",
        "name":"Mukesh Dubey",
    }

    return render(request, "sample.html" , context)

def MukeshPage(request):
    context = {
        "title": "Gaurav Chauhan",
        "name": "hello",
    }
    # Request response ..
    return render(request, "homeview.html" , context)

def GauravPage(request):
    context = {
        "title": "Gayatri",
        "name": "hello",
    }
    # Request response ..
    return render(request, "homeview.html" , context)


def Contactform(request):
    context = {
        "title": "Contact Page",
        "content": "welcome to Our contact page",

    }
    # if request.method == "GET":
    #     print(request.GET)
    #     print(request.GET.get('fullname'))
    #     print(request.GET.get('email'))
    #     print(request.GET.get('content'))

    if request.method == "POST":
        print(request.POST)
        print(request.POST.get('name'))
        print(request.POST.get('email'))
        print(request.POST.get('pwd'))
        print(request.POST.get('content'))


    return render(request, "contact.html", context)

