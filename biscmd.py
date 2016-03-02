import sublime
import sublime_plugin
import re
import os


class BisCtrlCommand(sublime_plugin.WindowCommand):

    def run(self):
        self.window.show_input_panel("BIS Control Line:", "", self.on_done, None, None)
        pass

    def on_done(self, text):
        if self.window.active_view():
            self.window.active_view().run_command("bis_exec", {"text": text})


class BisExecCommand(sublime_plugin.TextCommand):

    def run(self, edit, text):

        # Get Path and User variables
        global_settings = sublime.load_settings('BIS.sublime-settings')
        appdata = os.environ['USERPROFILE']
        app = 'sublwatcher'
        sublime.status_message("Writing BisCmd file")
        file_name = self.view.file_name()
        filename_filter = global_settings.get('filename_filter', '.*')
        print("Filename filter" + filename_filter)

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
