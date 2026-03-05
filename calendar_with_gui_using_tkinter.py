import calendar
import customtkinter as ctk
from datetime import date

def create_calendar_gui():
    current_year = date.today().year
    current_month = date.today().month

def update_calendar(year, month):
    for widget in calendar_frame.winfo_children():
        widget.destroy()
    month_name = calendar.month_name[month]
    date_label.configure(text=f"{month_name} {year}")
    cal = calendar.monthcalendar(year, month)
    week_days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
    