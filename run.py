from HouseAdvisor import *
from Calendar import *

Aengus = HouseAdvisor("Aengus")
Nikki = HouseAdvisor("Nikki")
Gorman = HouseAdvisor("Gorman")
DeVaun = HouseAdvisor("DeVaun")

thebois = [Aengus, Nikki, DeVaun, Gorman]

cal = Calendar("c_vno4sej7ittvciiadual8v8sak@group.calendar.google.com")
cal.setHAs(thebois)
print(cal.get_today_events())
print(cal.who_on_duty())

