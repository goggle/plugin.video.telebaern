# -*- coding: utf-8 -*-

# Copyright (C) 2018 Alexander Seiler
#
#
# This file is part of plugin.video.telebaern.
#
# plugin.video.telebaern is free software: you can redistribute it and/or
# modify it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# plugin.video.telebaern is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with plugin.video.telebaern.
# If not, see <http://www.gnu.org/licenses/>.

# import sys
# import traceback

# import json
# import socket
# import urllib
# import urlparse

import xbmc
# import xbmcgui
# import xbmcplugin
import xbmcaddon

import azmedien

def get_boolean_setting(label):
    """
    Retrieve the boolean value of a setting switch.

    Keyword arguments:
    label -- the settings label
    """
    return REAL_SETTINGS.getSetting(label) == 'true'


ADDON_ID = 'plugin.video.telebaern'
REAL_SETTINGS = xbmcaddon.Addon(id=ADDON_ID)
ADDON_NAME = REAL_SETTINGS.getAddonInfo('name')
ADDON_VERSION = REAL_SETTINGS.getAddonInfo('version')
ICON = REAL_SETTINGS.getAddonInfo('icon')
FANART = REAL_SETTINGS.getAddonInfo('fanart')
LANGUAGE = REAL_SETTINGS.getLocalizedString
PROFILE = xbmc.translatePath(
    REAL_SETTINGS.getAddonInfo('profile')).decode("utf-8")
HOST = 'telebaern.tv'
# DEBUG = REAL_SETTINGS.getSetting('Enable_Debugging') == 'true'


# socket.setdefaulttimeout(TIMEOUT)


# General helper functions:


def run():
    """
    Run the plugin.
    """
    customer = azmedien.CustomerAddon(addon_id=ADDON_ID, real_settings=REAL_SETTINGS, icon=ICON, fanart=FANART)
    azmedien.run(customer, host=HOST)
    
