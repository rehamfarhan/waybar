#!/usr/bin/env python3
import datetime
import json

def get_countdown():
    exam_date = datetime.date(2026, 4, 21)
    today = datetime.date.today()
    delta = exam_date - today
    days = delta.days

    text = f"󰺬 {days}d"
    tooltip = f"{days} days remaining until April 21th exams."
    
    css_class = ""
    if days < 15:
        css_class = "critical"
    elif days < 30:
        css_class = "warning"
        
    return json.dumps({
        "text": text,
        "tooltip": tooltip,
        "class": css_class
    })

if __name__ == "__main__":
    print(get_countdown())
