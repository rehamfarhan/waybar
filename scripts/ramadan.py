#!/usr/bin/env python3
import datetime
import json
import requests
import subprocess
import sys

# Configuration for Satkhira, Bangladesh
CITY = "Satkhira"
COUNTRY = "Bangladesh"
METHOD = 1  # University of Islamic Sciences, Karachi

def get_ramadan_info():
    try:
        # 1. Fetch live prayer times
        url = f"https://api.aladhan.com/v1/timingsByCity?city={CITY}&country={COUNTRY}&method={METHOD}"
        response = requests.get(url, timeout=5)
        response.raise_for_status()
        data = response.json()
        
        timings = data['data']['timings']
        sehri_str = timings['Fajr']
        iftar_str = timings['Maghrib']

        now = datetime.datetime.now()
        today = datetime.date.today()
        
        # Convert API strings to datetime objects
        sehri_dt = datetime.datetime.combine(today, datetime.datetime.strptime(sehri_str, "%H:%M").time())
        iftar_dt = datetime.datetime.combine(today, datetime.datetime.strptime(iftar_str, "%H:%M").time())

        # 2. Logic for next event
        if now < sehri_dt:
            next_event, target_dt, icon = "Sehri", sehri_dt, "󱗠"
        elif now < iftar_dt:
            next_event, target_dt, icon = "Iftar", iftar_dt, "󱗢"
        else:
            next_event = "Sehri"
            target_dt = sehri_dt + datetime.timedelta(days=1)
            icon = "󱗠"

        diff = target_dt - now
        total_seconds = int(diff.total_seconds())
        hours, remainder = divmod(total_seconds, 3600)
        minutes, _ = divmod(remainder, 60)

        # 3. Notification Trigger
        # Send notification if the event is happening within the next 60 seconds
        if 0 <= total_seconds < 60:
            msg = f"It is time for {next_event} ({target_dt.strftime('%I:%M %p')})!"
            subprocess.run(["notify-send", "-u", "critical", "-a", "Ramadan Timer", "🌙 Time Alert", msg])

        # 4. JSON Output for Waybar
        time_remaining = f"{hours}h {minutes}m"
        exact_time = target_dt.strftime("%I:%M %p")
        
        return json.dumps({
            "text": f"{icon} {next_event} in {time_remaining}",
            "tooltip": f"Next Event: {next_event}\nTime: {exact_time}\nLocation: {CITY}",
            "class": next_event.lower()
        })

    except Exception as e:
        return json.dumps({
            "text": "󱗠 Error",
            "tooltip": f"Error: {str(e)}"
        })

if __name__ == "__main__":
    print(get_ramadan_info())
