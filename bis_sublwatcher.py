import sublime
import sublime_plugin
import re
import os
from random import randint
#===============================================================================
#
#
#
#===============================================================================
class AppCurrentCommand(sublime_plugin.TextCommand):

    def run(self, edit, text):

        dirtquote = randint(1, 10)
        print(randint(1,10))
        if dirtquote == 1:
            quote = "\"My name is Joe Dirte, I added an e to the end, cause it sounds cool.\" ~Joe Dirt\n\n"
        elif dirtquote == 2:
            quote = "\"Life's a garden, dig it.\" ~Joe Dirt\n\n"
        elif dirtquote == 3:
            quote = "\"People say Joe Dirt's a weird name, and how cool am I.\" ~Joe Dirt\n\n"
        elif dirtquote == 3:
            quote = "\"Luckily, my neck broke my fall.\" ~Joe Dirt\n\n"
        else:
            quote = "\n"





        if text == "DEPLOY -E PROD":
            deploy = sublime.ok_cancel_dialog(quote + "You are about to Deploy to PRODUCTION!","Continue")
            print(dirtquote)
        else:
            deploy = True

        if deploy == False:
            return
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
class SublTestCommand(sublime_plugin.TextCommand):

    def run(self, edit):

        # Get Path and User variables
        global_settings = sublime.load_settings('BIS.sublime-settings')
        appdata = os.environ['USERPROFILE']
        app = 'sublwatcher'
        print("1==============================================================")
        print(self.view.text_point(1,1))
        print("2==============================================================")
        print(self.view.line(self.view.text_point(1,1)))
        print("3==============================================================")
        print(self.view.substr(self.view.line(self.view.text_point(1,1))))
        print("4==============================================================")

