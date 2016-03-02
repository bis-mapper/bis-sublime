import sublime
import sublime_plugin
import re
import os
#===============================================================================
#
#
#
#===============================================================================
class IbldInputCommand(sublime_plugin.WindowCommand):
    def run(self, icmd, itype, iscript):
        if iscript == "Y":
            self.webscript = ",Y"
        else:
            self.webscript = ""
        if itype == "S":
            self.ptype = "Service"
        else:
            self.ptype = "Resource"
        self.text = "IBLD," + icmd + "," + itype
        self.counter = 0
        self.prompts = ["Appname(or CAB):", self.ptype + " Name:"]
        self.show_prompt()

    def on_done(self, text):
        self.text += "," + text
        self.counter += 1
        if self.counter < len(self.prompts):
            self.show_prompt()
        else:
            self.input_done()

    def input_done(self):
        if self.window.active_view():
            self.window.active_view().run_command("ibld_exec", {"text": self.text + self.webscript})

    def show_prompt(self):
        self.window.show_input_panel(self.prompts[self.counter], "", self.on_done, None, None)
#===============================================================================
#
#
#
#===============================================================================
class IbldExecCommand(sublime_plugin.TextCommand):

    def run(self, edit, text):

        # Get Path and User variables
        global_settings = sublime.load_settings('BIS.sublime-settings')
        appdata = os.environ['USERPROFILE']
        app = 'sublwatcher'
        sublime.status_message("Writing BisCmd file")
        file_name = self.view.file_name()
        filename_filter = global_settings.get('filename_filter', '.*')

        if not re.search(filename_filter, file_name):
            file_name = appdata + '\\' + app + '\\'

        pos = file_name.find('site-')
        pos = pos + 5
        site = file_name[pos]
        bis_cmd_file = 'site-' + site + '\\changes.txt'
        file_path = appdata + '\\' + app + '\\' + bis_cmd_file

        # Write file to path
        with open(file_path, "w") as textfile:
            textfile.write("BisCmd" + "," + file_name + "," + "input" + "," + text)
#===============================================================================
#
#
#
#===============================================================================
