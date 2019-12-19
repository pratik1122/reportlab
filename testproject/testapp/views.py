from django.shortcuts import render

# Create your views here.
from testapp.models import Report


import openpyxl

def input(request):
    return render(request,'testapp/forms.html')



def index(request):

    if "GET" == request.method:
        return render(request, 'testapp/index.html', {})

    else:
        excel_file = request.FILES["excel_file"]

        wb = openpyxl.load_workbook(excel_file,data_only = True)

        # getting a particular sheet by name out of many sheets
        worksheet = wb["Sheet1"]


        # worksheet = wb["Sheet1"]
        print(worksheet)


#################################  reading excel data        #######################################

        excel_data = list()
        sd = {}
        # iterating over the rows and column
        # getting value from each cell in row
        for row in worksheet.iter_rows(min_col=2,max_col =4,min_row =4,max_row =8):
            row_data = list()

            sd['name'] = row[0].value
            sd['phone'] = row[1].value
            sd['address'] = row[2].value
            r = Report(**sd)
            r.save()

            #     row_data.append(str(cell.value))
            # excel_data.append(row_data)


        return render(request,'testapp/forms.html')










