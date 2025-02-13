import pathlib
from django.shortcuts import render
from django.http import HttpResponse

this_dir = pathlib.Path(__file__).resolve().parent

def home_page_view(request, *args, **kwargs):

    my_title ="My page"
    my_context ={
        "page_title" : my_title
    }
    html_template = "home.html"
    # html_file_path =this_dir / "home.html"
    # html_ = html_file_path.read_text()
    return render(request,html_template, my_context)
    # return "hello World" # 'str' object has no attribute 'get'



def my_old_home_page_view(request, *args, **kwargs):
    # html_ =""
    my_title ="My page"
    my_context ={
        "page-title" : my_title
    }
    html_ = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>
<body>
    <h1> Inline {page-title} </h1>
    <p>this is using of pathlib function checking finding html file and access to io.</p>
</body>
</html>
""".format(**my_context) # page_title=my_title
    print(this_dir)
    # html_file_path =this_dir / "home.html"
    # html_ = html_file_path.read_text()
    return HttpResponse(html_)
    # return "hello World" # 'str' object has no attribute 'get'