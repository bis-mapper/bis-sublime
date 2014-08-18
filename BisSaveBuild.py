import sublime
import sublime_plugin
import re
import os


class BisSaveBuild(sublime_plugin.EventListener):
    def on_post_save(self, view):
        global_settings = sublime.load_settings('BIS.sublime-settings')
        print

        # See if we should build. A project level build_on_save setting
        # takes precedence. To be backward compatible, we assume the global
        # build_on_save to be true if not defined.
        should_build = view.settings().get('build_on_save', global_settings.get('build_on_save', True))

        # Load filename filter. Again, a project level setting takes precedence.
        filename_filter = view.settings().get('filename_filter', global_settings.get('filename_filter', '.*'))
        print("Filename filter" + filename_filter)

        if not should_build:
            return

        if not re.search(filename_filter, view.file_name()):
            return

        # Get Path and User variables
        appdata = os.environ['USERPROFILE']
        app = 'sublwatcher'
        bis_save_file = 'changes.txt'
        file_path = appdata + '\\' + app + '\\' + bis_save_file
        file_name = view.file_name()

        # Write file to path
        with open(file_path, "w") as textfile:
            textfile.write("modified" + "," + file_name + ", file, BisSaveBuild")
