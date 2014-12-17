import sublime
import sublime_plugin
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
                self.view.sel().add(sublime.Region(fend, end))
                for region in self.view.sel():
                    h1text = self.view.substr(region)
                    sublime.status_message(h1text)
                    print(h1text)
                    if len(h1text) > 0:
                        if h1text[0] == ' ' or h1text[0] == '@' or h1text[0] == '\t' or h1text[0] == '[' or h1text[0] == ']' or h1text[0] == '<' or h1text[0] == '>' or h1text.endswith('_'):
                            flag = 'false'
                            if h1text[0] == '[' or h1text[0] == ']' or h1text[0] == '<' or h1text[0] == '>' or h1text.endswith('_'):
                                pass
                            else:
                                self.view.sel().clear()
                                fend = fend + 1
                                self.view.sel().add(sublime.Region(fend, end))
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
            newStr = h1text.replace("[", "")
            newStr = newStr.replace("<", "")
            newStr = newStr.replace(">", "")
            newStr = newStr.replace("]", "")
            webbrowser.open_new("https://developer.mozilla.org/en-US/docs/HTML/Element/" + newStr)
            return
        elif len(h1text) > 0 and (h1text.endswith('_')):
            # print(h1text)
            selection = h1text.lower()
            if selection == 'nsfileupld_':
                webpath = "http://gitlab.galaxy.local/docs/ice_modules/webhelpers/#nsfileupld_"
            elif selection == 'addupldfile_':
                webpath = "http://gitlab.galaxy.local/docs/ice_modules/webhelpers/#addupldfile_"
            elif selection == 'delupldfile_':
                webpath = "http://gitlab.galaxy.local/docs/ice_modules/webhelpers/#delupldfile_"
            elif selection == 'reorderupldfiles_':
                webpath = "http://gitlab.galaxy.local/docs/ice_modules/webhelpers/#reorderupldfiles_"
            elif selection == 'globaluplddata_':
                webpath = "http://gitlab.galaxy.local/docs/ice_modules/webhelpers/#globaluplddata_"
            elif selection == 'getupldfiles_':
                webpath = "http://gitlab.galaxy.local/docs/ice_modules/webhelpers/#getupldfiles_"
            elif selection == 'htmltags_' or selection == 'icehtmltags_':
                webpath = "http://gitlab.galaxy.local/docs/ice_modules/webhelpers/#htmltags_"
            elif selection == 'webbrk_':
                webpath = "http://gitlab.galaxy.local/docs/ice_modules/webhelpers/#webbrk_"
            elif selection == 'checkboxtag_':
                webpath = "http://gitlab.galaxy.local/docs/ice_modules/webhelpers/#checkboxtag_"
            elif selection == 'radiobtntag_':
                webpath = "http://gitlab.galaxy.local/docs/ice_modules/webhelpers/#radiobtntag_"
            elif selection == 'textfieldtag_':
                webpath = "http://gitlab.galaxy.local/docs/ice_modules/webhelpers/#textfieldtag_"
            elif selection == 'selecttag_':
                webpath = "http://gitlab.galaxy.local/docs/ice_modules/webhelpers/#selecttag_"
            elif selection == 'labletag_':
                webpath = "http://gitlab.galaxy.local/docs/ice_modules/webhelpers/#labeltag_"
            elif selection == 'textareatag_':
                webpath = "http://gitlab.galaxy.local/docs/ice_modules/webhelpers/#textareatag_"
            elif selection == 'nstextcleanup_':
                webpath = "http://gitlab.galaxy.local/docs/ice_modules/webhelpers/#nstextcleanup_"
            elif selection == 'redirect_' or selection == 'iceredirect_':
                webpath = "http://gitlab.galaxy.local/docs/ice_modules/webhelpers/#redirect_"
            elif selection == 'nstoolbelt_':
                webpath = "http://gitlab.galaxy.local/docs/ice_modules/utilities/#nstoolbelt_"
            elif selection == 'getlocfromdef_':
                webpath = "http://gitlab.galaxy.local/docs/ice_modules/utilities/#getlocfromdef_"
            elif selection == 'formparams_':
                webpath = "http://gitlab.galaxy.local/docs/ice_modules/utilities/#formparams_"
            elif selection == 'getfileext_':
                webpath = "http://gitlab.galaxy.local/docs/ice_modules/utilities/#getfileext_"
            elif selection == 'getqterechdgs_':
                webpath = "http://gitlab.galaxy.local/docs/ice_modules/utilities/#getqterechgds_"
            elif selection == 'gethdgs_':
                webpath = "http://gitlab.galaxy.local/docs/ice_modules/utilities/#gethdgs_"
            elif selection == 'nsparsepol_':
                webpath = "http://gitlab.galaxy.local/docs/ice_modules/utilities/#nsparsepol_"
            elif selection == 'nsdownpayment_':
                webpath = "http://gitlab.galaxy.local/docs/ice_modules/utilities/#nsdownpayment_"
            elif selection == 'dtpaging_':
                webpath = "http://gitlab.galaxy.local/docs/ice_modules/utilities/#dtpaging_"
            elif selection == 'nsstmgmtapi_':
                webpath = "http://gitlab.galaxy.local/docs/ice_modules/statemgmt/#nsstmgmtapi_"
            elif selection == 'smglobal_':
                webpath = "http://gitlab.galaxy.local/docs/ice_modules/statemgmt/#nsstmgmtapi_"
            elif selection == 'setss_':
                webpath = "http://gitlab.galaxy.local/docs/ice_modules/statemgmt/#creating-a-new-server-side-variable"
            elif selection == 'getss_':
                webpath = "http://gitlab.galaxy.local/docs/ice_modules/statemgmt/#getting-an-existing-server-side-variable"
            elif selection == 'delss_':
                webpath = "http://gitlab.galaxy.local/docs/ice_modules/statemgmt/#removing-an-existing-server-side-variable"
            elif selection == 'smresult_':
                webpath = "http://gitlab.galaxy.local/docs/ice_modules/statemgmt/#smresult_"
            elif selection == 'nsconfig_':
                webpath = "http://gitlab.galaxy.local/docs/ice_modules/config/#nsconfig_"
            elif selection == 'nsconfig_':
                webpath = "http://gitlab.galaxy.local/docs/ice_modules/config/#nsconfig_"
            elif selection == 'nsassets_':
                webpath = "http://gitlab.galaxy.local/docs/ice_modules/assets/#nsassets_"
            elif selection == 'nsextassets_':
                webpath = "http://gitlab.galaxy.local/docs/ice_modules/assets/#nsextassets_"
            elif selection == 'errors_' or selection == 'icerrors_' or selection == 'nserrors_':
                webpath = "http://gitlab.galaxy.local/docs/ice_modules/formvalidation/#errors_"
            elif selection == 'formval_' or selection == 'iceformval_':
                webpath = "http://gitlab.galaxy.local/docs/ice_modules/formvalidation/#formval_"
            elif selection == 'htmlhead_' or selection == 'icehtmlhead_':
                webpath = "http://gitlab.galaxy.local/docs/ice_modules/webtemplates/#htmlhead_"
            elif selection == 'header_' or selection == 'iceheader_':
                webpath = "http://gitlab.galaxy.local/docs/ice_modules/webtemplates/#header_"
            elif selection == 'nav_' or selection == 'icenav_':
                webpath = "http://gitlab.galaxy.local/docs/ice_modules/webtemplates/#nav_"
            elif selection == 'container_' or selection == 'icecontainer_':
                webpath = "http://gitlab.galaxy.local/docs/ice_modules/webtemplates/#container_"
            elif selection == 'alerts_' or selection == 'icealerts_':
                webpath = "http://gitlab.galaxy.local/docs/ice_modules/webtemplates/#alerts_"
            elif selection == 'errordsp_' or selection == 'icerrordsp_':
                webpath = "http://gitlab.galaxy.local/docs/ice_modules/webtemplates/#errordsp_"
            elif selection == 'errorscn_' or selection == 'icerrorscn_':
                webpath = "http://gitlab.galaxy.local/docs/ice_modules/webtemplates/#errorscn_"
            elif selection == 'footer_' or selection == 'icefooter_':
                webpath = "http://gitlab.galaxy.local/docs/ice_modules/webtemplates/#footer_"
            elif selection == 'icesendrecv_':
                webpath = "http://gitlab.galaxy.local/docs/ice_modules/wflstart/#icesendrecv_"
            elif selection == 'nsircoldimport_':
                webpath = "http://gitlab.galaxy.local/docs/ice_modules/imagerightmodules/#nsircoldimport_"
            elif selection == 'nsirfup_':
                webpath = "http://gitlab.galaxy.local/docs/ice_modules/imagerightmodules/#nsirfup_"
            elif selection == 'nsirnup_':
                webpath = "http://gitlab.galaxy.local/docs/ice_modules/imagerightmodules/#nsirnup_"
            elif selection == 'nsirafup_':
                webpath = "http://gitlab.galaxy.local/docs/ice_modules/imagerightmodules/#nsirafup_"
            elif selection == 'nsirimport_':
                webpath = "http://gitlab.galaxy.local/docs/ice_modules/imagerightmodules/#nsirimport_"
            elif selection == 'nsirimport_':
                webpath = "http://gitlab.galaxy.local/docs/ice_modules/imagerightmodules/#nsirimport_"
            else:
                webpath = "http://gitlab.galaxy.local/docs/?q=" + selection
            webbrowser.open_new(webpath)
            return
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
        elif h1text.lower() == 'dsp':
            path = "hh.exe C:\\Unisys\\Clients\\Help\\comref.chm::/40_S02D/D_and_DSP_Display_Report_.htm"
        elif h1text.lower() == 'fdr':
            path = "hh.exe C:\\Unisys\\Clients\\Help\\comref.chm::/40_S02F/_fdr_find_and_read_line_.htm"
        elif h1text.lower() == 'inc':
            path = "hh.exe C:\\Unisys\\Clients\\Help\\comref.chm::/40_S02I/_INC_Increment_Variable_.htm"
        elif h1text.lower() == 'juv':
            path = "hh.exe C:\\Unisys\\Clients\\Help\\comref.chm::/40_S02J/_juv_justify_variable_.htm"
        elif h1text.lower() == 'lch':
            path = "hh.exe C:\\Unisys\\Clients\\Help\\comref.chm::/40_S02C/chg_and_lch_locate_and_change_.htm"
        elif h1text.lower() == 'lcv':
            path = "hh.exe C:\\Unisys\\Clients\\Help\\comref.chm::/40_S02L/_lcv_locate_and_change_variable_.htm"
        elif h1text.lower() == 'ldv':
            path = "hh.exe C:\\Unisys\\Clients\\Help\\comref.chm::/40_S02L/_LDV_Load_Variable_.htm"
        elif h1text.lower() == 'lln':
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
        elif h1text.lower() == 'os':
            path = "hh.exe C:\\Unisys\\Clients\\Help\\comref.chm::/40_S02O/os_and_os_operating_system_interface_.htm"
        elif h1text.lower() == 'rdb':
            path = "hh.exe C:\\Unisys\\Clients\\Help\\comref.chm::/40_S02R/RDB_and_RDB_Run_Debug_.htm"
        elif h1text.lower() == 'rel':
            path = "hh.exe C:\\Unisys\\Clients\\Help\\comref.chm::/40_S02R/Release_Display_and_REL.htm"
        elif h1text.lower() == 'rep':
            path = "hh.exe C:\\Unisys\\Clients\\Help\\comref.chm::/40_S02R/REP_and_REP_Replace_Report_.htm"
        elif h1text.lower() == 'ret':
            path = "hh.exe C:\\Unisys\\Clients\\Help\\comref.chm::/40_S02R/RETR_and_REH_Retrieve_Report_from_History_.htm"
        elif h1text.lower() == 'rfm':
            path = "hh.exe C:\\Unisys\\Clients\\Help\\comref.chm::/40_S02R/rf_and_rfm_reformat_report_.htm"
        elif h1text.lower() == 'rsl':
            path = "hh.exe C:\\Unisys\\Clients\\Help\\comref.chm::/40_S02R/rslt_and_rsl_create_result_copy_.htm"
        elif h1text.lower() == 'run':
            path = "hh.exe C:\\Unisys\\Clients\\Help\\comref.chm::/40_S02R/run.htm"
        elif h1text.lower() == 'return':
            path = "hh.exe C:\\Unisys\\Clients\\Help\\comref.chm::/40_S02R/_RETURN_Return_Call_Routine_.htm"
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
        elif h1text.lower() == 'srr':
            path = "hh.exe C:\\Unisys\\Clients\\Help\\comref.chm::/40_S02S/_srr_sort_and_replace_.htm"
        elif h1text.lower() == 'tot':
            path = "hh.exe C:\\Unisys\\Clients\\Help\\comref.chm::/40_S02T/TOT_and_TOT_Totalize_.htm"
        elif h1text.lower() == 'tip':
            path = "hh.exe C:\\Unisys\\Clients\\Help\\comref.chm::/40_S02T/_TIP_Tool_Tip_.htm"
        elif h1text.lower() == 'rnm':
            path = "hh.exe C:\\Unisys\\Clients\\Help\\comref.chm::/40_S02R/_RNM_Rename_.htm"
        elif h1text.lower() == 'srh':
            path = "hh.exe C:\\Unisys\\Clients\\Help\\comref.chm::/40_S02S/_srh_search_.htm"
        elif h1text.lower() == 'sru':
            path = "hh.exe C:\\Unisys\\Clients\\Help\\comref.chm::/40_S02S/_sru_search_update_.htm"
        elif h1text.lower() == 'snu':
            path = "hh.exe C:\\Unisys\\Clients\\Help\\comref.chm::/40_S02S/SNU_and_SNU_Send_Report_to_User_.htm"
        elif h1text.lower() == 'sys':
            path = "hh.exe C:\\Unisys\\Clients\\Help\\comref.chm::/40_S02S/SYSTEM_and_SYS_System_.htm"
        elif h1text.lower() == 'upd':
            path = "hh.exe C:\\Unisys\\Clients\\Help\\comref.chm::/_ULK_Unlock_.htm"
        elif h1text.lower() == 'ulk':
            path = "hh.exe C:\\Unisys\\Clients\\Help\\comref.chm::/40_S02U/UPD_and_UPD_Update_.htm"
        elif h1text.lower() == 'wat':
            path = "hh.exe C:\\Unisys\\Clients\\Help\\comref.chm::/40_S02W/_WAT_Wait_.htm"
        elif h1text.lower() == 'wrl':
            path = "hh.exe C:\\Unisys\\Clients\\Help\\comref.chm::/40_S02W/_wrl_write_line_.htm"
        elif h1text.lower() == 'xun':
            path = "hh.exe C:\\Unisys\\Clients\\Help\\comref.chm::/40_S02X/_xun_exit_mapper_.htm"
        elif h1text.lower() == 'xr':
            path = "hh.exe C:\\Unisys\\Clients\\Help\\comref.chm::/40_S02X/XR_and_DUP_Duplicate_Report_.htm"
        elif h1text.lower() == 'xqt':
            path = "hh.exe C:\\Unisys\\Clients\\Help\\comref.chm::/40_S02X/_XQT_Execute_.htm"
        elif h1text.lower() == 'ynk':
            path = "hh.exe C:\\Unisys\\Clients\\Help\\comref.chm::/40_S02Y/Yank_Line_and_LNY.htm"
        else:
            path = "hh.exe C:\\Unisys\\Clients\\Help\\BIS.chm"

        subprocess.Popen(path)
