#Main working file, prepare functions to be called in gui.py

from importlib.resources import path
from icalendar import Calendar, Event, vCalAddress, vText
from datetime import datetime
from pathlib import Path
import os
import pytz
from ics import Calendar
import requests

#import calendar from file or directory
#input: path to calendar
#output: Calendar entries in usabel format //TODO
#Based on: icalendar, google calendar (ics)
def importcalendar(calendarpath:path):
    return

#import calendar from file or directory
#input: url to calendar
#output: Calendar entries in usabel format //TODO
#Based on: google calendar (ics)
def importcalendar(calendarUrl: str):
    return