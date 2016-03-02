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
        if dirtquote == 1:
            quote = "\"My name is Joe Dirte(deer-tay), I added an e to the end, cause it sounds cool.\"\n ~Joe Dirt, Joe Dirt\n\n\n"
        elif dirtquote == 2:
            quote = "\"Life's a garden, dig it.\"\n ~Joe Dirt, Joe Dirt\n\n\n"
        elif dirtquote == 3:
            quote = "\"People say Joe Dirt's a weird name, and how cool am I., Joe Dirt\"\n ~Joe Dirt\n\n\n"
        elif dirtquote == 3:
            quote = "\"Luckily, my neck broke my fall.\"\n ~Joe Dirt, Joe Dirt\n\n\n"
        elif dirtquote == 4:
            quote = "\"I got the poo on me!\"\n ~Joe Dirt, Joe Dirt\n\n\n"
        elif dirtquote == 5:
            quote = "\"The pen is blue, the pen is blue, the g**d*** pen is blue!\"\n ~Fletcher, Liar Liar\n\n\n"
        elif dirtquote == 6:
            quote = "\"Uh-oh. You've found the claw's only weakness... Sub-zero temperatures![Splatting sound]\"\n ~Fletcher, Liar Liar\n\n\n"
        elif dirtquote == 7:
            quote = "\"There's so much more room for activities!\"\n ~Brennan & Dale, Step Brothers\n\n\n"
        else:
            quote = "\n"





        if text == "DEPLOY -E PROD":
            deploy = sublime.ok_cancel_dialog(quote + "You are about to Deploy to PRODUCTION!","Continue")
        else:
            deploy = True

        if deploy == False:
            return

#       Capture line2 of the page to determine if Status Page and get site/appname if so
        line2 = self.view.substr(self.view.line(self.view.text_point(1,1)))
        # Check if GIT STATUS page or not
        if line2[:6] == "Local:":
            statpage = True
        else:
            statpage = False

        # Get Path and User variables
        global_settings = sublime.load_settings('BIS.sublime-settings')
        appdata = os.environ['USERPROFILE']
        app = 'sublwatcher'
        sublime.status_message("Writing BisCmd file")
        file_name = self.view.file_name()
        filename_filter = global_settings.get('filename_filter', '.*')
        #   Status page has no filename, so skip regex
        if statpage == False:
            if not re.search(filename_filter, file_name):
                file_name = appdata + '\\' + app + '\\'

        if statpage == True:
            pos = line2.find('site-')
            pos = pos + 5
            site = line2[pos]
            pos = pos + 2
            appname = line2[pos:]
            file_name = appdata + '\\' + app + '\\site-' + site + '\\' + appname + '\\'
        else:
            pos = file_name.find('site-')
            pos = pos + 5
            site = file_name[pos]
        bis_cmd_file = 'site-' + site + '\\changes.txt'
        file_path = appdata + '\\' + app + '\\' + bis_cmd_file

        # Write file to path
        if statpage == True:
            with open(file_path, "w") as textfile:
                textfile.write("BisCmd" + "," + file_name + "," + "input" + "," + text + ",STATUS," + appname)
        else:
            with open(file_path, "w") as textfile:
                textfile.write("BisCmd" + "," + file_name + "," + "input" + "," + text)
#===============================================================================
#
#
#
#===============================================================================
#class SublTestCommand(sublime_plugin.TextCommand):
#
#    def run(self, edit):
#
#        # Get Path and User variables
#        global_settings = sublime.load_settings('BIS.sublime-settings')
#        appdata = os.environ['USERPROFILE']
#        app = 'sublwatcher'
#        line2 = self.view.substr(self.view.line(self.view.text_point(1,1)))
#        # Check if GIT STATUS page or not
#        if line2[:6] == "Local:":
#            statpage = True
#        else:
#            statpage = False
#
#        if statpage == True:
#            pos = line2.find('site-')
#            pos = pos + 5
#            site = line2[pos]
#            pos = pos + 2
#            appname = line2[pos:]
#
#
#        print("1==============================================================")
#        print(self.view.text_point(1,1))
#        print("2==============================================================")
#        print(self.view.line(self.view.text_point(1,1)))
#        print("3==============================================================")
#        print(self.view.substr(self.view.line(self.view.text_point(1,1))))
#        print("4==============================================================")
#        print(line2[:6])
#        print("5==============================================================")
#        print("[" + str(statpage) + "}   S[" + site + "]   A[" + appname + "]")
#