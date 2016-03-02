# import sublime
# import sublime_plugin
# import os

# class BisBugCommand(sublime_plugin.TextCommand):
#     def run(self, edit):

#         path      = self.view.file_name()
#         directory = os.path.dirname(path)
#         file_name = os.path.basename(path)
#         directory = directory + "\BisBug.bis"

# print path
#         current_user = os.environ.get("USERNAME")
# print current_user

# Check if BisBug script is registered
#         if os.path.exists("C:\Unisys\Clients\MPC\Scripts\BisBug.ATR"):

# print "Writing BisBug command file"
#             with open(directory, "w") as textfile:
#                 textfile.write(file_name)

#             self.view.window().run_command("exec", {
#               "cmd": ['C:\Unisys\Clients\MPC\mpcapi32.exe -cBisBug -dMAPPER.MSF'],
#               "shell": True
#             })

#         if os.path.exists("C:\Unisys\Clients\MPC$1\Scripts\BisBug.ATR"):
# print "Writing BisBug command file"
#             with open(directory, "w") as textfile:
#                 textfile.write(file_name)

#             self.view.window().run_command("exec", {
#               "cmd": ['C:\Unisys\Clients\MPC$1\mpcapi32.exe -cBisBug -dMAPPER.MSF'],
#               "shell": True
#             })

# else:
# print "Could not find BisBug script in current directory"
