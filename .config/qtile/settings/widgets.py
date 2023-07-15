from .theme import colors
from .keys import TERMINAL

from qtile_extras import widget
from libqtile.lazy import lazy
from qtile_extras.widget.decorations import PowerLineDecoration
# Get the icons at https://www.nerdfonts.com/cheat-sheet (you need a Nerd Font)

def power_line_arrow_right():
    return {
    "decorations": [
        PowerLineDecoration(path="arrow_right")
    ]
}

def power_line_arrow_left():
    return {
    "decorations": [
        PowerLineDecoration(path="arrow_left")
    ]
}

def base(fg='text', bg='dark'): 
    return {
        'foreground': colors[fg],
        'background': colors[bg]
    }


def separator():
    return widget.Sep(**base(), linewidth=0, padding=5)


def icon(fg='text', bg='dark', fontsize=16, text="?"):
    return widget.TextBox(
        **base(fg, bg),
        fontsize=fontsize,
        text=text,
        padding=3
    )


def workspaces(): 
    return [
        separator(),
        widget.GroupBox(
            **base(fg='light'),
            font='Noto',
            fontsize=19,
            margin_y=3,
            margin_x=0,
            padding_y=8,
            padding_x=5,
            borderwidth=1,
            active=colors['active'],
            inactive=colors['inactive'],
            rounded=False,
            highlight_method='block',
            urgent_alert_method='block',
            urgent_border=colors['urgent'],
            this_current_screen_border=colors['focus'],
            this_screen_border=colors['grey'],
            other_current_screen_border=colors['dark'],
            other_screen_border=colors['dark'],
            disable_drag=True,
            **power_line_arrow_left()
        ),
        separator(),
        widget.CurrentLayoutIcon(**base(bg='color1'), scale=0.65, **power_line_arrow_left()),
        widget.WindowName(**base(fg='focus'), fontsize=14, padding=5,**power_line_arrow_right()),

    ]


primary_widgets = [
    *workspaces(),



    icon(bg="color4", text=''),  # Icon: nf-oct-cpu

    widget.CPU(**base(bg='color4'), format="{freq_current}GHz {load_percent}%"),

    icon(bg="color4", text='󰍛'),  # Icon: nf-md-memory

    widget.Memory(**base(bg='color4'),format="{MemUsed: .0f}{mm} ", 
                mouse_callbacks={
                        'Button1': lazy.spawn(TERMINAL + " --hold -e htop"),                    # left click
                        'Button3': lazy.spawn(TERMINAL + " --hold -e watch -n 2 free -th"),     # right click
                    },
                **power_line_arrow_right()
                ),

    widget.Pomodoro(**base(bg='color3'), color_inactive=colors['text'], **power_line_arrow_right()),

    

    icon(bg="color2", fontsize=17, text='󰃰'), # Icon: nf-mdi-calendar_clock

    widget.Clock(**base(bg='color2'), format='%Y/%m/%d %a %H:%M', **power_line_arrow_right()),

    widget.StatusNotifier(**base(bg='color1'), padding=5),
]

secondary_widgets = [
    *workspaces(),

    widget.CurrentLayoutIcon(**base(bg='color1'), scale=0.65, **power_line_arrow_right()),

    widget.CurrentLayout(**base(bg='color1'), padding=5, **power_line_arrow_right()),

    widget.Clock(**base(bg='color2'), format='%Y/%m/%d %a %H:%M', **power_line_arrow_right()),
]

widget_defaults = {
    'font': 'Noto Bold',
    'fontsize': 14,
    'padding': 1,
}
extension_defaults = widget_defaults.copy()