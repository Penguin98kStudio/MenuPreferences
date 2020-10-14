import sublime
import sublime_plugin


class MenuTogglePreferencesCommand(sublime_plugin.TextCommand):

	def run(self, edit):
		view = self.view
		settings = view.settings()

		def getv(key):
			if type(key) == list:
				if len(key) == 4:
					return [key[-1], settings2.get(key[0]), key]
				else:
					return [key[0], settings.get(key[0].lower()), key]
			else:
				return [key, settings.get(key.lower()), key]

		def toggle(_, val, key):
			if type(key) == list:
				if len(key) == 4:
					if val == key[1]:
						settings2.set(key[0], key[2])
					else:
						settings2.set(key[0], key[1])
				else:
					if val == key[1]:
						settings.set(key[0].lower(), key[2])
					else:
						settings.set(key[0].lower(), key[1])
			else:
				settings.set(key.lower(), not val)

		def on_done(index):
			if index != -1:
				settings2 = sublime.load_settings(
					"MenuPenguinLists.sublime-settings"
					)
				settings3 = sublime.load_settings(
					"MenuPenguinDefault.sublime-settings"
					)
				preferences = settings2.get("preferences_list")
				freq = settings2.get("preferences_freq")
				toggle(*preferenceslist[index])
				if settings3.get("enable_sort_for_toggle"):
					# adjust Order
					freq[index] += 1
					freq, preferences = (
						list(_)
						for _ in zip(*sorted(zip(freq, preferences), reverse=True))
						)
					settings2.set("preferences_list", preferences)
					settings2.set("preferences_freq", freq)
					sublime.save_settings("MenuPenguinLists.sublime-settings")

		# preferences	=	[
		# 						"Fix_Indent_On_Line_Move",
		# 						"Word_Wrap",
		# 						"Line_Numbers",
		# 						["Draw_White_Space","selection","all"],
		# 						["plugin_mode", "extended", "disabled","Display_Number_Conversions"],
		# 						"Gutter",
		# 						"Indent_With_Tabs_On_Save",
		# 						"Scroll_Past_End",
		# 						"Show_Char_Code",
		# 					]
		settings2 = sublime.load_settings("MenuPenguinLists.sublime-settings")
		preferences = settings2.get("preferences_list")
		preferenceslist = [
			getv(pref[0]) if len(pref) == 1 else getv(pref) for pref in preferences
			]
		preferenceslist2 = [[pref[0], str(pref[1])] for pref in preferenceslist]
		view.window().show_quick_panel(preferenceslist2, on_done)
