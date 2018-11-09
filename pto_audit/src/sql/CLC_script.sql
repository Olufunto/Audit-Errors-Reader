truncate table audit_errors_clc; 
DECLARE
  v_max_seq audit_trail.seq%type;
  v_min_seq audit_trail.seq%type;
  v_batch_no audit_trail.batch_no%type;
  v_drn audit_trail.drn%type;
  v_posting_date audit_trail.posting_dt%type;
  v_chg_code audit_trail.chg_code%type;
  v_op_num audit_trail.op_num%type;
  v_before audit_trail.before%type;
  v_after audit_trail.after%type;
  v_seq audit_trail.seq%type;
  v_queue audit_trail.queue%type;
  CURSOR vcur
  IS
    SELECT distinct  drn

    FROM audit_trail
    WHERE (drn) IN
      ( SELECT drn FROM audit_trail WHERE chg_code ='10'
      )
  AND drn NOT IN
    (SELECT drn
    FROM
      (SELECT COUNT(1),
        drn
      FROM audit_trail  WHERE chg_code ='10'
      GROUP BY drn
      HAVING COUNT(1) = 1
      )
    )
  AND chg_code       = '10' 
  AND NVL(before,'xx') <> NVL(AFTER,'xx')
  ORDER BY drn;

BEGIN
  FOR i IN vcur
  LOOP
    SELECT MIN(seq),
      MAX(seq)
    INTO v_min_seq,
      v_max_seq
    FROM audit_trail
    WHERE chg_code =  '10'
    AND drn         =i.drn
    
    AND NVL(before,'xx') <> NVL(AFTER,'xx');
    --dbms_output.put_line (i.drn||'~~'||i.batch_no||'~~'||i.before||'~~'||i.after||'~'||v_min_seq||'~~'||v_max_seq);
    SELECT batch_no ,
      drn,
      posting_dt,
      chg_code,
      op_num,
      before,
      queue
    INTO v_batch_no ,
      v_drn,
      v_posting_date,
      v_chg_code,
      v_op_num,
      v_before,
      v_queue
    FROM audit_trail
    WHERE drn = i.drn
    AND seq   = v_min_seq;
    SELECT AFTER
    INTO v_after
    FROM audit_trail
    WHERE drn = i.drn
    AND seq   = v_max_seq;
    INSERT
    INTO audit_errors_clc VALUES
      (
        v_batch_no,
        v_posting_date,
        v_drn,
        v_op_num,
        v_queue,
        v_chg_code,
        v_before,
        v_after,
        v_min_seq
      );
    COMMIT;
  END LOOP;
  
  COMMIT;
END;
/