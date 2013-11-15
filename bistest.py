import sublime
import sublime_plugin
import os

# class RunSingleBisTest(sublime_plugin.WindowCommand):

#   def window(self):
#       return self.view.window()

#   def get_file_name(self):
#       self.folder_name, self.file_name = os.path.split(file_name)
#       self.partition_folder = partition_folder
#       self.absolute_path = file_name
#   def parent_dir_name(self):
#     head_dir, tail_dir = os.path.split(self.folder_name)
#     return tail_dir
#   def get_project_root(self): return self.folder_name
#   def find_project_root(self):
#     to_find = os.sep + self.partition_folder + os.sep
#     project_root, _, _ = self.absolute_path.partition(to_find)
#     return project_root
#   def relative_file_path(self):
#     to_find = os.sep + self.partition_folder + os.sep
#     _, _, relative_path = self.absolute_path.partition(to_find)
#     return self.partition_folder + os.sep + relative_path
#   def get_current_line_number(self, view):
#     char_under_cursor = view.sel()[0].a
#     return view.rowcol(char_under_cursor)[0] + 1

#   def load_config(self):
#     s = sublime.load_settings("BisTest.sublime-settings")
#     global HIDE_PANEL; HIDE_PANEL = s.get("hide_panel")
#     global SAVE_ON_RUN; SAVE_ON_RUN = s.get("save_on_run")
#     # global SYNTAX; SYNTAX = s.get('syntax')
#     # global THEME; THEME = s.get('theme')

#   def save_all(self):
#     if SAVE_ON_RUN:
#       self.window().run_command("save_all")

#   def run_shell_command(self, command, working_dir):
#     if not command:
#       return False
#     self.view.window().run_command("exec", {
#       "cmd": [command],
#       "shell": True,
#       "working_dir": working_dir,
#       "file_regex": r"([^ ]*\.bis):?(\d*)"
#     })
#     self.display_results()
#     return True

#   # def is_enabled(self): return 'run_test' in self.file_type().features()
#   def run(self):
#     self.load_config()
#     self.save_all()
#     file_name = self.view.file_name()
#     self.panel = self.window.get_output_panel("exec")
#     self.window.run_command("show_panel", {"panel": "output.exec"})
#     # self.panel.set_syntax_file(SYNTAX)


    # file = self.file_type()
    # command = file.run_single_test_command(self.view)
    # self.run_shell_command(command, file.get_project_root())

class BisTestCommand(sublime_plugin.WindowCommand):

    def load_config(self):
        s = sublime.load_settings("BisTest.sublime-settings")
        global HIDE_PANEL; HIDE_PANEL = s.get("hide_panel")
        global SAVE_ON_RUN; SAVE_ON_RUN = s.get("save_on_run")
        # global SYNTAX; SYNTAX = s.get('syntax')
        # global THEME; THEME = s.get('theme')

    def run(self):
        self.load_config()
        # self.window.show_input_panel("MAPPER Control Line:", "", self.on_done, None, None)

        self.panel = self.window.get_output_panel("exec")
        self.window.run_command("show_panel", {"panel": "output.exec"})
        self.panel.set_syntax_file(SYNTAX)
        if HIDE_PANEL:
          self.window.run_command("hide_panel")

        pass

    def display_results(self):
        display = ShowInScratch(self.window()) if USE_SCRATCH else ShowInPanel(self.window())
        display.display_results()


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
        file_name = self.view.file_name()

        # Write file to path
        with open(file_path, "w") as textfile:
            textfile.write(text + "|" + file_name)
