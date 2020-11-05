# coding=utf-8
from __future__ import absolute_import

import octoprint.plugin

class TouchtestPlugin(octoprint.plugin.SettingsPlugin,
                      octoprint.plugin.AssetPlugin,
                      octoprint.plugin.TemplatePlugin):

    ##~~ SettingsPlugin mixin

    def get_settings_defaults(self):
        return dict(
            bedWidth=200.0,
            bedDepth=200.0,
            edgeOffset=15.0,
            feedrate=7500.0,
        )

    ##~~ AssetPlugin mixin

    def get_assets(self):
        # Define your plugin's asset files to automatically include in the
        # core UI here.
        return dict(
            js=["js/touchtest.js"],
            css=["css/touchtest.css"],
            less=["less/touchtest.less"]
        )

    ##~~ Softwareupdate hook

    def get_update_information(self):
        # Define the configuration for your plugin to use with the Software Update
        # Plugin here. See https://github.com/foosel/OctoPrint/wiki/Plugin:-Software-Update
        # for details.
        return dict(
            touchtest=dict(
                displayName="Touchtest Plugin",
                displayVersion=self._plugin_version,

                # version check: github repository
                type="github_release",
                user="Peaches491",
                repo="OctoPrint-Touchtest",
                current=self._plugin_version,

                # update method: pip
                pip="https://github.com/Peaches491/OctoPrint-Touchtest/archive/{target_version}.zip"
            )
        )

    def get_template_configs(self):
        return [
            dict(type="sidebar", name="Bed Leveling Touch Points", icon="sort-by-attributes-alt"),
            dict(type="settings", custom_bindings=False)
        ]


__plugin_name__ = "Touchtest Plugin"
__plugin_pythoncompat__ = ">=2.7,<4"  # python 2 and 3

def __plugin_load__():
    global __plugin_implementation__
    __plugin_implementation__ = TouchtestPlugin()

    global __plugin_hooks__
    __plugin_hooks__ = {
        "octoprint.plugin.softwareupdate.check_config": __plugin_implementation__.get_update_information
    }

