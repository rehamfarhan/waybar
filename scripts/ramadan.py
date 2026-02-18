#!/usr/bin/env python3
import datetime
import json
import sys

# Since I don't have the user's location, I will use a simple fixed calculation 
# or look for an API. For now, let's provide a script that can be configured.
# Ramadan 2026 starts approx Feb 19.

def get_ramadan_info():
    today = datetime.date.today()
    # Simple example data for the month of Ramadan (Feb/March 2026)
    # In a real scenario, this would use a library like 'hijri-converter' or an API.
    
    # Placeholder: Sehri ~5:15 AM, Iftar ~6:15 PM
    sehri = datetime.time(5, 15)
    iftar = datetime.time(18, 15)
    
    now = datetime.datetime.now()
    sehri_dt = datetime.datetime.combine(today, sehri)
    iftar_dt = datetime.datetime.combine(today, iftar)
    
    if now < sehri_dt:
        next_event = "Sehri"
        remaining = sehri_dt - now
        icon = "󱗠"
    elif now < iftar_dt:
        next_event = "Iftar"
        remaining = iftar_dt - now
        icon = "󱗢"
    else:
        # Next day's Sehri
        next_event = "Sehri"
        remaining = (sehri_dt + datetime.timedelta(days=1)) - now
        icon = "󱗠"

    hours, remainder = divmod(remaining.seconds, 3600)
    minutes, _ = divmod(remainder, 60)
    
    time_str = f"{hours}h {minutes}m"
    text = f"{icon} {next_event} in {time_str}"
    tooltip = f"Next: {next_event}
Remaining: {time_str}"
    
    return json.dumps({
        "text": text,
        "tooltip": tooltip
    })

if __name__ == "__main__":
    print(get_ramadan_info())
