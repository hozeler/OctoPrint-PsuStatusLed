# coding=utf-8
from __future__ import absolute_import

import octoprint.plugin

class PsuStatusLedPlugin(octoprint.plugin.StartupPlugin,
                       octoprint.plugin.TemplatePlugin,
                       octoprint.plugin.SettingsPlugin,
                       octoprint.plugin.AssetPlugin):
	def on_after_startup(self):
		self._logger.info("PSU Status Led! (more: %s)" % self._settings.get(["url"]))

	def get_settings_defaults(self):
		return dict(url="https://en.wikipedia.org/wiki/Hello_world")

	def get_template_configs(self):
		return [
			dict(type="navbar", custom_bindings=False),
			dict(type="settings", custom_bindings=False)
		]

	def get_assets(self):
		return dict(
			js=["js/psustatusled.js"],
			css=["css/psustatusled.css"],
			less=["less/psustatusled.less"]
		)

__plugin_name__ = "Psu Status Led"
__plugin_pythoncompat__ = ">=2.7,<4"
__plugin_implementation__ = PsuStatusLedPlugin()
