import sublime
import sublime_plugin
from glob import glob
from os.path import isdir, split as splitpath


class MenuOpenFromCurrentDirCommand(sublime_plugin.TextCommand):

	def run(self, edit):
		path = self.view.file_name()
		path, name = splitpath(path)
		ext = name.split('.')[-1]
		pathlen = len(path) + 1
		files = [file[pathlen:] for file in glob(path + '\\*') if not isdir(file)]
		fileswithext = [file for file in files if file.endswith(ext)]
		restoffiles = [file for file in files if not file.endswith(ext)]
		files = fileswithext + restoffiles

		def on_done(index):
			if index != -1:
				self.view.window().open_file(files[index])

		self.view.window().show_quick_panel(files, on_done)
