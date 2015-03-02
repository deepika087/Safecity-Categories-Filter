    
from pprint import pprint as pp
    
import jsonpickle
class SafeCityFilter:
    def __init__(self, title, date, location, description, category, approved):
        self._incidentTitle=title
        self._incidentDate=date
        self._incidentLocation=location
        self._incidentDescription=description
        self._incidentCategory=category
        self._incidentApproved=approved        
