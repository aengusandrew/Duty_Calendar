class HouseAdvisors:
    def __init__(self, HA_List):
        self.HAs=HA_List
    def add(self, newHA):
        self.HAs.append(newHA)

    def kill(self, killHA):
        self.HAs.remove(killHA)

    def names(self):
        HA_names = []
        for HA in self.HAs:
            HA_names.append(HA.name())
        return HA_names

    HAs=[]


class HouseAdvisor:
    def __init__(self, name):
        self.HA_name=name
    def name(self):
        return self.HA_name
    def setname(self, newname):
        self.HA_name=name
    def __str__(self):
        return self.HA_name
    HA_name=""