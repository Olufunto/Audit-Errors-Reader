commit;

update audit_trail set batch_no = rtrim(ltrim(batch_no)), posting_dt = rtrim(ltrim(posting_dt)),
drn = rtrim(ltrim(drn)), op_num = rtrim(ltrim(op_num)) , queue = rtrim(ltrim(queue)), chg_code = rtrim(ltrim(chg_code)),
before = rtrim(ltrim(before)) , after = rtrim(ltrim(after)), seq = ltrim(rtrim(seq));
commit;

delete from audit_trail where op_num is null;
commit; 