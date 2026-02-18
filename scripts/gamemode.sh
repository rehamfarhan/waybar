#!/bin/bash

# Simple script to toggle gamemode for Hyprland
# and clear some system cache.

HYPR_STATE=$(hyprctl getoption animations:enabled | awk 'NR==1{print $2}')

if [ "$HYPR_STATE" = "1" ]; then
    # Disable animations, gaps, etc.
    hyprctl --batch "
        keyword animations:enabled 0;
        keyword decoration:drop_shadow 0;
        keyword decoration:blur:enabled 0;
        keyword general:gaps_in 0;
        keyword general:gaps_out 0;
        keyword general:border_size 1;
        keyword decoration:rounding 0"
    
    # Free up RAM (requires sudo for full effect, but we can try)
    # sync; echo 3 | sudo tee /proc/sys/vm/drop_caches > /dev/null
    
    # Send notification
    notify-send "Gamemode Enabled" "Optimized for performance."
    echo '{"text": "󰓓 ", "class": "enabled", "tooltip": "Gamemode: ON"}'
else
    # Re-enable standard settings (defaulting to some common values)
    hyprctl --batch "
        keyword animations:enabled 1;
        keyword decoration:drop_shadow 1;
        keyword decoration:blur:enabled 1;
        keyword general:gaps_in 5;
        keyword general:gaps_out 10;
        keyword general:border_size 2;
        keyword decoration:rounding 10"
        
    notify-send "Gamemode Disabled" "Standard settings restored."
    echo '{"text": "󰓓 ", "class": "disabled", "tooltip": "Gamemode: OFF"}'
fi
