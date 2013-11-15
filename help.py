import sublime, sublime_plugin
import os.path
import subprocess
import webbrowser

class helpCommand(sublime_plugin.TextCommand):
  def run(self, edit):
    for region in self.view.sel():
        flag = 'true'
        i = 2
        end = region.end()
        while (flag == 'true'):
          fend = end - i
          self.view.sel().add(sublime.Region(fend,end))
          for region in self.view.sel():
            h1text = self.view.substr(region)
            sublime.status_message(h1text)
            print(h1text)
            if len(h1text) > 0:
             if h1text[0] == ' ' or h1text[0] == '@' or h1text[0] == '\t' or h1text[0] == '[' or h1text[0] == ']' or h1text[0] == '<' or h1text[0] == '>':
               flag = 'false'
               if h1text[0] == '[' or h1text[0] == ']' or h1text[0] == '<' or h1text[0] == '>':
                pass
               else:
                self.view.sel().clear()
                fend = fend + 1
                self.view.sel().add(sublime.Region(fend,end))
                for region in self.view.sel():
                 h1text = self.view.substr(region)
             else:
              if fend == 0:
                flag = 'false'
              i = i + 1
            else:
              flag = 'false'

    self.view.sel().clear()

    if len(h1text) > 0 and (h1text[0] == '[' or h1text[0] == '<'):
      newStr = h1text.replace("[","")
      newStr = newStr.replace("<","")
      newStr = newStr.replace(">","")
      newStr = newStr.replace("]","")
      webbrowser.open_new("https://developer.mozilla.org/en-US/docs/HTML/Element/"+newStr)
      return

    elif h1text.lower() == 'dsp':
      path = "hh.exe C:\\Unisys\\Clients\\Help\\comref.chm::/40_S02D/D_and_DSP_Display_Report_.htm"
    elif h1text.lower() == 'add':
      path = "hh.exe C:\\Unisys\\Clients\\Help\\comref.chm::/40_S02a/adon_adto_and_add_append_report_.htm"
    elif h1text.lower() == 'adr':
      path = "hh.exe C:\\Unisys\\Clients\\Help\\comref.chm::/40_S02a/AR_and_ADR_Add_Report_.htm"
    elif h1text.lower() == 'bfn':
      path = "hh.exe C:\\Unisys\\Clients\\Help\\comref.chm::/40_S02B/bf_and_bfn_binary_find_.htm"
    elif h1text.lower() == 'cal':
      path = "hh.exe C:\\Unisys\\Clients\\Help\\comref.chm::/40_S02C/CAL_CAL_Calculate_CALU_CAU_Calculate_Update_.htm"
    elif h1text.lower() == 'call':
      path = "hh.exe C:\\Unisys\\Clients\\Help\\comref.chm::/40_S02C/_call_call_subroutine_.htm"
    elif h1text.lower() == 'cau':
      path = "hh.exe C:\\Unisys\\Clients\\Help\\comref.chm::/40_S02C/CAL_CAL_Calculate_CALU_CAU_Calculate_Update_.htm"
    elif h1text.lower() == 'cnt':
      path = "hh.exe C:\\Unisys\\Clients\\Help\\comref.chm::/40_S02C/cnt_and_cnt_count_.htm"
    elif h1text.lower() == 'dat':
      path = "hh.exe C:\\Unisys\\Clients\\Help\\comref.chm::/40_S02D/DATE_and_DAT_Date_.htm"
    elif h1text.lower() == 'dc':
      path = "hh.exe C:\\Unisys\\Clients\\Help\\comref.chm::/40_S02D/_dc_date_calculator_.htm"
    elif h1text.lower() == 'dec':
      path = "hh.exe C:\\Unisys\\Clients\\Help\\comref.chm::/40_S02D/_DEC_Decrement_Variable_.htm"
    elif h1text.lower() == 'def':
      path = "hh.exe C:\\Unisys\\Clients\\Help\\comref.chm::/40_S02D/_def_define_.htm"
    elif h1text.lower() == 'fdr':
      path = "hh.exe C:\\Unisys\\Clients\\Help\\comref.chm::/40_S02F/_fdr_find_and_read_line_.htm"
    elif h1text.lower() == 'inc':
      path = "hh.exe C:\\Unisys\\Clients\\Help\\comref.chm::/40_S02I/_INC_Increment_Variable_.htm"
    elif h1text.lower() == 'juv':
      path = "hh.exe C:\\Unisys\\Clients\\Help\\comref.chm::/40_S02J/_juv_justify_variable_.htm"
    elif h1text.lower() == 'LCH':
      path = "hh.exe C:\\Unisys\\Clients\\Help\\comref.chm::/40_S02C/chg_and_lch_locate_and_change_.htm"
    elif h1text.lower() == 'LCV':
      path = "hh.exe C:\\Unisys\\Clients\\Help\\comref.chm::/40_S02L/_lcv_locate_and_change_variable_.htm"
    elif h1text.lower() == 'LLN':
      path = "hh.exe C:\\Unisys\\Clients\\Help\\comref.chm::/40_S02L/_lln_last_line_number_.htm"
    elif h1text.lower() == 'lzr':
      path = "hh.exe C:\\Unisys\\Clients\\Help\\comref.chm::/40_S02L/LZ_and_LZR_Line_Zero_.htm"
    elif h1text.lower() == 'mau':
      path = "hh.exe C:\\Unisys\\Clients\\Help\\comref.chm::/40_S02M/MA_and_MCH_Match_MAU_and_MAU_Match_Update_.htm"
    elif h1text.lower() == 'mch':
      path = "hh.exe C:\\Unisys\\Clients\\Help\\comref.chm::/40_S02M/MA_and_MCH_Match_MAU_and_MAU_Match_Update_.htm"
    elif h1text.lower() == 'net':
      path = "hh.exe C:\\Unisys\\Clients\\Help\\comref.chm::/40_S02N/_NET_Network_Sign_On_.htm"
    elif h1text.lower() == 'nrd':
      path = "hh.exe C:\\Unisys\\Clients\\Help\\comref.chm::/40_S02N/_NRD_Network_Read_.htm"
    elif h1text.lower() == 'nrn':
      path = "hh.exe C:\\Unisys\\Clients\\Help\\comref.chm::/40_S02N/_NRN_Network_Run_.htm"
    elif h1text.lower() == 'OS':
      path = "hh.exe C:\\Unisys\\Clients\\Help\\comref.chm::/40_S02O/os_and_os_operating_system_interface_.htm"
    elif h1text.lower() == 'rdc':
      path = "hh.exe C:\\Unisys\\Clients\\Help\\comref.chm::/40_S02R/_RDC_Read_Continuous_.htm"
    elif h1text.lower() == 'rdl':
      path = "hh.exe C:\\Unisys\\Clients\\Help\\comref.chm::/40_S02R/_RDL_Read_Line_.htm"
    elif h1text.lower() == 'rln':
      path = "hh.exe C:\\Unisys\\Clients\\Help\\comref.chm::/40_S02R/_RLN_Read_Line_Next_.htm"
    elif h1text.lower() == 'rsr':
      path = "hh.exe C:\\Unisys\\Clients\\Help\\comref.chm::/40_S02R/_RSR_Run_Subroutine_.htm"
    elif h1text.lower() == 'srh':
      path = "hh.exe C:\\Unisys\\Clients\\Help\\comref.chm::/40_S02S/S_and_SRH_Search_SU_and_SRU_Search_Update_.htm"
    elif h1text.lower() == 'sor':
      path = "hh.exe C:\\Unisys\\Clients\\Help\\comref.chm::/40_S02S/SORT_SOR_Sort_SORTR_SRR_Sort_and_Replace_.htm"
    elif h1text.lower() == 'wrl':
      path = "hh.exe C:\\Unisys\\Clients\\Help\\comref.chm::/40_S02S/SOE_Updating_and_WRL_Write_Line_.htm"
    elif h1text.lower() == 'tot':
      path = "hh.exe C:\\Unisys\\Clients\\Help\\comref.chm::/40_S02T/TOT_and_TOT_Totalize_.htm"
    elif h1text.lower() == 'rnm':
      path = "hh.exe C:\\Unisys\\Clients\\Help\\comref.chm::/40_S02R/_RNM_Rename_.htm"
    elif h1text.lower() == 'ldv':
      path = "hh.exe C:\\Unisys\\Clients\\Help\\comref.chm::/40_S02L/_LDV_Load_Variable_.htm"
    else:
      path = "hh.exe C:\\Unisys\\Clients\\Help\\BIS.chm"

    subprocess.Popen(path)


