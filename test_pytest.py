import datetime
import show_open_food_trucks
from unittest.mock import Mock,patch

def  test_request_response():

    s = show_open_food_trucks.Data()
    response = s.get_data("http://data.sfgov.org/resource/bbb8-hzi6.json?dayorder=3&$select=applicant, location \
        &$where=start24 <='13:00' AND end24>='13:00'&$limit=10&$offset=10&$order=applicant ASC")
    
    assert response.status_code==200

def test_get_url():

    with patch.object(datetime, 'datetime', Mock(wraps=datetime.datetime)) as patched:
        
        d = show_open_food_trucks.Display()
        
        monday = datetime.datetime(year=2020, month=2, day=17)
        patched.today.return_value = monday
        timeNow = datetime.datetime(year=2020, month=2, day=17, hour=13, minute=00)
        patched.now.return_value = timeNow

        url = d.get_url()

        assert url=="http://data.sfgov.org/resource/bbb8-hzi6.json?dayorder=1&$select=applicant, location \
        &$where=start24 <='13:00' AND end24>='13:00'&$limit=10&$offset=0&$order=applicant ASC"


   






