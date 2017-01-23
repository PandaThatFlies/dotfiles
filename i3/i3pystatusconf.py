import subprocess

from i3pystatus import Status

status = Status(standalone=True)

# Clock
status.register("clock",
    format="%H:%M",
    on_leftclick=["zsh /home/shota/.config/i3/clock.sh"],
    #hints={
    #    "separator_block_width": 42,},
	)

# Date
status.register("clock",
    format="%a %-d %b",
    on_leftclick="zsh /home/shota/.config/i3/calendar.sh",
    #hints={
    #    "separator": False,
    #    "separator_block_width": 28,},
	)

# Shows pulseaudio default sink volume
#
# Note: requires libpulseaudio from PyPI


status.register("pulseaudio",
    format=" {volume}",)

# Displays the weather like this:
#
#status.register("weather",
#    location_code="ASXX0043:1",
#    format="GEELONG {current_temp}",
#    interval=60)
#status.register("weather",
#    location_code="ASXX0075:1",
#    format="MELBOURNE {current_temp}",
#    interval=60)

# Shows the average load of the last minute and the last 5 minutes
# (the default value for format is used)
#status.register("load")



# Displays whether a DHCP client is running
#status.register("runwatch",
#    name="DHCP",
#    path="/var/run/dhclient*.pid",)

# Shows the address and up/down state of eth0. If it is up the address is shown in
# green (the default value of color_up) and the CIDR-address is shown
# (i.e. 10.10.10.42/24).
# If it's down just the interface name (eth0) will be displayed in red
# (defaults of format_down and color_down)
#
# Note: the network module requires PyPI package netifaces
#status.register("network",
#    format_up=" {essid} {quality:03.0f}%",
#    format_down="",
#    color_up="#38912b",
#    color_down="#BF3939",
#    )

#battery

status.register("battery",
    format="{status} {percentage_design:.0f}%{remaining:%E⁣   %hh%Mm}",
    alert=True,
    alert_percentage=10,
    #full_color="#3BB9FF",
    full_color="#FFFFFF",
    color="#FFFFFF",
    charging_color="#4AA02C",
    critical_color="#C11B17",
    on_leftclick='notify-send -u low "`acpi -iab`"',
    status={
        "DPL": "⚠ ",
       	"DIS": "🔋 ",
       	"CHR": "⚡",
       	"FULL": "🔌 ",
    },
    #hints={
    #    "separator_block_width": 42,},
	)


# Has all the options of the normal network and adds some wireless specific things
# like quality and network names.
#
# Note: requires both netifaces and basiciw
status.register("network",
    interface="wlp2s0",
    format_up="",
    format_down="",
    color_up="#FFFFFF",
    on_leftclick="zsh /home/shota/.config/i3/nm-applet.sh",
    on_upscroll ="", 
    on_downscroll ="", 
    )

# Shows disk usage of /
# Format:
# 42/128G [86G]
status.register("disk",
    path="/",
    format="{avail}G",)

#status.register("disk",
#    path="/home/benkaiser/HD/",
#    format="{avail}G",)




# Shows your CPU temperature, if you have a Intel CPU
status.register("temp",
    format=" {temp:.0f}°C",)

# CPU usage
status.register("cpu_usage",
    format="CPU: {usage}%",
    #start_color="#4AA02C",
    #end_color="#C11B17",
	interval=5,
    on_leftclick="zsh /home/shota/.config/i3/htop.sh",
    #hints={
        #"separator_block_width": 42,
        #"min_width": 81,
		#"width": 81,},
	)

#ram
status.register("mem",    
	format="RAM: {used_mem}/{total_mem}",

	divisor=1073741824,	
	color="#FFFFFF",
	warn_percentage=75,
	alert_percentage=90,
    alert_color="#C11B17",
    warn_color="##FFCC00",
    #multi_colors="true",
    on_leftclick="zsh /home/shota/.config/i3/htop.sh",
    #hints={
    #    #"separator_block_width": 42,
    #    "min_width": 81,
	#	"width": 81,},
	)


#wifi(with nm-applet)
#status.register("shell",
#    command="nm-applet",)




# Music
status.register("mpd",
    format="{status}  {artist} - {title}",
    status={
        'stop': '◾',
        'play': '▶',
        'pause': '⏸'
    },
    #hints={
    #    "separator_block_width": 42,},
	)


# all my custom buttons
#status.register("text",
#    text="New Comic",
#    cmd_leftclick="/home/benkaiser/.i3/update_background",
#    color="#44bbff")

#status.register("text",
#    text="Sleep Screen",
#    cmd_leftclick="sleep 1; xset dpms force off",
#    color="#44bbff")

#i3lock = "i3lock -i /home/benkaiser/Pictures/wallpapers/wide_windows_desktop.png -p win";

#status.register("text",
#    text="Suspend System",
#    cmd_leftclick=i3lock + "; systemctl suspend",
#    color="#44bbff")

#status.register("text",
#    text="Screensaver",
#    cmd_leftclick="xscreensaver-command -activate",
#    color="#44bbff")

#status.register("text",
#    text="lock",
#    cmd_leftclick=i3lock,
#    color="#44bbff")

status.run()
