from django.shortcuts import render
from CategoriesApp.SafeCityFilter import SafeCityFilter as scf
import jsonpickle
import csv

columnIncidentTitle=1
columnIncidentDate=2
columnLocation=3
columnDescription=4
columnCategory=5
columnFirstName=10
columnLastName=11
columnEmail=12
columnApproved=13
columnVerified=14


Categories = list()
Categories.append("Rape / Sexual Assault")
Categories.append("Catcalls/Whistles")
Categories.append("Commenting")
Categories.append("Touching /Groping")
Categories.append("Sexual Invites")
Categories.append("Indecent exposure")
Categories.append("Ogling/Facial Expressions/Staring")
Categories.append("Taking pictures")
Categories.append("Others")
Categories.append("Poor / No Street Lighting")
Categories.append("North East India Report")
Categories.append("Chain Snatching")


# Create your views here.
def chooseCategory(request):
    selectedCategoryIndex = request.GET.get('q', '')
    message = "Not Searched yet"
    totalCount = 0
    if not( selectedCategoryIndex == '' ):
        message, totalCount = searchCategory(selectedCategoryIndex)
    return render(request, "CategoriesApp/index.html", {"messageKey" : message, "TotalResult": totalCount});

def readCsv(filename):
    f = open(filename,  encoding="utf8");
    reader = csv.reader(f);
    rowList = list()
    for row in reader :
        row_utf8 = row
        rowList.append(row_utf8)
    return rowList

def searchCategory(selectedCategoryIndex):
    ind = int(selectedCategoryIndex)
    selectedCategory = Categories[ind]
    print("Requested category" + selectedCategory)
    listResult = list();
    rows = readCsv('D:\Safecity\DjangoProject\Safecity\Scripts\Categories\CategoriesApp\DB.csv')
    totalCount = 0;
    print("==============RESULTS===================")
    for row in rows:
        if (row[columnCategory].find(selectedCategory) > 0 \
            and row[columnApproved] == "YES"):

            """
            print(row[columnIncidentTitle], row[columnIncidentDate],
                  row[columnLocation], row[columnDescription], row[columnCategory],
                  row[columnFirstName], row[columnLastName], row[columnEmail],
                  row[columnApproved], row[columnVerified])
            """

            filteredResult=scf(row[columnIncidentTitle], row[columnIncidentDate],
                  row[columnLocation], row[columnDescription], row[columnCategory],
                  row[columnApproved])
            listResult.append(filteredResult);
            totalCount = totalCount + 1;

    jsonFilteredResult = jsonpickle.encode(listResult, unpicklable=False);
    print(totalCount)
    return jsonFilteredResult, totalCount

            #resultCount=resultCount+1
    #return resultCount