from django.shortcuts import render, HttpResponse

# Create your views here.
def home(requests):
        return render(requests,'index.html')

def add(requests):
    if requests.method == 'POST':
        a = int(requests.POST['txt1'])
        b = int(requests.POST['txt2'])
           
        if requests.POST.get('btnadd'):
            c= a+b
            mydict={'ans':c}
            return render (requests,'output.html',mydict)

        elif requests.POST.get('btnsub'):
            c= a-b
            mydict={'ans':c}
            return render (requests,'output.html',mydict)
        
        elif requests.POST.get('btnmul'):
            c= a*b
            mydict={'ans':c}
            return render (requests,'output.html',mydict)
        
        elif requests.POST.get('btndiv'):
            c= a/b
            mydict={'ans':c}
            return render (requests,'output.html',mydict)
            
            
       
    return render(requests,'add.html')