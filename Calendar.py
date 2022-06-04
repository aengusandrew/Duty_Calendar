from apiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from datetime import *
from HouseAdvisor import *
import pickle


# TODO: Remove temp list of HAs
Aengus = HouseAdvisor("Aengus")
Nikki = HouseAdvisor("Nikki")
Gorman = HouseAdvisor("Gorman")
DeVaun = HouseAdvisor("DeVaun")

thebois = [Aengus, Nikki, DeVaun, Gorman]


class Duty_Calendar:
    def __init__(self, CalendarId):
        scopes = ['https://www.googleapis.com/auth/calendar']
        flow = InstalledAppFlow.from_client_secrets_file("client_secret.json", scopes=scopes)
        credentials = pickle.load(open("token.pkl", "rb"))
        self.service = build("calendar", "v3", credentials=credentials)
        self.cal_id = CalendarId

    def get_today_events(self):
        today = date.today()
        todays_events = []
        events = self.service.events().list(calendarId=self.cal_id, maxResults=2500, orderBy="startTime", singleEvents=True).execute()
        for event in events['items']:
            try:
                if event['start']['date'] == str(today):
                    todays_events.append(event['summary'])
            except KeyError:
                pass
        return todays_events

    def who_on_duty(self):
        todays_events = self.get_today_events()
        for event in todays_events:
            if event in self.HAs.names():
                return event

    def duty_label(self):
        curr_time = int(datetime.today().strftime("%H%M"))
        if curr_time >= self.duty_start or curr_time <= self.duty_end:
            try:
                Duty_HA = self.who_on_duty()
                if not self.in_room:
                    return "Tonight on duty is " + Duty_HA + ".\n The duty phone number is " + self.duty_phone + "."
                else:
                    return "Tonight on duty is " + Duty_HA + ", in their room.\n The duty phone number is " + self.duty_phone + "."
                # TODO: Add functionality to HA class which allows the system to display their room based off their name
            except TypeError:
                return "Error, no HA listed on duty tonight"
        else:
            return "We are not currently in duty hours,\n the campus safety phone number is " + self.campo_phone + "."

    def set_duty_hours(self, start_time, end_time):
        self.duty_start = start_time
        self.duty_end = end_time

    def setHAs(self, HA_list):
        for HA in HA_list:
            self.HAs.add(HA)

    HAs = HouseAdvisors(thebois)
    cal_id = ""
    duty_phone = "315-742-2622"
    campo_phone = "315-268-6666"

    duty_start = 2000
    duty_end = 800

    in_room = False