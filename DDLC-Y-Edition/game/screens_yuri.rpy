# Yuri-themed menu overrides and color tweaks

# change the accent color globally to a purple shade
init -1 python:
    # Ren'Py GUI settings are stored on the gui object
    gui.accent_color = "#9b59b6"  # a lavender/purple tint
    gui.interface_text_color = "#ffffff"

# simple custom main menu screen for Y-Edition
# use slightly higher priority than the stock menu so ours takes effect
init -499 screen main_menu():
    tag menu
    # solid purple background
    add Solid("#2e0854")

    # title and yuri portrait
    vbox:
        xpos 0.5
        ypos 0.15
        xanchor 0.5
        yanchor 0.5

        text "DDLC - Y Edition" size 60 color "#ffffff" xalign 0.5 yalign 0.5
        add "yuri/0b.png" xalign 0.5 yalign 0.5

    # navigation buttons
    vbox:
        xpos 0.5
        ypos 0.5
        xanchor 0.5
        yanchor 0.5
        spacing 20

        textbutton "Start" action Start() style "navigation_button"
        textbutton "Load" action ShowMenu("load") style "navigation_button"
        textbutton "Preferences" action ShowMenu("preferences") style "navigation_button"
        textbutton "Quit" action Quit(confirm=False) style "navigation_button"

    key "K_ESCAPE" action Quit(confirm=False)
