#!/usr/bin/env python3
import datetime
import json
import sys

# Assume target bedtime is 11:00 PM (23:00) 
# and target wakeup is 7:00 AM next day.

def get_sleep_info():
    now = datetime.datetime.now()
    today = datetime.date.today()
    
    # Define sleep window
    wakeup = datetime.time(7, 0)
    bedtime = datetime.time(23, 0)
    
    # Calculate sleep remaining until 7 AM next day
    wakeup_dt = datetime.datetime.combine(today + datetime.timedelta(days=1), wakeup)
    remaining = wakeup_dt - now
    hours = remaining.total_seconds() / 3600
    
    # Activate if it's past 10 PM
    if now.time() >= datetime.time(22, 0) or now.time() < wakeup:
        icon = "󰒲"
        h, rem = divmod(int(remaining.total_seconds()), 3600)
        m, _ = divmod(rem, 60)
        
        text = f"{icon} {h}h {m}m left"
        css_class = "warning" if hours < 8 else ""
        if hours < 6:
            css_class = "critical"
            
        return json.dumps({
            "text": text,
            "tooltip": f"You need to sleep! Approx {h}h {m}m until wakeup.",
            "class": css_class
        })
    else:
        return json.dumps({"text": "", "tooltip": ""})

if __name__ == "__main__":
    print(get_sleep_info())
