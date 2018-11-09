import xml.etree.ElementTree as ET
import pandas as pd
import smtplib
import numpy as np
# load and parse the file

df_session = pd.DataFrame(columns=['oper_id'])#, 'comp_typ', 'station_name','app','wrk_grp','stat_cat','st_dt','end_dt','action_time','lost_action_time','work_ready_time','wait_for_work_time','sys_ohs','idle_time'])
df_comp_type = pd.DataFrame(columns=['comp_typ'])
path = 'c:\Repo\\DataExtract_StatsExport_20180816_111233.xml'
xmlTree = ET.parse(path)

elemList = []
opid = ''
comptyp = ''

root = xmlTree.getroot()

sep = ","




for each in root.findall('.//session'):

    operlogin = each.find('.//operatorLogin')

    if operlogin is not None:
        print('')
        #print(operlogin.text)

    component_type = each.find('.//componentType')
    if component_type is not None:
        print('')
       # print(component_type.text, '~~~~~')

    station_name = each.find('.//stationName')
    if station_name is not None:
        print('')
        #print(station_name.text, '~~~~~')

    v_application = each.find('.//application')
    if v_application is not None:
        #print(v_application.text, '~~~~~')
        print('')

    v_workgroup = each.find('.//workgroup')
    if v_workgroup is not None:
        # print(v_application.text, '~~~~~')
        print('')

    v_statsCategory = each.find('.//statsCategory')
    if v_statsCategory is not None:
        # print(v_application.text, '~~~~~')
        print('')
    else:
        v_statsCategory = "XXXXX"
    #if v_statsCategory is None:


    v_start = each.find('.//start')
    if v_start is not None:
        # print(v_application.text, '~~~~~')
        print('')

    v_end = each.find('.//end')
    if v_end is not None:
        # print(v_application.text, '~~~~~')
        print('')

    v_actionTime = each.find('.//actionTime')
    if v_actionTime is not None:
        # print(v_application.text, '~~~~~')
        print('')

    v_lostActionTime = each.find('.//lostActionTime')
    if v_lostActionTime is not None:
        # print(v_application.text, '~~~~~')
        print('')

    v_workReadyTime = each.find('.//workReadyTime')
    if v_workReadyTime is not None:
        # print(v_application.text, '~~~~~')
        print('')

    v_waitForWorkTime = each.find('.//waitForWorkTime')
    if v_waitForWorkTime is not None:
        # print(v_application.text, '~~~~~')
        print('')

    v_systemOverhead = each.find('.//systemOverhead')
    if v_systemOverhead is not None:
        # print(v_application.text, '~~~~~')
        print('')

    v_idleTime = each.find('.//idleTime')
    if v_idleTime is not None:
        # print(v_application.text, '~~~~~')
        print('')

    #print(operlogin.text ,component_type.text, station_name.text, v_application.text, v_workgroup.text, v_statsCategory.text, v_start.text, v_end.text, v_actionTime.text, v_lostActionTime.text, v_workReadyTime.text, v_waitForWorkTime.text, v_systemOverhead.text, v_idleTime.text )
    #print('' if rating is None else rating.text)
    #df_session.insert(1,'oper_id',rating,True)
    #df_session.append('oper_id',rating.text )
    #df_session = df_session.append({'oper_id': operlogin.text}, ignore_index=True)

    #print(elemList)


    with open('c:\\repo\\newtrial.txt', 'a') as f:
        print(operlogin.text.rstrip() ,sep,component_type.text.rstrip() ,sep, station_name.text.rstrip(),sep, v_application.text.rstrip(), sep,v_workgroup.text.rstrip(),sep, v_statsCategory.text,sep, v_start.text, sep, v_end.text, sep, v_actionTime.text,sep,v_lostActionTime.text,sep, v_workReadyTime.text,sep, v_waitForWorkTime.text,sep, v_systemOverhead.text,sep,v_idleTime.text,file=f)



''' 
for each in root.findall('.//suspendSession'):
    suspend_operid = each.find('.//operatorLogin')
    #print('' if rating is None else rating.text)
    if suspend_operid is not None:
        print('')
        #print(suspend_operid.text)

    suspend_comp_type = each.find('.//componentType')
    # print('' if rating is None else rating.text)
    if suspend_comp_type is not None:
        print('')

    suspend_stationName = each.find('.//stationName')
    # print('' if rating is None else rating.text)
    if suspend_stationName is not None:
        print('')

    suspend_application = each.find('.//application')
    # print('' if rating is None else rating.text)
    if suspend_application is not None:
        print('')

    suspend_workgroup = each.find('.//workgroup')
    # print('' if rating is None else rating.text)
    if suspend_workgroup is not None:
        print('')

    suspend_statsCategory = each.find('.//statsCategory')
    # print('' if rating is None else rating.text)
    if suspend_statsCategory is not None:
        print('')

    suspend_suspendKey = each.find('.//suspendKey')
    # print('' if rating is None else rating.text)
    if suspend_suspendKey is not None:
        print('')
    suspend_suspendCode = each.find('.//suspendCode')

    suspend_suspend_dt = each.find('.//suspendDate')

    suspend_resume_dt = each.find('.//resumeDate')
    suspend_sus_duration = each.find('.//suspendDuration')
    suspend_is_included = each.find('.//isIncludedInActionTime')

    print(suspend_operid.text, suspend_comp_type.text, suspend_stationName.text, suspend_application.text, suspend_workgroup.text, suspend_statsCategory.text , suspend_suspendKey.text, suspend_suspendCode.text, suspend_suspend_dt.text,suspend_resume_dt.text, suspend_sus_duration.text, suspend_is_included.text)
 
for each in root.findall('.//distribution'):
     v_distribution_num = each.find('.//distributionNum')
     distribution_Name = each.find('.//distributionName')
     record_id = each.find('.//recordID')
     distribution_class = each.find('.//distributionClass')
     print(v_distribution_num.text, distribution_Name.text,record_id.text, distribution_class.text )
     


#print("ABOUT TO HIT DRA")
for each in root.findall('.//DRA'):
    #print("something is about to happen")
    DRA_OPERid = each.find('.//operatorLogin')
    DRA_comp_type = each.find('.//componentType')



    DRA_station = each.find('.//stationName')

    DRA_application = each.find('.//application')

    DRA_workgroup = each.find('.//workgroup')

    DRA_stat_cat = each.find('.//statsCategory')

    DRA_deposits_rvw = each.find('.//depositsReviewed')

    DRA_deposits_re_rvw = each.find('.//depositsReReviewd')

    DRA_deposits_total = each.find('.//depositsTotal')
    DRA_deposits_nohold = each.find('.//depositsNoHold')
    DRA_depwithnochanges = each.find('.//depositsWithNonnegchanges')
    DRA_depoholdrevwd = each.find('.//depoHoldReviewed')
    DRA_depNNGRvwd = each.find('.//depNNGReviewed')
    DRA_holdapplied = each.find('.//holdsApplied')
    DRA_holdsremoved = each.find('.//holdsRemoved')
    DRA_items_nonneg = each.find('.//itemsNonneg')
    DRA_total_rtnr_dep = each.find('.//totalReturnDeposits')
    DRA_total_sent_deposits = each.find('.//totalSentDeposits')
    DRA_total_timeout_dep = each.find('.//totalTimeoutDeposits')



    print(DRA_OPERid.text, DRA_comp_type.text, DRA_station.text, DRA_application.text, DRA_workgroup.text,DRA_stat_cat.text,DRA_deposits_rvw.text,DRA_deposits_re_rvw.text,DRA_deposits_total.text,DRA_deposits_nohold.text,DRA_depwithnochanges.text,DRA_depoholdrevwd.text,DRA_depNNGRvwd.text,DRA_holdapplied.text, DRA_holdsremoved.text, DRA_items_nonneg.text,DRA_total_rtnr_dep.text, DRA_total_sent_deposits.text,DRA_total_timeout_dep.text)


for each in root.findall('.//CLC'):
    CLC_oper_id = each.find('.//operatorLogin')
    #print('' if rating is None else rating.text)
    CLC_comp_type = each.find('.//componentType')
    CLC_station_name = each.find('.//stationName')
    CLC_application = each.find('.//application')
    CLC_workgrp = each.find('.//workgroup')
    CLC_stat_cat = each.find('.//statsCategory')
    CLC_item_processed = each.find('.//itemsProcessed')
    CLC_key_stroke = each.find('.//keyStrokeCredit')
    CLC_actualkeystrokes = each.find('.//actualKeystrokes')
    CLC_items_rekeyed = each.find('.//itemsRekeyed')
    CLC_amtlength_suspects = each.find('.//amountLengthSuspects')
    CLC_errorbyamt = each.find('.//errorByAmountLength')

    print(CLC_oper_id.text, CLC_comp_type.text,CLC_station_name.text,CLC_application.text, CLC_workgrp.text, CLC_stat_cat.text, CLC_item_processed.text, CLC_key_stroke.text,CLC_actualkeystrokes.text,
          CLC_items_rekeyed.text,CLC_amtlength_suspects.text,CLC_errorbyamt.text)



for each in root.findall('.//AK'):
    AK_oper_id = each.find('.//operatorLogin')
    AK_comp_Type = each.find('.//componentType')
    AK_station_name = each.find('.//stationName')
    AK_application = each.find('.//application')
    AK_wrkgrp = each.find('.//workgroup')
    AK_stat_cat = each.find('.//statsCategory')
    AK_item_processed = each.find('.//itemsProcessed')
    AK_keystroke_crd = each.find('.//keyStrokeCredit')
    AK_actual_key = each.find('.//actualKeystrokes')

    print(AK_oper_id.text,AK_comp_Type.text,AK_station_name.text,AK_application.text, AK_wrkgrp.text, AK_stat_cat.text, AK_item_processed.text, AK_keystroke_crd.text,AK_actual_key.text)








for each in root.findall('.//BAL'):
    BAL_oper_id = each.find('.//operatorLogin')
    BAL_comp_type = each.find('.//componentType')
    BAL_statn_nm = each.find('.//stationName')
    BAL_application = each.find('.//application')
    BAL_wrk_grp = each.find('.//workgroup')
    BAL_stat_cat = each.find('.//statsCategory')
    BAL_item_processed = each.find('.//itemsProcessed')
    BAL_keystroke_credit = each.find('.//keyStrokeCredit')
    BAL_actual_keystrokes = each.find('.//actualKeystrokes')
    BAL_images_classified = each.find('.//imagesReclassified')
    BAL_images_rejected = each.find('.//imagesRejected')
    BAL_batches = each.find('.//batches')
    BAL_adjustments = each.find('.//adjustments')
    BAL_suspense = each.find('.//suspensed')
    BAL_unsuspensed = each.find('.//unsuspensed')
    BAL_reimaged = each.find('.//reimaged')
    BAL_front_pig = each.find('.//frontPiggyback')
    BAL_rear_pig = each.find('.//rearPiggyback')
    BAL_corrected  = each.find('.//corrected')
    BAL_moved = each.find('.//moved')
    BAL_credit_items = each.find('.//creditItems')
    BAL_debit_items = each.find('.//debitItems')
    BAL_batches_completed = each.find('.//batchesCompleted')

    BAL_batches_sent = each.find('.//batchesSent')
    BAL_batches_return = each.find('.//batchesReturn')
    BAL_blocks_split = each.find('.//blocksSplit')
    BAL_batches_split = each.find('.//batchesSplit')
    BAL_batches_moved = each.find('.//batchesMoved')
    BAL_items_complted_Batch = each.find('.//itemsInCompleteBatches')
    BAL_itemsInSent_batches = each.find('.//itemsInSentBatches')
    BAL_items_returned_inbatches = each.find('.//itemsInReturnedBatches')
    BAL_items_recalc = each.find('.//itemsReclassifiedAsNonproof')
    BAL_tape = each.find('.//tapeSubDocs')
    BAL_suspect = each.find('.//suspectsFound')
    BAL_suspects_were_changed = each.find('.//suspectsWereChanged')
    BAL_suspectsWereMisencodes = each.find('.//suspectsWereMisencodes')
    BAL_suspects_weremisreads = each.find('.//suspectsWereMisreads')
    BAL_suspectsWereKeyErrors = each.find('.//suspectsWereKeyErrors')
    BAL_annotations = each.find('.//annotations')
    print(BAL_oper_id.text, BAL_comp_type.text, BAL_statn_nm.text, BAL_application.text, BAL_wrk_grp.text,
          BAL_stat_cat.text, BAL_item_processed.text, BAL_keystroke_credit.text,BAL_actual_keystrokes.text, BAL_images_classified.text,
          BAL_images_rejected.text,BAL_batches.text, BAL_adjustments.text, BAL_suspense.text, BAL_unsuspensed.text, BAL_reimaged.text,
          BAL_front_pig.text, BAL_rear_pig.text,BAL_corrected.text, BAL_moved.text, BAL_credit_items.text, BAL_debit_items.text, BAL_batches_completed.text,
          BAL_batches_sent.text, BAL_batches_return.text ,BAL_blocks_split.text , BAL_batches_split.text, BAL_batches_moved.text, BAL_items_complted_Batch.text, BAL_itemsInSent_batches.text,
          BAL_items_returned_inbatches.text,BAL_items_recalc.text,BAL_tape.text,BAL_suspect.text, BAL_suspects_were_changed.text,  BAL_suspectsWereMisencodes.text,
          BAL_suspects_weremisreads.text, BAL_suspectsWereKeyErrors.text, BAL_annotations.text  )

'''


































