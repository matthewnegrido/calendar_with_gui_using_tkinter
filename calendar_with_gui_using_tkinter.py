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
    for col, day_name in enumerate(week_days):
        label = ctk.CTkLabel(calendar_frame, text=day_name, font=("Arial", 12, "bold"))
        label.grid(row=0, column=col, padx=5, pady=5)
    for row, week in enumerate(cal):
        for col, day in enumerate(week):
            if day == 0:
                label = ctk.CTkLabel(calendar_frame, text="", font=("Arial", 12))
            else:
                label = ctk.CTkLabel(calendar_frame, text=str(day), font=("Arial", 12))
                if year == date.today().year and month == date.today().month and day == date.today().day:
                    label.configure(text_color="red")
            label.grid(row=row + 1, column=col, padx=5, pady=5)

            