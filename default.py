# -*- coding: utf-8 -*-

""" ^ SECTION 1:
    This should be at the top of your code to declare the type of text
    format you're using. Without this you may find some text editors save
    it in an incompatible format and this can make bug tracking extremely
    confusing! More info here: https://www.python.org/dev/peps/pep-0263/
"""

#----------------------------------------------------------------

"""
    SECTION 2:
    This is where you'd put your license details, the GPL3 license 
    is the most common to use as it makes it easy for others to fork
    and improve upon your code. If you're re-using others code ALWAYS
    check the license first, removal of licenses is NOT allowed and you
    generally have to keep to the same license used in the original work
    (check license details as some do differ).

    Although not all licenses require it (some do, some don't),
    you should always give credit to the original author(s). Someone may have spent
    months if not years on the code so really it's the very least you can do if
    you choose to use their work as a base for your own.
"""
# License: GPL (http://www.gnu.org/licenses/gpl-3.0.html)
# Addon: My YouTube Add-on
# Author: Arcade DreamWorks

#----------------------------------------------------------------

"""
    SECTION 3:
    This is your global imports, any modules you need to import code from
    are added here. You'll see a handful of the more common imports below.
"""
import os           # access operating system commands
import xbmc         # the base xbmc functions, pretty much every add-on is going to need at least one function from here
import xbmcaddon    # pull addon specific information such as settings, id, fanart etc.
import xbmcplugin   # contains functions required for creating directory structure style add-ons (plugins)

# The following are often used, we are not using them in this particular file so they are commented out

# import re           # allows use of regex commands, if you're intending on scraping you'll need this
# import xbmcgui      # gui based functions, contains things like creating dialog pop-up windows

from koding import route, Addon_Setting, Add_Dir, Find_In_Text, Open_URL, OK_Dialog
from koding import Open_Settings, Play_Video, Run, Text_File

#------------------------------------------------------------

"""
    SECTION 4:
    These are our global variables, anything we set here can be accessed by any of
    our functions later on. Please bare in mind though that if you change the value
    of a global variable from inside a function the value will revert back to the
    value set here once that function has completed.
"""
debug        = Addon_Setting(setting='debug')       # Grab the setting of our debug mode in add-on settings
addon_id     = xbmcaddon.Addon().getAddonInfo('id') # Grab our add-on id

# Set the base plugin url you want to hook into
BASE  = "plugin://plugin.video.youtube/playlist/"
BASE2 = "plugin://plugin.video.youtube/channel/"

# Set each of your YouTube playlist id's
YOUTUBE_CHANNEL_ID_1 = "UCi623vUlmMZGgZbVcmzHc7Q"
YOUTUBE_CHANNEL_ID_2 = "PLZmmdCFFYCOWp8dEGbsHnKySFuNAn-0i5"
YOUTUBE_CHANNEL_ID_3 = "PLCpdvYcv59AgI_UbY4C1GhwFZ5CQL3N5c"
YOUTUBE_CHANNEL_ID_4 = "PLCpdvYcv59AjPl1d0DTugILsmMlVRhq4u"
YOUTUBE_CHANNEL_ID_5 = "UCaPwSXblS8F0owlKHGc6huw"
YOUTUBE_CHANNEL_ID_6 = "PL8D4Iby0Bmm_RcdU5KgREpDbsQAfSlw-I"
YOUTUBE_CHANNEL_ID_7 = "PL8D4Iby0Bmm8wob_KNgW8crCdQ5pxA2Pv"
YOUTUBE_CHANNEL_ID_8 = "UCxr8MeszCjWA-dtclQsv6vQ"

#----------------------------------------------------------------

"""
    SECTION 5:
    Add our custom functions in here, it's VERY important these go in this section
    as the code in section 6 relies on these functions. If that code tries to run
    before these functions are declared the add-on will fail.

    You'll notice each function in here has a decorator above it (an @route() line of code),
    this assigns a mode to the function so it can be called with Add_Dir and it also tells
    the code what paramaters to send through. For example you'll notice the Main_Menu() function
    we've assigned to the mode "main" - this means if we ever want to get Add_Dir to open that
    function we just use the mode "main". This particular function does not require any extra
    params to be sent through but if you look at the Simple_Dialog() function you'll see we send through
    2 different paramaters (title and msg), if you look at the Add_Dir function in Main_Menu()
    on line 106 you'll see we've sent these through as a dictionary. Using that same format you can send
    through as many different params as you wish.
"""

#----------------------------------------------------------------
# This is the main menu we open into
@route(mode='main_menu')
def Main_Menu():

        
# Add some YT Playlists (see we're using BASE as the url)
    Add_Dir( 
        name="Eat Bulaga HD", url=BASE2+YOUTUBE_CHANNEL_ID_1+"/", folder=True,
        icon="https://m.media-amazon.com/images/M/MV5BZTUwZjJlMzgtNWQyOC00NGI3LTg3NTktNGQ1Yjc2MThlMGU3XkEyXkFqcGdeQXVyNTI5NjIyMw@@._V1_.jpg")

    Add_Dir( 
        name="Sugod Bahay HD", url=BASE+YOUTUBE_CHANNEL_ID_2+"/", folder=True,
        icon="http://s2.dmcdn.net/Ie5LQ.jpg")

    Add_Dir( 
        name="24 Oras HD", url=BASE+YOUTUBE_CHANNEL_ID_3+"/", folder=True,
        icon="https://i.ytimg.com/vi/fI7BZd1-wqc/maxresdefault.jpg")

	
    Add_Dir( 
        name="Unang Hirit HD", url=BASE+YOUTUBE_CHANNEL_ID_4+"/", folder=True,
        icon="https://i.ytimg.com/vi/uLZ3fFuuMRk/maxresdefault.jpg")

# Add some YT channels (see we're using BASE2 as the url for this one)
    Add_Dir( 
        name="Top Hits OPM Karaoke Playlist", url=BASE2+YOUTUBE_CHANNEL_ID_5+"/", folder=True,
        icon="http://tag911.ae/wp-content/uploads/2015/08/1a4.jpg")
		
    Add_Dir( 
        name="R&B Karaoke Playlist", url=BASE+YOUTUBE_CHANNEL_ID_6+"/", folder=True,
        icon="http://cdnaws.recis.io/i/img/00/68/71/1e_e47ac8_lg288.jpg")
		
    Add_Dir( 
        name="Rap/HipHop Karaoke Playlist", url=BASE+YOUTUBE_CHANNEL_ID_7+"/", folder=True,
        icon="http://cdnaws.recis.io/i/img/00/68/71/2d_2a1c43_lg288.jpg")
		
	 
#----------------------------------------------------------------
# A basic OK Dialog
@route(mode='koding_settings')
def Koding_Settings():
    Open_Settings()
#----------------------------------------------------------------
# A basic OK Dialog
@route(mode='simple_dialog', args=['title','msg'])
def Simple_Dialog(title,msg):
    OK_Dialog(title, msg)
#----------------------------------------------------------------

"""
    SECTION 6:
    Essential if creating list items, this tells kodi we're done creating our list items.
    The list will not populate without this. In the run command you need to set default to
    whatever route you want to open into, in this example the 'main_menu' route which opens the
    Main_Menu() function up at the top.
"""
if __name__ == "__main__":
    Run(default='main_menu')
    xbmcplugin.endOfDirectory(int(sys.argv[1]))