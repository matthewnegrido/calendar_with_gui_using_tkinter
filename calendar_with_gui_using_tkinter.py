import calendar
import tkinter as tk
from datetime import date

def create_calendar_gui():

    root_window = tk.Tk()
    root_window.title("Tkinter Calendar")

    current_year = date.today().year
    current_month = date.today().month

    navigation_frame = tk.Frame(root_window)
    navigation_frame.pack(pady=10)

    previous_button = tk.Button(navigation_frame, text="<", width=3)
    previous_button.pack(side="left", padx=5)

    date_label = tk.Label(navigation_frame, text="", font=("Arial", 16, "bold"))
    date_label.pack(side="left", padx=10)

    next_button = tk.Button(navigation_frame, text=">", width=3)
    next_button.pack(side="left", padx=5)

    calendar_frame = tk.Frame(root_window)
    calendar_frame.pack(padx=10, pady=10)

    def update_calendar(year, month):
        # Clear existing calendar widgets
        for widget in calendar_frame.winfo_children():
            widget.destroy()

        month_name = calendar.month_name[month]
        date_label.config(text=f"{month_name} {year}")

        cal = calendar.monthcalendar(year, month)
        week_days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]

        for col, day_name in enumerate(week_days):
            label = tk.Label(calendar_frame, text=day_name, font=("Arial", 12, "bold"))
            label.grid(row=0, column=col, padx=5, pady=5)

        for row, week in enumerate(cal):
            for col, day in enumerate(week):
                if day == 0:
                    label = tk.Label(calendar_frame, text="", font=("Arial", 12))
                else:
                    label = tk.Label(calendar_frame, text=str(day), font=("Arial", 12))
                    # Highlight today's date
                    if year == date.today().year and month == date.today().month and day == date.today().day:
                        label.config(fg="red")  # Changed from text_color="red" to fg="red"
                label.grid(row=row + 1, column=col, padx=5, pady=5)

    def next_month_action():
        nonlocal current_year, current_month
        current_month += 1
        if current_month > 12:
            current_month = 1
            current_year += 1
        update_calendar(current_year, current_month)

    def previous_month_action():
        nonlocal current_year, current_month
        current_month -= 1
        if current_month < 1:
            current_month = 12
            current_year -= 1
        update_calendar(current_year, current_month)

    previous_button.config(command=previous_month_action)
    next_button.config(command=next_month_action)

    update_calendar(current_year, current_month)
    root_window.mainloop()

if __name__ == "__main__":
    create_calendar_gui()