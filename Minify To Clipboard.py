import sublime, sublime_plugin
from subprocess import Popen, PIPE, STDOUT
import re

class MinifyJsToClipboardCommand(sublime_plugin.TextCommand):
	def run(self, edit):
		selections = self.view.sel() # RegionSet
		selbody = ''
		for sel in selections:
			selbody = selbody + self.view.substr(sel)

		p = Popen(['uglifyjs'], stdout=PIPE, stdin=PIPE, stderr=PIPE)
		out = p.communicate(input=selbody)
		# print output
		if re.search('^\s$',out[1]):
			# no errors. return the minified output
			sublime.set_clipboard(out[0])
		else:
			sublime.set_clipboard("/* [ERROR in provided JavaScript] */")
			
