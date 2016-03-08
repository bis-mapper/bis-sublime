#===============================================================================
#
#  ####   #####  #####         #####  #   #  ####   #      #####  #   #  #####
#  #   #    #    #             #      #   #  #   #  #        #    ## ##  #
#  ####     #    #####  #####  #####  #   #  ####   #        #    # # #  ####
#  #   #    #        #             #  #   #  #   #  #        #    #   #  #
#  ####   #####  #####         #####   ###   ####   #####  #####  #   #  #####
#
#===============================================================================
#   IMPORTS!
import sublime
import sublime_plugin
import re
import os
import datetime
import subprocess
import threading
from getpass import getuser
from shutil import copyfile
from random import randint
#===============================================================================
#
#===============================================================================
#
#  #####   ###   #   #  #####         ####   #   #  #####  #      ####
#  #      #   #  #   #  #             #   #  #   #    #    #      #   #
#  #####  #####  #   #  ####   #####  ####   #   #    #    #      #   #
#      #  #   #   # #   #             #   #  #   #    #    #      #   #
#  #####  #   #    #    #####         ####    ###   #####  #####  ####
#
#===============================================================================
#   SAVE FILE! - BisSaveBuild.py
class BisSaveBuild(sublime_plugin.EventListener):

    def on_pre_save(self, view):
        t = os.path.getmtime(view.file_name())
        self.dt = datetime.datetime.fromtimestamp(t).strftime("%Y%m%d %H%M%S")

    def on_post_save(self, view):
        global_settings = sublime.load_settings('BIS.sublime-settings')

        # See if we should build. A project level build_on_save setting
        # takes precedence. To be backward compatible, we assume the global
        # build_on_save to be true if not defined.
        should_build = view.settings().get(
            'build_on_save', global_settings.get('build_on_save', True))
        if not should_build:
            return

        # Capture line2 of the page to determine if Status Page
        statline, statpage = get_statpage(view)

        # Get User variables
        appdata, app, appname, file_name, site = get_user_vars(statline,statpage,global_settings,view)

        # Get Path
        file_path = get_file_path(site,appdata,app)

        # Write file save to site
        chg_text = "modified" + "," + file_name + ", file, BisSaveBuild," + self.dt[:8] + "," + self.dt[9:]
        write_file(file_path,chg_text)
#===============================================================================
#
#===============================================================================
#
#   ####  #####  ####   #             #      #####  #   #  #####
#  #        #    #   #  #             #        #    ##  #  #
#  #        #    ####   #             #        #    # # #  ####
#  #        #    #  #   #             #        #    #  ##  #
#   ####    #    #   #  #####         #####  #####  #   #  #####
#
#===============================================================================
#   OPEN BIS CONTROL LINE! - BisCmd.py
class BisCtrlCommand(sublime_plugin.WindowCommand):

    def run(self):
        self.window.show_input_panel("BIS Control Line:", "", self.on_done, None, None)
        pass

    def on_done(self, text):
        if self.window.active_view():
            self.window.active_view().run_command("app_current", {"text": text})
#===============================================================================
#
#===============================================================================
#
#  #####  #   #  ####   #      #   #   ###   #####   ####  #   #  #####  ####
#  #      #   #  #   #  #      #   #  #   #    #    #      #   #  #      #   #
#  #####  #   #  ####   #      # # #  #####    #    #      #####  ####   ####
#      #  #   #  #   #  #      ## ##  #   #    #    #      #   #  #      #  #
#  #####   ###   ####   #####  #   #  #   #    #     ####  #   #  #####  #   #
#
#===============================================================================
#   OPEN SUBLWATCHER!
class OpenSublwatcherCommand(sublime_plugin.TextCommand):
    def run(self, edit, site):
        appdata = os.environ['appdata']
        dst1 = appdata+'\\Unisys\\Clients\\MPC5.4\\Scripts\\SITE-'+site+'-SUBLWATCHER.ATR'
        if not os.path.exists(dst1):
            src1 = 'S:\\SUBLWATCHER_SCRIPTS\\SITE-'+site+'-SUBLWATCHER.ATR'
            src2 = 'S:\\SUBLWATCHER_SCRIPTS\\SITE-'+site+'-SUBLWATCHER.SCR'
            dst2 = appdata+'\\Unisys\\Clients\\MPC5.4\\Scripts\\SITE-'+site+'-SUBLWATCHER.SCR'
            copyfile(src1,dst1)
            copyfile(src2,dst2)
        th = SublwatcherThread(site)
        th.start()

class SublwatcherThread(threading.Thread):
    def __init__(self, site):
        self.site = site.upper()
        threading.Thread.__init__(self)

    def run(self):
        subprocess.call('C:\\Unisys\\Clients\\MPC\\mpcapi32.exe -cSITE-'+self.site+'-SUBLWATCHER -dD:\\Unisys\\Mapper\\MAPPER.MSF')
#===============================================================================
#
#===============================================================================
#   RUN MAJORITY OF TASKS! - Sublwatcher.py
class AppCurrentCommand(sublime_plugin.TextCommand):

    def run(self, edit, text):
        global_settings = sublime.load_settings('BIS.sublime-settings')

        # Check if PROD deploy: yes? confirm, no? continue
        deploy = deploy_conf(text)
        if deploy == False:
            return

        # Capture line2 of the page to determine if Status Page
        statline, statpage = get_statpage(self.view)

        # Get User variables
        appdata, app, appname, file_name, site = get_user_vars(statline,statpage,global_settings,self.view)

        # Get Path
        file_path = get_file_path(site,appdata,app)

        # Create File TEXT
        chg_text = "BisCmd" + "," + file_name + "," + "input" + "," + text      #DEFAULT!
        if statpage == True:
            if text[:6].upper() == "DEPLOY" or text[:6].upper() == "EXPORT":
                chg_text = "BisCmd" + "," + file_name + "," + "input" + "," + text + ",STATUS," + appname
            else:
                sublime.error_message(text + "\ncannot be used on the status screen! [ yet? ;) ]")
                return

        # Write file to path
        write_file(file_path,chg_text)
#===============================================================================
#
#===============================================================================
#
#  ####   #####  #####  #####
#  #   #    #    #      #
#  #   #    #    ####   ####
#  #   #    #    #      #
#  ####   #####  #      #
#
#===============================================================================
#   GET PARAMS FOR IBLD RESOURCE MANIPULATION
class DiffOtherCommand(sublime_plugin.WindowCommand):
    def run(self, site):
        self.text = 'DIFF'
        self.counter = 0
        if site == 'CURRENT':
            self.prompts = ["DIFF w/ report(ex. 1B200):"]
        else:
            self.prompts = ["DIFF w/ report(ex. 1B200):","DIFF w/ Site Letter(ex. X):"]
        self.show_prompt()

    def on_done(self, text):
        if self.counter == 1:
            self.text += " -S " + text
        else:
            self.text += " " + text
        self.counter += 1
        if self.counter < len(self.prompts):
            self.show_prompt()
        else:
            self.input_done()

    def input_done(self):
        if self.window.active_view():
            self.window.active_view().run_command("app_current", {"text": self.text})

    def show_prompt(self):
        self.window.show_input_panel(self.prompts[self.counter], "", self.on_done, None, None)
#===============================================================================
#
#===============================================================================
#
#  #####  ####   #      ####
#    #    #   #  #      #   #
#    #    ####   #      #   #
#    #    #   #  #      #   #
#  #####  ####   #####  ####
#
#===============================================================================
#   GET PARAMS FOR IBLD RESOURCE MANIPULATION
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
            self.window.active_view().run_command("app_current", {"text": self.text + self.webscript})

    def show_prompt(self):
        self.window.show_input_panel(self.prompts[self.counter], "", self.on_done, None, None)
#===============================================================================
#
#===============================================================================
#
#  #####  #   #  #   #   ####  #####  #####  #####  #   #  #####
#  #      #   #  ##  #  #        #      #    #   #  ##  #  #
#  ####   #   #  # # #  #        #      #    #   #  # # #  #####
#  #      #   #  #  ##  #        #      #    #   #  #  ##      #
#  #       ###   #   #   ####    #    #####  #####  #   #  #####
#
#===============================================================================
#   DEPLOY_CONF - display confirmation dialog for PROD deploy
def deploy_conf(text):
    if text.upper() == "DEPLOY -E PROD":
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

        deploy = sublime.ok_cancel_dialog(quote + "You are about to Deploy to PRODUCTION!","Continue")
    else:
        deploy = True
    return deploy
#===============================================================================
#
#===============================================================================
#   GET_STATPAGE - returns statline and statpage
def get_statpage(cur_view):
    statline = cur_view.substr(cur_view.line(cur_view.text_point(1,1)))
    # Check if GIT STATUS page or not
    if statline[:6] == "Local:":
        statpage = True
    else:
        statpage = False
    return statline, statpage
#===============================================================================
#
#===============================================================================
#   GET_FILE_PATH - returns file_path based on site passed in
def get_file_path(site,appdata,app):
    if site == 'NONE':
        bis_save_file = '\\changes.txt'
    else:
        bis_save_file = 'site-' + site + '\\changes.txt'
    file_path = appdata + '\\' + app + '\\' + bis_save_file
    return file_path
#===============================================================================
#
#===============================================================================
#   GET_USER_VARS - returns path and user variables
def get_user_vars(statline,statpage,global_settings,cur_view):
    appdata = os.environ['USERPROFILE']
    app = 'sublwatcher'
    appname = 'NA'                                                     #DEFAULT!
    if statpage == True:
        pos = statline.find('site-')
        pos = pos + 5
        site = statline[pos]
        pos = pos + 2
        appname = statline[pos:]
        file_name = appdata + '\\' + app + '\\site-' + site + '\\' + appname + '\\'
    else:
        filename_filter = global_settings.get('filename_filter', '.*')
        file_name = cur_view.file_name()
        if not re.search(filename_filter, file_name):
            file_name = appdata + '\\' + app + '\\'
            site = 'NONE'
            return appdata, app, appname, file_name, site
        pos = file_name.find('site-')
        pos = pos + 5
        site = file_name[pos]

    return appdata, app, appname, file_name, site
#===============================================================================
#
#===============================================================================
#   WRITE_FILE - writes the file out to the correct directory
def write_file(file_path,chg_text):
    with open(file_path, "w") as textfile:
        textfile.write(chg_text)
    return
#===============================================================================
#
#===============================================================================
#
#  #####  #####  #####  #####          ###   ####   #####   ###
#    #    #      #        #           #   #  #   #  #      #   #
#    #    ####   #####    #           #####  ####   ####   #####
#    #    #          #    #           #   #  #  #   #      #   #
#    #    #####  #####    #           #   #  #   #  #####  #   #
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
#===============================================================================
