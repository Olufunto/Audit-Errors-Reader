truncate table audit_errors_ofc;

DECLARE
  v_seq_max audit_trail.seq%type;
  v_seq_min audit_trail.seq%type;
  vv_seq audit_trail.seq%type;
  v_drn audit_trail.drn%type;
  v_after audit_trail.after%type;
  v_before audit_trail.before%type;
  v_op_num audit_trail.op_num%type;
  v_orig_operator audit_trail.op_num%type;
  v_chg_code audit_trail.chg_code%type;
  v_posting_dt audit_trail.posting_dt%type;
  v_batch_no audit_trail.batch_no%type;
  v_queue audit_trail.queue%type;
  v_work_after_min audit_trail.before%type;
  v_work_after_max audit_trail.after%type;
  v_op_num_before audit_trail.op_num%type;
   v_op_num_after audit_trail.op_num%type;
  
  CURSOR vcur
  IS
    SELECT DISTINCT drn
    FROM audit_trail
    WHERE drn IN
      (SELECT DISTINCT drn FROM audit_trail WHERE chg_code='5'
      )
  AND drn IN
    (SELECT drn
    FROM
      ( SELECT COUNT(1) , drn FROM audit_trail GROUP BY drn HAVING COUNT(1) <> 1
      )
    ) ;
  data_found EXCEPTION;
BEGIN

  FOR i IN vcur
  LOOP
    BEGIN
      SELECT MAX(seq),
        MIN(seq)
      INTO v_seq_max,
        v_seq_min
      FROM audit_trail
      WHERE drn             = i.drn
      AND chg_code          ='5'
      AND NVL(before,'xx') <> NVL(AFTER,'xx');

      SELECT op_num
      INTO v_orig_operator
      FROM audit_trail
      WHERE seq             = v_seq_min
      AND chg_code          ='5' and drn = i.drn
      AND NVL(before,'xx') <> NVL(AFTER,'xx');
      IF v_seq_max         <> v_seq_min THEN
        SELECT AFTER , op_num
        INTO v_work_after_min, v_op_num_before
        FROM audit_trail
        WHERE seq = v_seq_min
        AND drn   = i.drn;
        SELECT AFTER ,op_num
        INTO v_work_after_max ,v_op_num_after
        FROM audit_trail
        WHERE seq            = v_seq_max
        AND drn              = i.drn;
        IF v_work_after_min <> v_work_after_max and v_op_num_after <> v_op_num_before  THEN
          SELECT seq,
            drn,
            op_num,
            batch_no,
            before,
            AFTER ,
            posting_dt ,
            chg_code,
            queue
          INTO vv_seq,
            v_drn ,
            v_op_num ,
            v_batch_no,
            v_before ,
            v_after ,
            v_posting_dt,
            v_chg_code,
            v_queue
          FROM audit_trail
          WHERE seq             =v_seq_max
          AND drn               = i.drn
          AND NVL(before,'xx') <> NVL(AFTER,'xx') ;
          --dbms_output.put_line(vv_seq||' , ' || v_drn ||' , ' ||  v_op_num||' , ' || v_batch_no||' , ' ||  v_before ||' , ' ||  v_after ||' , ' ||  v_posting_dt||' , '||v_chg_code);
          INSERT
          INTO audit_errors_ofc VALUES
            (
              v_batch_no,
              v_posting_dt,
              v_drn,
              v_orig_operator,
              v_queue,
              v_chg_code,
              v_before,
              v_after,
              vv_seq
            );
          COMMIT;
        END IF;
      END IF;
    
    EXCEPTION
    WHEN no_data_found THEN
      CONTINUE;
    END;
  END LOOP;
END;
/