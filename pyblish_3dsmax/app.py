# Standard library
import os

# Pyblish libraries
import pyblish
import pyblish.api

# Import 3dsmax libraries
from pymxs import runtime as rt

# Local libraries
from pyblish_3dsmax import plugins
from Qt import QtWidgets


def register_host():
    """Register supported hosts"""
    pyblish.api.register_host("3dsmax")


def deregister_host():
    """Register supported hosts"""
    pyblish.api.deregister_host("3dsmax")


def register_plugins():
    # Register accompanying plugins
    plugin_path = os.path.dirname(plugins.__file__)
    pyblish.api.register_plugin_path(plugin_path)
    print("pyblish: Registered %s" % plugin_path)


def deregister_plugins():
    plugin_path = os.path.dirname(plugins.__file__)
    pyblish.api.deregister_plugin_path(plugin_path)


def _discover_gui():
    """Return the most desirable of the currently registered GUIs"""

    # Prefer last registered
    guis = reversed(pyblish.api.registered_guis())

    for gui in guis:
        try:
            gui = __import__(gui)
        except (ImportError, AttributeError):
            continue
        else:
            return gui


def show(main_widget):
    """Try showing the most desirable GUI."""
    app = _discover_gui()
    app.settings.WindowTitle = "Pyblish (3dsmax)"
    app.show(main_widget)


def setup():
    """Setup integration.

    Register plug-ins and integrate into the host

    """
    pyblish.api.register_gui('pyblish_lite')
    register_plugins()
    register_host()
    print("pyblish: Pyblish loaded successfully.")
    main_widget = get_main_widget()
    show(main_widget)


def get_main_widget():
    """Get 3dsmax main window."""
    return QtWidgets.QWidget.find(rt.windows.getMAXHWND())


def get_main_menubar(main_widget):
    """Get main Menubar by 3dsmax main windies."""
    return [i for i in main_widget.findChildren(QtWidgets.QMenuBar)][0]


def setup_menu():
    main_widget = get_main_widget()
    menu_bar = get_main_menubar(main_widget)
    action = QtWidgets.QAction("Pyblish", menu_bar)
    action.triggered.connect(setup)
    menu_bar.addAction(action)
