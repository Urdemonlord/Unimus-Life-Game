## This file contains options that can be changed to customize your game.
##
## Lines beginning with two '#' marks are comments, and you shouldn't uncomment
## them. Lines beginning with a single '#' mark are commented-out code, and you
## may want to uncomment them when appropriate.

## Basics ######################################################################

## A human-readable name of the game.
define config.name = _("Unimus Life Game")

## Determines if the title given above is shown on the main menu screen.
define gui.show_name = True

## The version of the game.
define config.version = "demo"

## Text that is placed on the game's about screen.
define gui.about = _p("""
Selamat datang di Unimus Life Game!
Game ini membawa Anda ke dalam pengalaman ospek di Universitas Muhammadiyah Semarang.
Nikmati petualangan, tantangan, dan interaksi dengan teman-teman baru.
""")

## A short name for the game used for executables and directories in the built
## distribution.
define build.name = "UnimusLifeGame"

## Sounds and music ############################################################

## These three variables control which mixers are shown to the player by default.
define config.has_sound = True
define config.has_music = True
define config.has_voice = True

## Uncomment the following line to set an audio file that will be played while
## the player is at the main menu.
define config.main_menu_music = "music/main_menu_theme.mp3"  # Ganti dengan file musik yang sesuai

## Transitions #################################################################
##
## These variables set transitions that are used when certain events occur.
define config.enter_transition = dissolve
define config.exit_transition = dissolve
define config.intra_transition = dissolve
define config.after_load_transition = None
define config.end_game_transition = None

## Window management ###########################################################
##
## This controls when the dialogue window is displayed.
define config.window = "auto"

## Transitions used to show and hide the dialogue window
define config.window_show_transition = Dissolve(.2)
define config.window_hide_transition = Dissolve(.2)

## Preference defaults #########################################################

## Controls the default text speed.
default preferences.text_cps = 0

## The default auto-forward delay.
default preferences.afm_time = 15

## Save directory ##############################################################
define config.save_directory = "UnimusLifeGame-1732553819"

## Icon ########################################################################
define config.window_icon = "gui/window_icon.png"  # Ganti dengan ikon yang sesuai

## Build configuration #########################################################
init python:

    ## The following functions take file patterns.
    build.classify('**~', None)
    build.classify('**.bak', None)
    build.classify('**/.**', None)
    build.classify('**/#**', None)
    build.classify('**/thumbs.db', None)

    build.documentation('*.html')
    build.documentation('*.txt')

## A Google Play license key is required to perform in-app purchases.
# define build.google_play_key = "..."

## The username and project name associated with an itch.io project.
# define build.itch_project = "renpytom/test-project"
