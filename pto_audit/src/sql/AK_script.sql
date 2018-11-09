truncate table audit_errors_ak;

DECLARE
  v_max_seq audit_trail.seq%type;
  v_min_seq audit_trail.seq%type;
  v_batch_no audit_trail.batch_no%type;
  v_drn audit_trail.drn%type;
  v_posting_dt audit_trail.posting_dt%type;
  v_chg_code audit_trail.chg_code%type;
  v_op_num audit_trail.op_num%type;
  v_before audit_trail.before%type;
  v_after audit_trail.after%type;
  v_seq audit_trail.seq%type;
  v_queue audit_trail.queue%type;
  v_seq audit_trail.seq%type;
  CURSOR vcur
  IS
    SELECT DISTINCT drn
    FROM audit_trail
    WHERE drn IN
      ( SELECT DISTINCT drn FROM audit_trail WHERE chg_code ='114'
      )
  AND drn NOT IN
    (SELECT drn
    FROM
      (SELECT COUNT(1),
        drn
      FROM audit_trail
      WHERE chg_code IN ('114','1')
      GROUP BY drn
      HAVING COUNT(1) = 1
      )
    )
  AND NVL(ltrim(rtrim(before)),'xx') <> NVL(ltrim(rtrim(AFTER)),'xx');
 
BEGIN
  FOR i IN vcur
  LOOP
    SELECT MAX(seq)
    INTO v_max_seq
    FROM audit_trail
    WHERE drn                           = i.drn
    AND chg_code                        = '1'
    AND NVL(ltrim(rtrim(before)),'xx') <> NVL(ltrim(rtrim(AFTER)),'xx');
    SELECT MIN(seq)
    INTO v_min_seq
    FROM audit_trail
    WHERE drn                           = i.drn
    AND chg_code                        = '114'
    AND NVL(ltrim(rtrim(before)),'xx') <> NVL(ltrim(rtrim(AFTER)),'xx');
    SELECT OP_NUM
    INTO V_OP_NUM
    FROM audit_trail
    WHERE drn     = i.drn
    AND seq       = v_min_seq;
    IF v_max_seq <> v_min_seq THEN
      SELECT batch_no ,
        posting_dt,
        queue,
        chg_code,
        ltrim(rtrim(before)) ,
        ltrim(rtrim(AFTER))
      INTO v_batch_no ,
        v_posting_dt,
        v_queue,
        v_chg_code,
        v_before,
        v_after
      FROM audit_trail
      WHERE drn                           = i.drn
      AND seq                             = v_max_seq
      AND NVL(ltrim(rtrim(before)),'xx') <> NVL(ltrim(rtrim(AFTER)),'xx')
      AND chg_code                        ='1';
      SELECT ltrim(rtrim(AFTER))
      INTO v_before
      FROM audit_trail
      WHERE drn                           = i.drn
      AND seq                             = v_min_seq
      AND chg_code                        ='114'
      AND NVL(ltrim(rtrim(before)),'xx') <> NVL(ltrim(rtrim(AFTER)),'xx');
      IF v_before                        <> v_after THEN
        INSERT
        INTO audit_errors_ak VALUES
          (
            v_batch_no,
            v_posting_dt,
            I.DRN,
            V_OP_NUM,
            v_queue,
            v_chg_code ,
            v_before,
            v_after ,
            v_max_seq
          );
        COMMIT;
      END IF;
    END IF;
  END LOOP;
  COMMIT;
END;



/