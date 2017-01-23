#! /bin/zsh

if [ -z "$(pidof nm-applet)" ]; then
	nm-applet
else
	pkill -n nm-applet
fi
