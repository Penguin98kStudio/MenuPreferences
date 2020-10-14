import sublime
import sublime_plugin


class MenuFileCommandsCommand(sublime_plugin.TextCommand):

	def run(self, edit):
		view = self.view
		window = view.window()
		settings = sublime.load_settings("MenuPenguinLists.sublime-settings")
		commandlist = settings.get("file_commands_list")

		def on_done(index):
			if index != -1:
				settings = sublime.load_settings(
					"MenuPenguinLists.sublime-settings"
					)
				settings2 = sublime.load_settings(
					"MenuPenguinDefault.sublime-settings"
					)
				frequencylist = settings.get("file_commands_freq")
				commandlist = settings.get("file_commands_list")

				#load command
				command = commandlist[index][2]

				if settings2.get("enable_sort_for_file_commands"):
					#adjust order
					frequencylist[index] += 1
					frequencylist, commandlist = (
						list(_) for _ in
						zip(*sorted(zip(frequencylist, commandlist), reverse=True))
						)
					settings.set("file_commands_freq", frequencylist)
					settings.set("file_commands_list", commandlist)
					sublime.save_settings("MenuPenguinLists.sublime-settings")

				#run loaded command
				if type(command) == list:
					window.run_command(*command)
				else:
					window.run_command(command)

		window.show_quick_panel([command[1] for command in commandlist], on_done)
