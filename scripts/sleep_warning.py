#!/usr/bin/env python3
import datetime
import json

def get_sleep_info():
    now = datetime.datetime.now()
    today = now.date()
    
    # Configuration
    wakeup_time = datetime.time(7, 0)
    bedtime_alert = datetime.time(22, 0)
    
    # Determine if "wakeup" should be today or tomorrow
    # If it's before 7 AM, wakeup is today. If it's late night, wakeup is tomorrow.
    if now.time() < wakeup_time:
        wakeup_dt = datetime.datetime.combine(today, wakeup_time)
    else:
        wakeup_dt = datetime.datetime.combine(today + datetime.timedelta(days=1), wakeup_time)
    
    remaining = wakeup_dt - now
    remaining_seconds = max(0, int(remaining.total_seconds()))
    hours, remainder = divmod(remaining_seconds, 3600)
    minutes, _ = divmod(remainder, 60)

    # Logic for when to show the module
    is_late_night = now.time() >= bedtime_alert
    is_early_morning = now.time() < wakeup_time

    if is_late_night or is_early_morning:
        icon = "󰒲"
        css_class = ""
        
        # Logic for CSS classes
        if hours < 6:
            css_class = "critical"
        elif hours < 8:
            css_class = "warning"
            
        return json.dumps({
            "text": f"{icon} {hours}h {minutes}m",
            "tooltip": f"Time until 7 AM: {hours}h {minutes}m",
            "class": css_class
        })
    
    # Return empty to hide the module during the day
    return json.dumps({"text": "", "class": "hidden"})

if __name__ == "__main__":
    print(get_sleep_info())
