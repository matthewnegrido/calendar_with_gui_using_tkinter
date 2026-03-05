import calendar
import customtkinter as ctk
from datetime import date

def create_calendar_gui():
    current_year = date.today().year
    current_month = date.today().month