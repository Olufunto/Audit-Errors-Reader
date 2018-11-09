setwd("C:\\Repo\\pto_audit\\Report")
library("RODBC")
connect <- odbcConnect("xe",uid = "pto",pwd = "pto")
dataframe <- sqlQuery(connect, query = "select * from audit_trail where drn in (select drn from audit_errors_ak) and chg_code in ('114','1') order by drn,seq,posting_dt")
write.csv(dataframe,file= "AK_RPT_Detailed.csv",row.names = FALSE)
dataframe <- sqlQuery(connect, query = "select count(1) Number_of_errors,get_user(op_num) NAME,op_num,posting_dt from audit_errors_ak group by posting_dt,op_num order by op_num,posting_dt")
write.csv(dataframe,file= "AK_RPT_Summary.csv",row.names = FALSE)

dataframe <- sqlQuery(connect, query = "select * from audit_trail where drn in (select drn from audit_errors_ofc) and chg_code ='5' order by drn,seq,posting_dt")
write.csv(dataframe,file= "OFC_RPT_Detailed.csv",row.names = FALSE)
dataframe <- sqlQuery(connect, query = "select count(1) Number_of_errors,get_user(op_num) NAME,op_num,posting_dt from audit_errors_ofc group by posting_dt,op_num order by op_num,posting_dt")
write.csv(dataframe,file= "OFC_RPT_Summary.csv",row.names = FALSE)

dataframe <- sqlQuery(connect, query = "select * from audit_trail where drn in (select drn from audit_errors_clc) and chg_code ='10' order by drn,seq,posting_dt")
write.csv(dataframe,file= "CLC_RPT_Detailed.csv",row.names = FALSE)
dataframe <- sqlQuery(connect, query = "select count(1) Number_of_errors,get_user(op_num) NAME,op_num,posting_dt from audit_errors_clc group by posting_dt,op_num order by op_num,posting_dt")
write.csv(dataframe,file= "CLC_RPT_Summary.csv",row.names = FALSE)

dataframe <- sqlQuery(connect, query = "select op_num,count(1) Number_of_occurences,get_user(op_num) name ,rep_module queue ,posting_dt , get_drn(op_num,posting_dt, rep_module) error_desc, 'Input Error' as Error_type , 'Low' as Priority from audit_errors_all group by op_num,rep_module,posting_dt, get_user(op_num) , get_drn(op_num,posting_dt, rep_module) order by get_user(op_num),rep_module")
write.csv(dataframe,file= "Consolidated_Summary.csv",row.names = FALSE)

odbcClose(connect)
