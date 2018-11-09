
with open('C:\\Repo\\pto_audit\\output\\data.ctl','a') as x:
    print('LOAD DATA ', file=x)
    print("""INFILE	'C:\Repo\pto_audit\output\db_data.csv'""", file =x )
    print("""BADFILE 'C:\Repo\pto_audit\output\db_data.bad'""", file =x )
    print("""DISCARDFILE	'C:\Repo\pto_audit\output\db_data.dsc' """, file=x)
    print('INSERT INTO TABLE audit_trail ' , file=x)
    print("""FIELDS TERMINATED BY "," OPTIONALLY ENCLOSED BY '"' TRAILING NULLCOLS """,file=x)
    print("(batch_no,posting_dt,drn,op_num,queue,chg_code,before,after,seq)",file=x)