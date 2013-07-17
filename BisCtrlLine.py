import sublime
import sublime_plugin
import os


class BisCtrlCommand(sublime_plugin.WindowCommand):
    def run(self):
        self.window.show_input_panel("MAPPER Control Line:", "", self.on_done, None, None)
        pass

    def on_done(self, text):
        if self.window.active_view():
            self.window.active_view().run_command("bis_exec", {"text": text})


class BisExecCommand(sublime_plugin.TextCommand):

    def run(self, edit, text):

        # Get Path and User variables
        appdata = os.environ['USERPROFILE']
        app = 'sublwatcher'
        bis_cmd_file = 'BisCmd.bis'
        file_path = appdata + '\\' + app + '\\' + bis_cmd_file
        sublime.status_message("Writing BisCmd file")

        # Write file to path
        with open(file_path, "w") as textfile:
            textfile.write(text)
