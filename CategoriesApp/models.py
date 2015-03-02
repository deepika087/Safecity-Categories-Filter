from django.db import models
import csv;

# Create your models here.
class MyCsvModel():

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

    def readCsv(self, filename):
        f = open(filename,  encoding="utf8");
        reader = csv.reader(f);
        rowList = list()
        for row in reader :
            row_utf8 = row
            rowList.append(row_utf8)
        return rowList

    def getCategories(self):
        rows = MyCsvModel.readCsv('DB.csv')
        distinctCategory = list()
        print("Total Input Length = " + str(len(rows)));

        for row in rows:
            print("Reading:" + row[MyCsvModel.columnCategory])
            for item in row[MyCsvModel.columnCategory].split(","):
                if not(item.lstrip().rstrip() in distinctCategory):
                    distinctCategory.append(item.lstrip().rstrip())
        print("Filtered Categories Length = " + str(len(distinctCategory)-1));

        result=list()
        count=0;
        for cat in distinctCategory:
            if (len(cat) > 0 and not(cat=="CATEGORY")):
                count=count+1
                result.append("\"" + str(count) + ".)" + cat + "\"");
        return result;



