#!/bin/bash

# Get username
USER=$(whoami)
# Get kernel info
KERNEL=$(uname -r)
# Get uptime
UPTIME=$(uptime -p | sed 's/up //')

# Return JSON for Waybar
# Using printf to handle newlines correctly and escaping double quotes for the tooltip
printf '{"text": " %s", "tooltip": "Kernel: %s\\nUptime: %s"}\n' "$USER" "$KERNEL" "$UPTIME"
