################################################################################
## Initialization
################################################################################

## The init offset statement causes the initialization statements in this file
## to run before init statements in any other file.
init offset = -2

## Calling gui.init resets the styles to sensible default values, and sets the
## width and height of the game.
init python:
    gui.init(1920, 1080)

## Enable checks for invalid or unstable properties in screens or transforms
define config.check_conflicting_properties = True

################################################################################
## GUI Configuration Variables
################################################################################

## Colors ######################################################################
##
## The colors of text in the interface.

## Unimus accent color
define gui.accent_color = '#1500fbff'  # Warna biru khas Unimus

## The color used for a text button when it is neither selected nor hovered.
define gui.idle_color = '#888888'

## The small color is used for small text, which needs to be brighter/darker to
## achieve the same effect.
define gui.idle_small_color = '#aaaaaa'

## The color that is used for buttons and bars that are hovered.
define gui.hover_color = '#66a3e0'

## The color used for a text button when it is selected but not focused.
define gui.selected_color = '#ffffff'

## The color used for a text button when it cannot be selected.
define gui.insensitive_color = '#8888887f'

## Colors used for the portions of bars that are not filled in.
define gui.muted_color = '#002851'
define gui.hover_muted_color = '#003d7a'

## The colors used for dialogue and menu choice text.
define gui.text_color = '#ffffff'
define gui.interface_text_color = '#ffffff'

## Fonts and Font Sizes ########################################################

## The font used for in-game text.
define gui.text_font = "DejaVuSans.ttf"  # Ganti dengan font yang sesuai jika ada

## The font used for character names.
define gui.name_text_font = "DejaVuSans.ttf"

## The font used for out-of-game text.
define gui.interface_text_font = "DejaVuSans.ttf"

## The size of normal dialogue text.
define gui.text_size = 33

## The size of character names.
define gui.name_text_size = 45

## The size of text in the game's user interface.
define gui.interface_text_size = 33

## The size of labels in the game's user interface.
define gui.label_text_size = 36

## The size of text on the notify screen.
define gui.notify_text_size = 24

## The size of the game's title.
define gui.title_text_size = 75

## Main and Game Menus #########################################################

# Konfigurasi Latar Belakang Menu 

# Definisikan path gambar
define gui.main_menu_background = "gui/unimus_main_menu.png"
define gui.game_menu_background = "gui/unimus_game_menu.png"

# Gunakan transform di style
style main_menu:
    background Transform(
        gui.main_menu_background, 
        zoom=1.0,      # Atur skala sesuai kebutuhan
        xalign=0.5,    # Rata tengah horizontal
        yalign=0.5     # Rata tengah vertikal
    )

style game_menu:
    background Transform(
        gui.game_menu_background, 
        zoom=1.0,      # Atur skala sesuai kebutuhan
        xalign=0.5,    # Rata tengah horizontal
        yalign=0.5     # Rata tengah vertikal
    )

# Fungsi opsional untuk resize (jika diperlukan)
init python:
    def resize_background(image_path, zoom=1.0, xalign=0.5, yalign=0.5):
        """
        Fungsi untuk membuat transform background
        
        :param image_path: Path gambar
        :param zoom: Skala gambar
        :param xalign: Perataan horizontal
        :param yalign: Perataan vertikal
        :return: Transform objek
        """
        return Transform(
            image_path, 
            zoom=zoom, 
            xalign=xalign, 
            yalign=yalign
        )

## Dialogue ####################################################################
##
## These variables control how dialogue is displayed on the screen one line at a
## time.

## The height of the textbox containing dialogue.
define gui.textbox_height = 278

## The placement of the textbox vertically on the screen.
define gui.textbox_yalign = 1.0

## The placement of the speaking character's name, relative to the textbox.
define gui.name_xpos = 360
define gui.name_ypos = 0

## The horizontal alignment of the character's name.
define gui.name_xalign = 0.0

## The width, height, and borders of the box containing the character's name.
define gui.namebox_width = None
define gui.namebox_height = None

## The borders of the box containing the character's name.
define gui.namebox_borders = Borders(5, 5, 5, 5)

## If True, the background of the namebox will be tiled.
define gui.namebox_tile = False

## The placement of dialogue relative to the textbox.
define gui.dialogue_xpos = 402
define gui.dialogue_ypos = 75

## The maximum width of dialogue text, in pixels.
define gui.dialogue_width = 1116

## The horizontal alignment of the dialogue text.
define gui.dialogue_text_xalign = 0.0

## Buttons #####################################################################
##
## These variables control aspects of how buttons are displayed.

## The width and height of a button, in pixels.
define gui.button_width = None
define gui.button_height = None

## The borders on each side of the button.
define gui.button_borders = Borders(6, 6, 6, 6)

## If True, the background image will be tiled.
define gui.button_tile = False

## The font used by the button.
define gui.button_text_font = gui.interface_text_font

## The size of the text used by the button.
define gui.button_text_size = gui.interface_text_size

## The color of button text in various states.
define gui.button_text_idle_color = gui.idle_color
define gui.button_text_hover_color = gui.hover_color
define gui.button_text_selected_color = gui.selected_color
define gui.button_text_insensitive_color = gui.insensitive_color

## The horizontal alignment of the button text.
define gui.button_text_xalign = 0.0

## Choice Buttons ##############################################################
##
## Choice buttons are used in the in-game menus.

define gui.choice_button_width = 1185
define gui.choice_button_height = None
define gui.choice_button_tile = False
define gui.choice_button_borders = Borders(150, 8, 150, 8)
define gui.choice_button_text_font = gui.text_font
define gui.choice_button_text_size = gui.text_size
define gui.choice_button_text_xalign = 0.5
define gui.choice_button_text_idle_color = '#888888'
define gui.choice_button_text_hover_color = "#ffffff"
define gui.choice_button_text_insensitive_color = '#8888887f'

## File Slot Buttons ###########################################################
##
## A file slot button is a special kind of button.

## The save slot button.
define gui.slot_button_width = 414
define gui.slot_button_height = 309
define gui.slot_button_borders = Borders(15, 15, 15, 15)
define gui.slot_button_text_size = 21
define gui.slot_button_text_xalign = 0.5
define gui.slot_button_text_idle_color = gui.idle_small_color
define gui.slot_button_text_selected_idle_color = gui.selected_color
define gui.slot_button_text_selected_hover_color = gui.hover_color

## The width and height of thumbnails used by the save slots.
define config.thumbnail_width = 384
define config.thumbnail_height = 216

## The number of columns and rows in the grid of save slots.
define gui.file_slot_cols = 3
define gui.file_slot_rows = 2

## Positioning and Spacing #####################################################
##
## These variables control the positioning and spacing of various user interface
## elements.

## The position of the left side of the navigation buttons.
define gui.navigation_xpos = 60

## The vertical position of the skip indicator.
define gui.skip_ypos = 15

## The vertical position of the notify screen.
define gui.notify_ypos = 68

## The spacing between menu choices.
define gui.choice_spacing = 33

## Buttons in the navigation section of the main and game menus.
define gui.navigation_spacing = 6

## Controls the amount of spacing between preferences.
define gui.pref_spacing = 15

## Controls the amount of spacing between preference buttons.
define gui.pref_button_spacing = 0

## The spacing between file page buttons.
define gui.page_spacing = 0

## The spacing between file slots.
define gui.slot_spacing = 15

## The position of the main menu text.
define gui.main_menu_text_xalign = 1.0

## Frames ######################################################################
##
## These variables control the look of frames that can contain user interface
## components when an overlay or window is not present.

## Generic frames.
define gui.frame_borders = Borders(6, 6, 6, 6)

## The frame that is used as part of the confirm screen.
define gui.confirm_frame_borders = Borders(60, 60, 60, 60)

## The frame that is used as part of the skip screen.
define gui.skip_frame_borders = Borders(24, 8, 75, 8)

## The frame that is used as part of the notify screen.
define gui.notify_frame_borders = Borders(24, 8, 60, 8)

## Should frame backgrounds be tiled?
define gui.frame_tile = False

## Bars, Scrollbars, and Sliders ###############################################
##
## These control the look and size of bars, scrollbars, and sliders.

## The height of horizontal bars, scrollbars, and sliders.
define gui.bar_size = 38
define gui.scrollbar_size = 18
define gui.slider_size = 38

## True if bar images should be tiled.
define gui.bar_tile = False
define gui.scrollbar_tile = False
define gui.slider_tile = False

## Horizontal borders.
define gui.bar_borders = Borders(6, 6, 6, 6)
define gui.scrollbar_borders = Borders(6, 6, 6, 6)
define gui.slider_borders = Borders(6, 6, 6, 6)

## Vertical borders.
define gui.vbar_borders = Borders(6, 6, 6, 6)
define gui.vscrollbar_borders = Borders(6, 6, 6, 6)
define gui.vslider_borders = Borders(6, 6, 6, 6)

## What to do with unscrollable scrollbars in the game menu.
define gui.unscrollable = "hide"

## History #####################################################################
##
## The history screen displays dialogue that the player has already dismissed.

## The number of blocks of dialogue history Ren'Py will keep.
define config.history_length = 250

## The height of a history screen entry.
define gui.history_height = 210

## Additional space to add between history screen entries.
define gui.history_spacing = 0

## The position, width, and alignment of the label giving the name of the
## speaking character.
define gui.history_name_xpos = 233
define gui.history_name_ypos = 0
define gui.history_name_width = 233
define gui.history_name_xalign = 1.0

## The position, width, and alignment of the dialogue text.
define gui.history_text_xpos = 255
define gui.history_text_ypos = 3
define gui.history_text_width = 1110
define gui.history_text_xalign = 0.0

## NVL-Mode ####################################################################
##
## The NVL-mode screen displays the dialogue spoken by NVL-mode characters.

## The borders of the background of the NVL-mode background window.
define gui.nvl_borders = Borders(0, 15, 0, 30)

## The maximum number of NVL-mode entries Ren'Py will display.
define gui.nvl_list_length = 6

## The height of an NVL-mode entry.
define gui.nvl_height = 173

## The spacing between NVL-mode entries when gui.nvl_height is None.
define gui.nvl_spacing = 15

## The position, width, and alignment of the label giving the name of the
## speaking character.
define gui.nvl_name_xpos = 645
define gui.nvl_name_ypos = 0
define gui.nvl_name_width = 225
define gui.nvl_name_xalign = 1.0

## The position, width, and alignment of the dialogue text.
define gui.nvl_text_xpos = 675
define gui.nvl_text_ypos = 12
define gui.nvl_text_width = 885
define gui.nvl_text_xalign = 0.0

## The position, width, and alignment of nvl_thought text.
define gui.nvl_thought_xpos = 360
define gui.nvl_thought_ypos = 0
define gui.nvl_thought_width = 1170
define gui.nvl_thought_xalign = 0.0

## The position of nvl menu_buttons.
define gui.nvl_button_xpos = 675
define gui.nvl_button_xalign = 0.0

## Localization ################################################################

## This controls where a line break is permitted.
define gui.language = "unicode"

################################################################################
## Mobile devices
################################################################################

init python:

    ## This increases the size of the quick buttons to make them easier to touch
    ## on tablets and phones.
    @gui.variant
    def touch():
        gui.quick_button_borders = Borders(60, 21, 60, 0)

    ## This changes the size and spacing of various GUI elements to ensure they
    ## are easily visible on phones.
    @gui.variant
    def small():
        ## Font sizes.
        gui.text_size = 45
        gui.name_text_size = 54
        gui.notify_text_size = 38
        gui.interface_text_size = 45
        gui.button_text_size = 45
        gui.label_text_size = 51

        ## Adjust the location of the textbox.
        gui.textbox_height = 360
        gui.name_xpos = 120
        gui.dialogue_xpos = 135
        gui.dialogue_width = 1650

        ## Change the size and spacing of various things.
        gui.slider_size = 54

        gui.choice_button_width = 1860
        gui.choice_button_text_size = 45

        gui.navigation_spacing = 30
        gui.pref_button_spacing = 15

        gui.history_height = 285
        gui.history_text_width = 1035

        gui.quick_button_text_size = 30

        ## File button layout.
        gui.file_slot_cols = 2
        gui.file_slot_rows = 2

        ## NVL-mode.
        gui.nvl_height = 255

        gui.nvl_name_width = 458
        gui.nvl_name_xpos = 488

        gui.nvl_text_width = 1373
        gui.nvl_text_xpos = 518
        gui.nvl_text_ypos = 8

        gui.nvl_thought_width = 1860
        gui.nvl_thought_xpos = 30

        gui.nvl_button_width = 1860
        gui.nvl_button_xpos = 30
