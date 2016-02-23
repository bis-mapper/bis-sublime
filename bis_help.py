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
        elif h1text.lower() == 'art':
            path = "hh.exe C:\\Unisys\\Clients\\Help\\comref.chm::/40_S02a/A_and_ART_Arithmetic_.htm"
        elif h1text.lower() == 'aux':
            path = "hh.exe C:\\Unisys\\Clients\\Help\\comref.chm::/40_S02a/aux_and_aux_auxiliary_.htm"
        elif h1text.lower() == 'bbo':
            path = "hh.exe C:\\Unisys\\Clients\\Help\\comref.chm::/40_S02B/_BBO_Block_Blank_Overlay_.htm"
        elif h1text.lower() == 'bco':
            path = "hh.exe C:\\Unisys\\Clients\\Help\\comref.chm::/40_S02B/_BCO_Block_Copy_Overlay_.htm"
        elif h1text.lower() == 'bpo':
            path = "hh.exe C:\\Unisys\\Clients\\Help\\comref.chm::/40_S02B/_BPO_Block_Put_Overlay_.htm"
        elif h1text.lower() == 'bfn':
            path = "hh.exe C:\\Unisys\\Clients\\Help\\comref.chm::/40_S02B/bf_and_bfn_binary_find_.htm"
        elif h1text.lower() == 'blt':
            path = "hh.exe C:\\Unisys\\Clients\\Help\\comref.chm::/40_S02B/blt_and_blt_build_label_table_.htm"
        elif h1text.lower() == 'br':
            path = "hh.exe C:\\Unisys\\Clients\\Help\\comref.chm::/40_S02B/br_and_br_background_run_.htm"
        elif h1text.lower() == 'brg':
            path = "hh.exe C:\\Unisys\\Clients\\Help\\comref.chm::/40_S02B/_brg_break_graphics_.htm"
        elif h1text.lower() == 'brk':
            path = "hh.exe C:\\Unisys\\Clients\\Help\\comref.chm::/40_S02B/_BRK_Break_.htm"
        elif h1text.lower() == 'btn':
            path = "hh.exe C:\\Unisys\\Clients\\Help\\comref.chm::/40_S02B/_btn_define_button_.htm"
        elif h1text.lower() == 'cab':
            path = "hh.exe C:\\Unisys\\Clients\\Help\\comref.chm::/40_S02C/c_cs_and_cab_cabinet_switch_.htm"
        elif h1text.lower() == 'cah':
            path = "hh.exe C:\\Unisys\\Clients\\Help\\comref.chm::/40_S02C/_cah_cache_report_.htm"
        elif h1text.lower() == 'cal':
            path = "hh.exe C:\\Unisys\\Clients\\Help\\comref.chm::/40_S02C/CAL_CAL_Calculate_CALU_CAU_Calculate_Update_.htm"
        elif h1text.lower() == 'call':
            path = "hh.exe C:\\Unisys\\Clients\\Help\\comref.chm::/40_S02C/_call_call_subroutine_.htm"
        elif h1text.lower() == 'cau':
            path = "hh.exe C:\\Unisys\\Clients\\Help\\comref.chm::/40_S02C/CAL_CAL_Calculate_CALU_CAU_Calculate_Update_.htm"
        elif h1text.lower() == 'cbx':
            path = "hh.exe C:\\Unisys\\Clients\\Help\\comref.chm::/40_S02C/_CBX_Define_Combo_Box_.htm"
        elif h1text.lower() == 'ccc':
            path = "hh.exe C:\\Unisys\\Clients\\Help\\comref.chm::/40_S02C/_ccc_com_client_create_instance_.htm"
        elif h1text.lower() == 'ccg':
            path = "hh.exe C:\\Unisys\\Clients\\Help\\comref.chm::/40_S02C/_CCG_COM_Client_Get_Property_Value_.htm"
        elif h1text.lower() == 'cci':
            path = "hh.exe C:\\Unisys\\Clients\\Help\\comref.chm::/40_S02C/_CCI_COM_Client_Invoke_Method_.htm"
        elif h1text.lower() == 'ccp':
            path = "hh.exe C:\\Unisys\\Clients\\Help\\comref.chm::/40_S02C/_CCP_COM_Client_Put_Property_Value_.htm"
        elif h1text.lower() == 'ccr':
            path = "hh.exe C:\\Unisys\\Clients\\Help\\comref.chm::/40_S02C/_CCR_COM_Client_Release_Instance_.htm"
        elif h1text.lower() == 'cer':
            path = "hh.exe C:\\Unisys\\Clients\\Help\\comref.chm::/40_S02C/_cer_clear_error_routine_.htm"
        elif h1text.lower() == 'chd':
            path = "hh.exe C:\\Unisys\\Clients\\Help\\comref.chm::/40_S02C/_CHD_Command_Handler_.htm"
        elif h1text.lower() == 'chg':
            path = "hh.exe C:\\Unisys\\Clients\\Help\\comref.chm::/40_S02C/_CHG_Change_Variable_.htm"
        elif h1text.lower() == 'clk':
            path = "hh.exe C:\\Unisys\\Clients\\Help\\comref.chm::/40_S02C/_clk_clear_link_.htm"
        elif h1text.lower() == 'cls':
            path = "hh.exe C:\\Unisys\\Clients\\Help\\comref.chm::/40_S02C/_CLS_Close_Control_.htm"
        elif h1text.lower() == 'clt':
            path = "hh.exe C:\\Unisys\\Clients\\Help\\comref.chm::/40_S02C/clt_and_clt_clear_label_table_.htm"
        elif h1text.lower() == 'clv':
            path = "hh.exe C:\\Unisys\\Clients\\Help\\comref.chm::/40_S02C/_CLV_Clear_Variables_.htm"
        elif h1text.lower() == 'cmp':
            path = "hh.exe C:\\Unisys\\Clients\\Help\\comref.chm::/40_S02C/cmp_and_cmp_compare_data_.htm"
        elif h1text.lower() == 'cmu':
            path = "hh.exe C:\\Unisys\\Clients\\Help\\comref.chm::/40_S02C/_cmu_commit_updates_.htm"
        elif h1text.lower() == 'cnt':
            path = "hh.exe C:\\Unisys\\Clients\\Help\\comref.chm::/40_S02C/cnt_and_cnt_count_.htm"
        elif h1text.lower() == 'csr':
            path = "hh.exe C:\\Unisys\\Clients\\Help\\comref.chm::/40_S02C/_csr_clear_subroutine_.htm"
        elif h1text.lower() == 'dat':
            path = "hh.exe C:\\Unisys\\Clients\\Help\\comref.chm::/40_S02D/DATE_and_DAT_Date_.htm"
        elif h1text.lower() == 'dc':
            path = "hh.exe C:\\Unisys\\Clients\\Help\\comref.chm::/40_S02D/_dc_date_calculator_.htm"
        elif h1text.lower() == 'dcpy':
            path = "hh.exe C:\\Unisys\\Clients\\Help\\comref.chm::/40_S02D/_dcpy_ddp_copy_.htm"
        elif h1text.lower() == 'dcr':
            path = "hh.exe C:\\Unisys\\Clients\\Help\\comref.chm::/40_S02D/DECODE_and_DCR_Decode_Report_.htm"
        elif h1text.lower() == 'dcu':
            path = "hh.exe C:\\Unisys\\Clients\\Help\\comref.chm::/40_S02D/_dcu_decommit_updates_.htm"
        elif h1text.lower() == 'dde':
            path = "hh.exe C:\\Unisys\\Clients\\Help\\comref.chm::/40_S02D/_DDE_Dynamic_Data_Exchange_Interface_.htm"
        elif h1text.lower() == 'ddi':
            path = "hh.exe C:\\Unisys\\Clients\\Help\\comref.chm::/40_S02D/_ddi_data_definition_information_.htm"
        elif h1text.lower() == 'dec':
            path = "hh.exe C:\\Unisys\\Clients\\Help\\comref.chm::/40_S02D/_DEC_Decrement_Variable_.htm"
        elif h1text.lower() == 'def':
            path = "hh.exe C:\\Unisys\\Clients\\Help\\comref.chm::/40_S02D/_def_define_.htm"
        elif h1text.lower() == 'del':
            path = "hh.exe C:\\Unisys\\Clients\\Help\\comref.chm::/40_S02D/DEL_and_DEL_Delete_.htm"
        elif h1text.lower() == 'dev':
            path = "hh.exe C:\\Unisys\\Clients\\Help\\comref.chm::/40_S02D/dev_and_dev_device_.htm"
        elif h1text.lower() == 'dfa':
            path = "hh.exe C:\\Unisys\\Clients\\Help\\comref.chm::/40_S02D/_DFA_Defer_Add_.htm"
        elif h1text.lower() == 'dfc':
            path = "hh.exe C:\\Unisys\\Clients\\Help\\comref.chm::/40_S02D/_DFC_Set_Default_Color_.htm"
        elif h1text.lower() == 'dfu':
            path = "hh.exe C:\\Unisys\\Clients\\Help\\comref.chm::/40_S02D/_DFU_Defer_Updates_.htm"
        elif h1text.lower() == 'diag':
            path = "hh.exe C:\\Unisys\\Clients\\Help\\comref.chm::/40_S02D/_diag_(generating_diagnostic_reports).htm"
        elif h1text.lower() == 'dir':
            path = "hh.exe C:\\Unisys\\Clients\\Help\\comref.chm::/40_S02D/_dir_directory_.htm"
        elif h1text.lower() == 'dlr':
            path = "hh.exe C:\\Unisys\\Clients\\Help\\comref.chm::/40_S02D/DR_and_DLR_Delete_Report_.htm"
        elif h1text.lower() == 'dpur':
            path = "hh.exe C:\\Unisys\\Clients\\Help\\comref.chm::/40_S02D/_dpur_ddp_purge_.htm"
        elif h1text.lower() == 'drw':
            path = "hh.exe C:\\Unisys\\Clients\\Help\\comref.chm::/40_S02D/_drw_drawer_.htm"
        elif h1text.lower() == 'dsf':
            path = "hh.exe C:\\Unisys\\Clients\\Help\\comref.chm::/40_S02D/_DSF_Display_Form_.htm"
        elif h1text.lower() == 'dsg':
            path = "hh.exe C:\\Unisys\\Clients\\Help\\comref.chm::/40_S02G/G_and_DSG_Display_Graphics_.htm"
        elif h1text.lower() == 'dsm':
            path = "hh.exe C:\\Unisys\\Clients\\Help\\comref.chm::/40_S02D/_DSM_Display_Message_.htm"
        elif h1text.lower() == 'dsp':
            path = "hh.exe C:\\Unisys\\Clients\\Help\\comref.chm::/40_S02D/D_and_DSP_Display_Report_.htm"
        elif h1text.lower() == 'dsx':
            path = "hh.exe C:\\Unisys\\Clients\\Help\\comref.chm::/40_S02D/_DSX_Display_Report_and_Exit_.htm"
        elif h1text.lower() == 'dul':
            path = "hh.exe C:\\Unisys\\Clients\\Help\\comref.chm::/40_S02D/_DUL_Defer_Unlock_.htm"
        elif h1text.lower() == 'dup':
            path = "hh.exe C:\\Unisys\\Clients\\Help\\comref.chm::/40_S02X/XR_and_DUP_Duplicate_Report_.htm"
        elif h1text.lower() == 'dvs':
            path = "hh.exe C:\\Unisys\\Clients\\Help\\comref.chm::/40_S02D/_dvs_define_variable_size_.htm"
        elif h1text.lower() == 'ecl':
            path = "hh.exe C:\\Unisys\\Clients\\Help\\comref.chm::/40_S02E/ecl_and_ecl_exec_control_language.htm"
        elif h1text.lower() == 'ecr':
            path = "hh.exe C:\\Unisys\\Clients\\Help\\comref.chm::/40_S02E/ENCODE_and_ECR_Encode_Report_.htm"
        elif h1text.lower() == 'edt':
            path = "hh.exe C:\\Unisys\\Clients\\Help\\comref.chm::/40_S02E/_EDT_Define_Edit_Box_.htm"
        elif h1text.lower() == 'elt':
            path = "hh.exe C:\\Unisys\\Clients\\Help\\comref.chm::/40_S02E/elt_and_elt_element_.htm"
        elif h1text.lower() == 'el-':
            path = "hh.exe C:\\Unisys\\Clients\\Help\\comref.chm::/40_S02E/elt_and_el_element_delete_.htm"
        elif h1text.lower() == 'esr':
            path = "hh.exe C:\\Unisys\\Clients\\Help\\comref.chm::/40_S02E/_ESR_Exit_Subroutine_.htm"
        elif h1text.lower() == 'ext':
            path = "hh.exe C:\\Unisys\\Clients\\Help\\comref.chm::/40_S02E/EXT_and_EXT_Extract_.htm"
        elif h1text.lower() == 'fc':
            path = "hh.exe C:\\Unisys\\Clients\\Help\\comref.chm::/40_S02F/FC_and_FC_Format_Columns_.htm"
        elif h1text.lower() == 'fch':
            path = "hh.exe C:\\Unisys\\Clients\\Help\\comref.chm::/40_S02F/_fch_relational_aggregate_fetch_.htm"
        elif h1text.lower() == 'fdr':
            path = "hh.exe C:\\Unisys\\Clients\\Help\\comref.chm::/40_S02F/_fdr_find_and_read_line_.htm"
        elif h1text.lower() == 'fil':
            path = "hh.exe C:\\Unisys\\Clients\\Help\\comref.chm::/40_S02F/FILE_and_FIL_Create_File_.htm"
        elif h1text.lower() == 'fky':
            path = "hh.exe C:\\Unisys\\Clients\\Help\\comref.chm::/40_S02F/_FKY_Function_Key_.htm"
        elif h1text.lower() == 'fmt':
            path = "hh.exe C:\\Unisys\\Clients\\Help\\comref.chm::/40_S02F/_FMT_Format_.htm"
        elif h1text.lower() == 'fnd':
            path = "hh.exe C:\\Unisys\\Clients\\Help\\comref.chm::/40_S02F/F_and_FND_Find_.htm"
        elif h1text.lower() == 'fon':
            path = "hh.exe C:\\Unisys\\Clients\\Help\\comref.chm::/40_S02F/_FON_Font_.htm"
        elif h1text.lower() == 'goc':
            path = "hh.exe C:\\Unisys\\Clients\\Help\\comref.chm::/40_S02G/GOC_and_GOC_Generate_Organization_Charts_.htm"
        elif h1text.lower() == 'gs':
            path = "hh.exe C:\\Unisys\\Clients\\Help\\comref.chm::/40_S02G/GS_and_GS_Graphics_Scaler_.htm"
        elif h1text.lower() == 'gto':
            path = "hh.exe C:\\Unisys\\Clients\\Help\\comref.chm::/40_S02G/_GTO_Go_To_.htm"
        elif h1text.lower() == 'help':
            path = "hh.exe C:\\Unisys\\Clients\\Help\\comref.chm::/40_S02H/HELP_and_HELP_Help_.htm"
        elif h1text.lower() == 'hid':
            path = "hh.exe C:\\Unisys\\Clients\\Help\\comref.chm::/40_S02H/_HID_Hide_Control_.htm"
        elif h1text.lower() == 'hsh':
            path = "hh.exe C:\\Unisys\\Clients\\Help\\comref.chm::/40_S02H/_hsh_hash_.htm"
        elif h1text.lower() == 'idu':
            path = "hh.exe C:\\Unisys\\Clients\\Help\\comref.chm::/40_S02I/iu_and_idu_index_user_.htm"
        elif h1text.lower() == 'if':
            path = "hh.exe C:\\Unisys\\Clients\\Help\\comref.chm::/40_S02I/_IF_If_Conditional_.htm"
        elif h1text.lower() == 'inc':
            path = "hh.exe C:\\Unisys\\Clients\\Help\\comref.chm::/40_S02I/_INC_Increment_Variable_.htm"
        elif h1text.lower() == 'ind':
            path = "hh.exe C:\\Unisys\\Clients\\Help\\comref.chm::/40_S02I/I_and_IND_Index_.htm"
        elif h1text.lower() == 'inp':
            path = "hh.exe C:\\Unisys\\Clients\\Help\\comref.chm::/40_S02I/_INP_Accept_Input_.htm"
        elif h1text.lower() == 'juv':
            path = "hh.exe C:\\Unisys\\Clients\\Help\\comref.chm::/40_S02J/_juv_justify_variable_.htm"
        elif h1text.lower() == 'key':
            path = "hh.exe C:\\Unisys\\Clients\\Help\\comref.chm::/40_S02K/_KEY_Function_Key_Input_.htm"
        elif h1text.lower() == 'kll':
            path = "hh.exe C:\\Unisys\\Clients\\Help\\comref.chm::/40_S02K/KILL_and_KLL_Kill_.htm"
        elif h1text.lower() == 'lch':
            path = "hh.exe C:\\Unisys\\Clients\\Help\\comref.chm::/40_S02C/chg_and_lch_locate_and_change_.htm"
        elif h1text.lower() == 'lcv':
            path = "hh.exe C:\\Unisys\\Clients\\Help\\comref.chm::/40_S02L/_lcv_locate_and_change_variable_.htm"
        elif h1text.lower() == 'lda':
            path = "hh.exe C:\\Unisys\\Clients\\Help\\comref.chm::/40_S02L/_LDA_Load_Variable_Array_.htm"
        elif h1text.lower() == 'ldv':
            path = "hh.exe C:\\Unisys\\Clients\\Help\\comref.chm::/40_S02L/_LDV_Load_Variable_.htm"
        elif h1text.lower() == 'lfc':
            path = "hh.exe C:\\Unisys\\Clients\\Help\\comref.chm::/40_S02L/_LFC_Load_Format_Characters_.htm"
        elif h1text.lower() == 'lfn':
            path = "hh.exe C:\\Unisys\\Clients\\Help\\comref.chm::/40_S02L/_lfn_load_field_name_.htm"
        elif h1text.lower() == 'lgf':
            path = "hh.exe C:\\Unisys\\Clients\\Help\\comref.chm::/40_S02L/_lgf_log_off_relational_database_.htm"
        elif h1text.lower() == 'lgn':
            path = "hh.exe C:\\Unisys\\Clients\\Help\\comref.chm::/40_S02L/_LGN_Log_On_to_Relational_Database_.htm"
        elif h1text.lower() == 'lln':
            path = "hh.exe C:\\Unisys\\Clients\\Help\\comref.chm::/40_S02L/_lln_last_line_number_.htm"
        elif h1text.lower() == 'lna':
            path = "hh.exe C:\\Unisys\\Clients\\Help\\comref.chm::/40_S02a/append_line_and_lna.htm"
        elif h1text.lower() == 'lnd':
            path = "hh.exe C:\\Unisys\\Clients\\Help\\comref.chm::/40_S02D/delete_and_yank_line_and_lnd.htm"
        elif h1text.lower() == 'lng':
            path = "hh.exe C:\\Unisys\\Clients\\Help\\comref.chm::/40_S02L/LANG_and_LNG_Language_.htm"
        elif h1text.lower() == 'lni':
            path = "hh.exe C:\\Unisys\\Clients\\Help\\comref.chm::/40_S02I/Insert_Line_and_LNI.htm"
        elif h1text.lower() == 'lnk':
            path = "hh.exe C:\\Unisys\\Clients\\Help\\comref.chm::/40_S02L/_LNK_Link_to_Another_Run_.htm"
        elif h1text.lower() == 'lnm':
            path = "hh.exe C:\\Unisys\\Clients\\Help\\comref.chm::/40_S02M/Move_Line_and_LNM.htm"
        elif h1text.lower() == 'lnp':
            path = "hh.exe C:\\Unisys\\Clients\\Help\\comref.chm::/40_S02P/Put_Line_and_LNP.htm"
        elif h1text.lower() == 'lnx':
            path = "hh.exe C:\\Unisys\\Clients\\Help\\comref.chm::/40_S02D/duplicate_line_and_lnx.htm"
        elif h1text.lower() == 'lny':
            path = "hh.exe C:\\Unisys\\Clients\\Help\\comref.chm::/40_S02Y/Yank_Line_and_LNY.htm"
        elif h1text.lower() == 'ln+':
            path = "hh.exe C:\\Unisys\\Clients\\Help\\comref.chm::/40_S02a/add_line_and_ln_.htm"
        elif h1text.lower() == 'ln-':
            path = "hh.exe C:\\Unisys\\Clients\\Help\\comref.chm::/40_S02D/delete_line_and_ln_.htm"
        elif h1text.lower() == 'loc':
            path = "hh.exe C:\\Unisys\\Clients\\Help\\comref.chm::/40_S02L/LOC_and_LOC_Locate_.htm"
        elif h1text.lower() == 'lok':
            path = "hh.exe C:\\Unisys\\Clients\\Help\\comref.chm::/40_S02L/_LOK_Update_Lock_.htm"
        elif h1text.lower() == 'lsm':
            path = "hh.exe C:\\Unisys\\Clients\\Help\\comref.chm::/40_S02L/_LSM_Load_System_Message_.htm"
        elif h1text.lower() == 'lst':
            path = "hh.exe C:\\Unisys\\Clients\\Help\\comref.chm::/40_S02L/_LST_Define_List_Box_.htm"
        elif h1text.lower() == 'lzr':
            path = "hh.exe C:\\Unisys\\Clients\\Help\\comref.chm::/40_S02L/LZ_and_LZR_Line_Zero_.htm"
        elif h1text.lower() == 'mau':
            path = "hh.exe C:\\Unisys\\Clients\\Help\\comref.chm::/40_S02M/MA_and_MCH_Match_MAU_and_MAU_Match_Update_.htm"
        elif h1text.lower() == 'mch':
            path = "hh.exe C:\\Unisys\\Clients\\Help\\comref.chm::/40_S02M/MA_and_MCH_Match_MAU_and_MAU_Match_Update_.htm"
        elif h1text.lower() == 'mbx':
            path = "hh.exe C:\\Unisys\\Clients\\Help\\comref.chm::/40_S02M/_MBX_Define_Message_Box_.htm"
        elif h1text.lower() == 'mnu':
            path = "hh.exe C:\\Unisys\\Clients\\Help\\comref.chm::/40_S02M/_MNU_Define_Menu_Bar_.htm"
        elif h1text.lower() == 'mql':
            path = "hh.exe C:\\Unisys\\Clients\\Help\\comref.chm::/40_S02M/_mql_mapper_query_language_.htm"
        elif h1text.lower() == 'msg':
            path = "hh.exe C:\\Unisys\\Clients\\Help\\comref.chm::/40_S02M/_msg_message_to_console_.htm"
        elif h1text.lower() == 'namdmp':
            path = "hh.exe C:\\Unisys\\Clients\\Help\\comref.chm::/40_S02N/_NAMDMP.htm"
        elif h1text.lower() == 'namlst':
            path = "hh.exe C:\\Unisys\\Clients\\Help\\comref.chm::/40_S02N/_NAMLST.htm"
        elif h1text.lower() == 'net':
            path = "hh.exe C:\\Unisys\\Clients\\Help\\comref.chm::/40_S02N/_NET_Network_Sign_On_.htm"
        elif h1text.lower() == 'nof':
            path = "hh.exe C:\\Unisys\\Clients\\Help\\comref.chm::/40_S02N/_NOF_Network_Off_.htm"
        elif h1text.lower() == 'nrd':
            path = "hh.exe C:\\Unisys\\Clients\\Help\\comref.chm::/40_S02N/_NRD_Network_Read_.htm"
        elif h1text.lower() == 'nrm':
            path = "hh.exe C:\\Unisys\\Clients\\Help\\comref.chm::/40_S02N/_NRM_Network_Remote_.htm"
        elif h1text.lower() == 'nrn':
            path = "hh.exe C:\\Unisys\\Clients\\Help\\comref.chm::/40_S02N/_NRN_Network_Run_.htm"
        elif h1text.lower() == 'nrt':
            path = "hh.exe C:\\Unisys\\Clients\\Help\\comref.chm::/40_S02N/_NRT_Network_Return_.htm"
        elif h1text.lower() == 'nwr':
            path = "hh.exe C:\\Unisys\\Clients\\Help\\comref.chm::/40_S02N/_NWR_Network_Write_.htm"
        elif h1text.lower() == 'ok':
            path = "hh.exe C:\\Unisys\\Clients\\Help\\comref.chm::/40_S02O/OK_and_OK_Acknowledge_Message_.htm"
        elif h1text.lower() == 'os':
            path = "hh.exe C:\\Unisys\\Clients\\Help\\comref.chm::/40_S02O/os_and_os_operating_system_interface_.htm"
        elif h1text.lower() == 'oum':
            path = "hh.exe C:\\Unisys\\Clients\\Help\\comref.chm::/40_S02O/_OUM_Output_Mask_.htm"
        elif h1text.lower() == 'out':
            path = "hh.exe C:\\Unisys\\Clients\\Help\\comref.chm::/40_S02O/_OUT_Output_.htm"
        elif h1text.lower() == 'pc':
            path = "hh.exe C:\\Unisys\\Clients\\Help\\comref.chm::/40_S02P/_PC_Run_PC_Program_.htm"
        elif h1text.lower() == 'pcf':
            path = "hh.exe C:\\Unisys\\Clients\\Help\\comref.chm::/40_S02P/_PCF_PC_File_.htm"
        elif h1text.lower() == 'pcr':
            path = "hh.exe C:\\Unisys\\Clients\\Help\\comref.chm::/40_S02P/_PCR_Transfer_from_PC_.htm"
        elif h1text.lower() == 'pcw':
            path = "hh.exe C:\\Unisys\\Clients\\Help\\comref.chm::/40_S02P/_PCW_MAPPER_to_PC_.htm"
        elif h1text.lower() == 'pic':
            path = "hh.exe C:\\Unisys\\Clients\\Help\\comref.chm::/40_S02P/_PIC_Display_Picture_.htm"
        elif h1text.lower() == 'pnt':
            path = "hh.exe C:\\Unisys\\Clients\\Help\\comref.chm::/40_S02P/PNT_Paint_and_PNT_Refresh_Screen_.htm"
        elif h1text.lower() == 'prt':
            path = "hh.exe C:\\Unisys\\Clients\\Help\\comref.chm::/40_S02P/PR_and_PRT_Print_.htm"
        elif h1text.lower() == 'psw':
            path = "hh.exe C:\\Unisys\\Clients\\Help\\comref.chm::/40_S02P/psw_and_psw_password_.htm"
        elif h1text.lower() == 'qcls':
            path = "hh.exe C:\\Unisys\\Clients\\Help\\comref.chm::/40_S02Q/_qcls_close_message_queue_object_.htm"
        elif h1text.lower() == 'qctl':
            path = "hh.exe C:\\Unisys\\Clients\\Help\\comref.chm::/40_S02Q/_qctl_queue_control_.htm"
        elif h1text.lower() == 'qget':
            path = "hh.exe C:\\Unisys\\Clients\\Help\\comref.chm::/40_S02Q/_QGET_Get_Message_from_Message_Queue_.htm"
        elif h1text.lower() == 'qinq':
            path = "hh.exe C:\\Unisys\\Clients\\Help\\comref.chm::/40_S02Q/_QINQ_Inquire_on_Object_Attribute_.htm"
        elif h1text.lower() == 'qopn':
            path = "hh.exe C:\\Unisys\\Clients\\Help\\comref.chm::/40_S02Q/_QOPN_Open_Message_Queue_Object_.htm"
        elif h1text.lower() == 'qput':
            path = "hh.exe C:\\Unisys\\Clients\\Help\\comref.chm::/40_S02Q/_QPUT_Put_Message_on_Message_Queue_.htm"
        elif h1text.lower() == 'qrel':
            path = "hh.exe C:\\Unisys\\Clients\\Help\\comref.chm::/40_S02Q/_qrel_release_message_.htm"
        elif h1text.lower() == 'qrsp':
            path = "hh.exe C:\\Unisys\\Clients\\Help\\comref.chm::/40_S02Q/_QRSP_Send_Response_Message_.htm"
        elif h1text.lower() == 'qsnd':
            path = "hh.exe C:\\Unisys\\Clients\\Help\\comref.chm::/40_S02Q/_qsnd_send_message_no_response_.htm"
        elif h1text.lower() == 'qsnr':
            path = "hh.exe C:\\Unisys\\Clients\\Help\\comref.chm::/40_S02Q/_qsnr_send_message_expect_response_.htm"
        elif h1text.lower() == 'ram':
            path = "hh.exe C:\\Unisys\\Clients\\Help\\comref.chm::/40_S02R/_ram_relational_aggregate_modify_.htm"
        elif h1text.lower() == 'rar':
            path = "hh.exe C:\\Unisys\\Clients\\Help\\comref.chm::/40_S02R/_RAR_Register_Abort_Routine_.htm"
        elif h1text.lower() == 'rdb':
            path = "hh.exe C:\\Unisys\\Clients\\Help\\comref.chm::/40_S02R/RDB_and_RDB_Run_Debug_.htm"
        elif h1text.lower() == 'rdc':
            path = "hh.exe C:\\Unisys\\Clients\\Help\\comref.chm::/40_S02R/_RDC_Read_Continuous_.htm"
        elif h1text.lower() == 'rdl':
            path = "hh.exe C:\\Unisys\\Clients\\Help\\comref.chm::/40_S02R/_RDL_Read_Line_.htm"
        elif h1text.lower() == 'reh':
            path = "hh.exe C:\\Unisys\\Clients\\Help\\comref.chm::/40_S02R/RETR_and_REH_Retrieve_Report_from_History_.htm"
        elif h1text.lower() == 'rel':
            path = "hh.exe C:\\Unisys\\Clients\\Help\\comref.chm::/40_S02R/Release_Display_and_REL.htm"
        elif h1text.lower() == 'relrnm':
            path = "hh.exe C:\\Unisys\\Clients\\Help\\comref.chm::/40_S02R/_RELRNM_Release_Rename_.htm"
        elif h1text.lower() == 'rep':
            path = "hh.exe C:\\Unisys\\Clients\\Help\\comref.chm::/40_S02R/REP_and_REP_Replace_Report_.htm"
        elif h1text.lower() == 'rer':
            path = "hh.exe C:\\Unisys\\Clients\\Help\\comref.chm::/40_S02R/_RER_Register_Error_Routine_.htm"
        elif h1text.lower() == 'ret':
            path = "hh.exe C:\\Unisys\\Clients\\Help\\comref.chm::/40_S02R/RETR_and_REH_Retrieve_Report_from_History_.htm"
        elif h1text.lower() == 'return':
            path = "hh.exe C:\\Unisys\\Clients\\Help\\comref.chm::/40_S02R/_RETURN_Return_Call_Routine_.htm"
        elif h1text.lower() == 'rfm':
            path = "hh.exe C:\\Unisys\\Clients\\Help\\comref.chm::/40_S02R/rf_and_rfm_reformat_report_.htm"
        elif h1text.lower() == 'rln':
            path = "hh.exe C:\\Unisys\\Clients\\Help\\comref.chm::/40_S02R/_RLN_Read_Line_Next_.htm"
        elif h1text.lower() == 'rnm':
            path = "hh.exe C:\\Unisys\\Clients\\Help\\comref.chm::/40_S02R/_RNM_Rename_.htm"
        elif h1text.lower() == 'rpw':
            path = "hh.exe C:\\Unisys\\Clients\\Help\\comref.chm::/40_S02R/rpsw_and_rpw_read_password_.htm"
        elif h1text.lower() == 'rrn':
            path = "hh.exe C:\\Unisys\\Clients\\Help\\comref.chm::/40_S02R/RR_and_RRN_Remote_Run_.htm"
        elif h1text.lower() == 'rs':
            path = "hh.exe C:\\Unisys\\Clients\\Help\\comref.chm::/40_S02R/RS_and_RS_Run_Status_.htm"
        elif h1text.lower() == 'rsi':
            path = "hh.exe C:\\Unisys\\Clients\\Help\\comref.chm::/40_S02R/rsi_and_rsi_remote_symbiont_interface_.htm"
        elif h1text.lower() == 'rsl':
            path = "hh.exe C:\\Unisys\\Clients\\Help\\comref.chm::/40_S02R/rslt_and_rsl_create_result_copy_.htm"
        elif h1text.lower() == 'rsr':
            path = "hh.exe C:\\Unisys\\Clients\\Help\\comref.chm::/40_S02R/_RSR_Run_Subroutine_.htm"
        elif h1text.lower() == 'rtn':
            path = "hh.exe C:\\Unisys\\Clients\\Help\\comref.chm::/40_S02R/_RTN_Return_Remote_.htm"
        elif h1text.lower() == 'run':
            path = "hh.exe C:\\Unisys\\Clients\\Help\\comref.chm::/40_S02R/run.htm"
        elif h1text.lower() == 'sc':
            path = "hh.exe C:\\Unisys\\Clients\\Help\\comref.chm::/40_S02S/_SC_Screen_Control_.htm"
        elif h1text.lower() == 'sch':
            path = "hh.exe C:\\Unisys\\Clients\\Help\\comref.chm::/40_S02S/_SCH_Schedule_Run_Statements_.htm"
        elif h1text.lower() == 'scn':
            path = "hh.exe C:\\Unisys\\Clients\\Help\\comref.chm::/40_S02S/_scn_screen_size_.htm"
        elif h1text.lower() == 'sen':
            path = "hh.exe C:\\Unisys\\Clients\\Help\\comref.chm::/40_S02S/SEND_and_SEN_Send_Report_.htm"
        elif h1text.lower() == 'sfc':
            path = "hh.exe C:\\Unisys\\Clients\\Help\\comref.chm::/40_S02S/_SFC_Set_Format_Characters_.htm"
        elif h1text.lower() == 'sgget':
            path = "hh.exe C:\\Unisys\\Clients\\Help\\comref.chm::/40_S02S/_SGGET_Session_Global_Report_Get_.htm"
        elif h1text.lower() == 'sgput':
            path = "hh.exe C:\\Unisys\\Clients\\Help\\comref.chm::/40_S02S/_SGPUT_Session_Global_Report_Put_.htm"
        elif h1text.lower() == 'shw':
            path = "hh.exe C:\\Unisys\\Clients\\Help\\comref.chm::/40_S02S/_SHW_Show_Control_.htm"
        elif h1text.lower() == 'si':
            path = "hh.exe C:\\Unisys\\Clients\\Help\\comref.chm::/40_S02S/_si.htm"
        elif h1text.lower() == 'siz':
            path = "hh.exe C:\\Unisys\\Clients\\Help\\comref.chm::/40_S02S/_SIZ_Control_Size_.htm"
        elif h1text.lower() == 'snu':
            path = "hh.exe C:\\Unisys\\Clients\\Help\\comref.chm::/40_S02S/SNU_and_SNU_Send_Report_to_User_.htm"
        elif h1text.lower() == 'sor':
            path = "hh.exe C:\\Unisys\\Clients\\Help\\comref.chm::/40_S02S/SORT_SOR_Sort_SORTR_SRR_Sort_and_Replace_.htm"
        elif h1text.lower() == 'spi':
            path = "hh.exe C:\\Unisys\\Clients\\Help\\comref.chm::/40_S02S/_spi_stored_procedure_interface_.htm"
        elif h1text.lower() == 'sq':
            path = "hh.exe C:\\Unisys\\Clients\\Help\\comref.chm::/40_S02S/_sq.htm"
        elif h1text.lower() == 'sql':
            path = "hh.exe C:\\Unisys\\Clients\\Help\\comref.chm::/40_S02S/_SQL_Submit_SQL_.htm"
        elif h1text.lower() == 'srh':
            path = "hh.exe C:\\Unisys\\Clients\\Help\\comref.chm::/40_S02S/S_and_SRH_Search_SU_and_SRU_Search_Update_.htm"
        elif h1text.lower() == 'srr':
            path = "hh.exe C:\\Unisys\\Clients\\Help\\comref.chm::/40_S02S/_srr_sort_and_replace_.htm"
        elif h1text.lower() == 'sru':
            path = "hh.exe C:\\Unisys\\Clients\\Help\\comref.chm::/40_S02S/_sru_search_update_.htm"
        elif h1text.lower() == 'stn':
            path = "hh.exe C:\\Unisys\\Clients\\Help\\comref.chm::/40_S02S/_stn_station_information_.htm"
        elif h1text.lower() == 'str':
            path = "hh.exe C:\\Unisys\\Clients\\Help\\comref.chm::/40_S02S/START_and_STR_Start_.htm"
        elif h1text.lower() == 'sub':
            path = "hh.exe C:\\Unisys\\Clients\\Help\\comref.chm::/40_S02S/_SUB_Subtotal_.htm"
        elif h1text.lower() == 'sys':
            path = "hh.exe C:\\Unisys\\Clients\\Help\\comref.chm::/40_S02S/SYSTEM_and_SYS_System_.htm"
        elif h1text.lower() == 'tip':
            path = "hh.exe C:\\Unisys\\Clients\\Help\\comref.chm::/40_S02T/_TIP_Tool_Tip_.htm"
        elif h1text.lower() == 'tot':
            path = "hh.exe C:\\Unisys\\Clients\\Help\\comref.chm::/40_S02T/TOT_and_TOT_Totalize_.htm"
        elif h1text.lower() == 'tpc':
            path = "hh.exe C:\\Unisys\\Clients\\Help\\comref.chm::/40_S02T/_tpc_client_interface_.htm"
        elif h1text.lower() == 'tps':
            path = "hh.exe C:\\Unisys\\Clients\\Help\\comref.chm::/40_S02T/_TPS_Server_Interface_.htm"
        elif h1text.lower() == 'trc':
            path = "hh.exe C:\\Unisys\\Clients\\Help\\comref.chm::/40_S02T/_trc_trace_relational_syntax_.htm"
        elif h1text.lower() == 'txt':
            path = "hh.exe C:\\Unisys\\Clients\\Help\\comref.chm::/40_S02T/_TXT_Define_Text_Box_.htm"
        elif h1text.lower() == 'ulk':
            path = "hh.exe C:\\Unisys\\Clients\\Help\\comref.chm::/40_S02U/UPD_and_UPD_Update_.htm"
        elif h1text.lower() == 'unx':
            path = "hh.exe C:\\Unisys\\Clients\\Help\\comref.chm::/40_S02U/UNIX_and_UNX_UNIX_Interface_.htm"
        elif h1text.lower() == 'upd':
            path = "hh.exe C:\\Unisys\\Clients\\Help\\comref.chm::/_ULK_Unlock_.htm"
        elif h1text.lower() == 'use':
            path = "hh.exe C:\\Unisys\\Clients\\Help\\comref.chm::/40_S02U/_USE_Use_Variable_Name_.htm"
        elif h1text.lower() == 'wat':
            path = "hh.exe C:\\Unisys\\Clients\\Help\\comref.chm::/40_S02W/_WAT_Wait_.htm"
        elif h1text.lower() == 'wdc':
            path = "hh.exe C:\\Unisys\\Clients\\Help\\comref.chm::/40_S02W/WC_and_WDC_Word_Change_.htm"
        elif h1text.lower() == 'win':
            path = "hh.exe C:\\Unisys\\Clients\\Help\\comref.chm::/40_S02W/_WIN_Define_Window_Display_.htm"
        elif h1text.lower() == 'wdl':
            path = "hh.exe C:\\Unisys\\Clients\\Help\\comref.chm::/40_S02W/WL_and_WDL_Word_Locate_.htm"
        elif h1text.lower() == 'wpr':
            path = "hh.exe C:\\Unisys\\Clients\\Help\\comref.chm::/40_S02W/wp_and_wpr_word_process_.htm"
        elif h1text.lower() == 'wrl':
            path = "hh.exe C:\\Unisys\\Clients\\Help\\comref.chm::/40_S02W/_wrl_write_line_.htm"
        elif h1text.lower() == 'xit':
            path = "hh.exe C:\\Unisys\\Clients\\Help\\comref.chm::/40_S02X/X_and_XIT_Sign_Off_User_Session_.htm"
        elif h1text.lower() == 'xqt':
            path = "hh.exe C:\\Unisys\\Clients\\Help\\comref.chm::/40_S02X/_XQT_Execute_.htm"
        elif h1text.lower() == 'xun':
            path = "hh.exe C:\\Unisys\\Clients\\Help\\comref.chm::/40_S02X/_xun_exit_mapper_.htm"
        else:
            path = "hh.exe C:\\Unisys\\Clients\\Help\\BIS.chm"

        subprocess.Popen(path)
