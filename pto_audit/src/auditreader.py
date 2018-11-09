
"""
Created on Tue Aug  7 09:06:24 2018

@author: 185467545
"""

import re
import os
import sys

inputfile = sys.argv[1]
operator_line = ""
operator_name = ""
report_date = ""
v_queue = ""
v_session_st_time = ""
pattern_date = "^(([0-9])|([0-2][0-9])|([3][0-1]))/(Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec)/\d{4}$"
pattern_number = r'\d{10}'
pattern_op_num = r'\d{3}'
filepath = inputfile
drn_num =""
op_num = ""
batch_no =""
posting_date = ""
a = ""
with open(filepath) as fp:
    for cnt, line in enumerate(fp):
        line = line.replace('\n\n', '\n').replace('\n\n', '\n')
        line = line.replace(" Resource Allocation Report                    Workgroup: FSSOperators                  ",
                            "")
        line = line.replace(" RBC", "")
        line = line.replace("*", " ")
        line = line.replace("Audit Exceptions Report", "")
        line = line.replace("         DRN           Oper              Activity             Chg               Before                         After","")
        line = line.replace("                       No.                                    Code","")
        line = line.replace(" --------------------  ----  -------------------------------  ----  -----------------------------  -----------------------------","")
        line = line.replace(
            " A session marked with an   indicates some data may be lost due to abnormal termination of operator application.",
            "")
        line = line.replace(" Operator totals and cumulative operator totals do not include Advice Notice sessions.",
                            "")
        line = line.replace("             END OF REPORT","")
        if line.find('Page') != -1:
            page_line = line.find('Page')

            page_diff = len(line) -page_line
            page_string = line[page_line:len(line)]
            line = line.replace(page_string,"")

        if line.find('Cycle:') != -1:
            cycleline =  line.find('Cycle:')
            cycle_string = line[cycleline:cycleline+9]
            line = line.replace(cycle_string,"")
        if line.find('Host Entry:') != -1:
            host_line = line.find('Host Entry:')
            host_string = line[host_line:host_line+16]
            line = line.replace(host_string,"")
        if line.find('Entry:') != -1:
            entry_line = line.find('Entry:')
            entry_string = line[entry_line:entry_line+13]
            line = line.replace(entry_string,"")
        if line.find('Posting Date:') != -1:
            posting_dt_line = line.find('Posting Date:')
            posting_date = line[posting_dt_line+14:posting_dt_line+25]
            posting_date_string = line[posting_dt_line:posting_dt_line+25]
            line = line.replace(posting_date_string,"")
        if line.find('Batch:') != -1:
            batch_line = line.find('Batch:')
            batch_no = line[batch_line+7:batch_line+12]
            batch_no_string = line[batch_line:batch_line+12]
            line = line.replace(batch_no_string, "")
        op_num = line[23:27]
        v_queue = line[29:61]
        v_chg_code = line [62:67]
        v_before = line [68:98]
        v_after = line [99:129]
        v_comma = ","
        insert_prefix = "insert into audit_trail values ('"
        insert_suffix = "');"
        old_drn_num = ""
        if line.rstrip() =="":           
            a="a"
        else:           
            a="a"
            if re.match(pattern_number, line[11:22]):
                drn_num = line[11:22]
                old_drn_num = drn_num               
            else:                
                a="a"                       
        if v_after.rstrip() =="" and v_before.rstrip() =="" and  v_chg_code.rstrip() =="" and v_queue.rstrip()== "" and op_num.rstrip() =="":           
            a="a"
        else:
            a= "a"            
            with open('C:\\Repo\\pto_audit\\output\\db_data.csv','a') as z:
                print( batch_no.rstrip(), v_comma.rstrip(), posting_date.rstrip(), v_comma.rstrip(), drn_num.rstrip(), v_comma.rstrip(),
                  op_num.rstrip(), v_comma.rstrip(), v_queue.rstrip(), v_comma.rstrip(), v_chg_code.rstrip(), v_comma.rstrip(), v_before.rstrip(),
                  v_comma.rstrip(), v_after.rstrip(),v_comma.rstrip(), cnt, file=z)
                #print("Print transformed data ...")               
print("#### File ",inputfile,"processing completed!!!")

