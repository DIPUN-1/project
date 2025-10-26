from django.shortcuts import render
from django.http import HttpResponse
import hashlib

# Create your views here.

def home(request):
    return render(request, "index.html")

def check(request):
    message = ''
    OrginalHashKey = request.POST.get('hash')
    SourcePDF = request.FILES.get('file')
    print(OrginalHashKey)
    if OrginalHashKey and SourcePDF:
        sha256_hash = hashlib.sha256()
        for chunk in SourcePDF.chunks():
            sha256_hash.update(chunk)

        calculated_hash = sha256_hash.hexdigest()
        if calculated_hash == OrginalHashKey:
           message = '✅ SUCCESS: The file is valid you are good to go'
        else:
            message = "\n❌ FAILURE: The file is corrupt or has been modified!"
            
            
    context = {'data' : OrginalHashKey, 'message' : message, 'pdf' : SourcePDF}
    
    return render(request, "check.html", context)