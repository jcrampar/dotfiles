# Antonio Sarosi
# https://youtube.com/c/antoniosarosi
# https://github.com/antoniosarosi/dotfiles

# Qtile keybindings

from libqtile.config import Key
from libqtile.command import lazy


mod = "mod4"
ALTGR = "mod5"
TERMINAL = "alacritty"

keys = [Key(key[0], key[1], *key[2:]) for key in [

    # ------------ Window Configs ------------

    # Switch between windows in current stack pane
    ([mod], "Down", lazy.layout.down()),
    ([mod], "Up", lazy.layout.up()),
    ([mod], "Left", lazy.layout.left()),
    ([mod], "Right", lazy.layout.right()),

    # Change window sizes 
    ([mod, "shift"], "Right", lazy.layout.grow()),
    ([mod, "shift"], "Left", lazy.layout.shrink()),
    ([mod, "shift"], "n", lazy.layout.normalize()),

    # Toggle floating
    ([mod, "shift"], "f", lazy.window.toggle_floating()),

    # Move windows up or down in current stack
    ([mod, "shift"], "j", lazy.layout.shuffle_down()),
    ([mod, "shift"], "k", lazy.layout.shuffle_up()),

    # Toggle between different layouts as defined below
    ([mod], "Tab", lazy.next_layout()),
    ([mod, "shift"], "Tab", lazy.prev_layout()),

    # Kill window
    ([mod], "w", lazy.window.kill()),

    # Switch focus of monitors
    ([mod], "period", lazy.next_screen()),
    ([mod], "comma", lazy.prev_screen()),

    # Restart Qtile
    ([mod, "control"], "r", lazy.restart()),

    ([mod, "control"], "q", lazy.shutdown()),
    ([mod], "r", lazy.spawncmd()),

    # ------------ App Configs ------------

    # Menu
    ([mod], "d", lazy.spawn("/home/juanc/.config/rofi/scripts/launcher.sh --show drun --type 6 --style 1")),

    
    # Window Nav
    ([mod], "r", lazy.spawn("rofi -show")),

    # rofi calc
    ([mod], "c", lazy.spawn("rofi -show calc")),

    # rofi emoji
    ([ALTGR], "e", lazy.spawn("rofi -show emoji")),

    # Browser
    ([mod], "b", lazy.spawn("brave")),

    # File Explorer
    ([mod], 'f', lazy.group['scratchpad'].dropdown_toggle('fm')),

    # Terminal
    ([mod], "Return", lazy.spawn(TERMINAL)),
    ([mod, "control"], 'Return', lazy.group['scratchpad'].dropdown_toggle('term')),

    #calendar
    ([mod], 'k', lazy.group['scratchpad'].dropdown_toggle('khal')),


    # Redshift
    ([mod], "f1", lazy.spawn("redshift -O 2400")),
    ([mod, "shift"], "f1", lazy.spawn("redshift -x")),

    # Screenshot
    ([], "Print", lazy.spawn("flameshot gui")),
    (["control"], "Print", lazy.spawn("flameshot full -p " + "/home/juanc/Pictures")),

    # menu power 
    ([ALTGR], "p", lazy.spawn("sh /home/juanc/.local/bin/powermenu.sh")),


    # ------------ Hardware Configs ------------

    # Volume
    ([], "XF86AudioLowerVolume", lazy.spawn(
        "pactl set-sink-volume @DEFAULT_SINK@ -5%"
    )),
    ([], "XF86AudioRaiseVolume", lazy.spawn(
        "pactl set-sink-volume @DEFAULT_SINK@ +5%"
    )),
    ([], "XF86AudioMute", lazy.spawn(
        "pactl set-sink-mute @DEFAULT_SINK@ toggle"
    )),

    # Brightness
    ([], "XF86MonBrightnessUp", lazy.spawn("brightnessctl set +10%")),
    ([], "XF86MonBrightnessDown", lazy.spawn("brightnessctl set 10%-")),
]]