#
#
#
import csv
import sys
start = int(sys.argv[1])
end = int(sys.argv[2])
end = end + 1

for tccg_number in range(start, end):
    #
    #
    #
    file_name = "output_"
    if tccg_number < 10:
        f = open(file_name + "0" + str(tccg_number) + ".txt")
    else:
        f = open(file_name + str(tccg_number) + ".txt")

    # use readline() to read the first line 
    line = f.readline()

    #
    #
    #
    int_ops     = 0
    float_time  = 0.0
    while line:
        #

        #
        #   "# of Operations"
        #
        if "of Operations" in line:
        #    print ("# of Operations >>> ", line)    
            tmp_line = line.split()
            int_ops = int(tmp_line[3])
 
        #
        #   "Kernel-Time"
        #
        # if "kernel" in line:
        #     tmp_line = line.split()
        #     float_time = float(tmp_line[1])

        #
        line = f.readline()
    #
    #
    #
    #
    file_namecsv = "output_"
    if tccg_number < 10:
        # fcsv = open(file_namecsv + "0" + str(tccg_number) + ".csv")
        fcsv = file_namecsv + "0" + str(tccg_number) + ".csv"
    else:
        fcsv = file_namecsv + str(tccg_number) + ".csv"
       
    grd = 0
    wgr = 0
    lsd = 0
    scr = 0
    vgrp = 0
    sgrp = 0
    fbar = 0
    feth_size = 0
    write_size = 0
    mem_write32B = 0
    tcc_ea_rdreq_32b_sum = 0
    tcc_ea_rdreq_sum = 0
    tcc_ea_wrreq_sum = 0
    tcc_ea_wrreq_64b_sum = 0
    vfetchinsts = 0
    ldsbankconflict = 0
    valuutilization = 0
    valubusy = 0
    salubusy = 0
    sq_waves = 0
    sq_lds_bankconflict = 0
    tcc_hit_sum = 0
    tcc_miss_sum =0
    
    sq_inst_salu = 0
    sq_inst_valu = 0
        
    with open(fcsv, mode='r') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        line_count = 0
        for row in csv_reader:
            if line_count == 0:
                # print(f'Metrics are {", ".join(row)}')
                line_count += 1
            # print(f'\t{row["name"]} works in the {row["department"]} department, and was born in {row["birthday month"]}.')
            grd = float(row["grd"])
            wgr = float(row["wgr"])
            lsd = float(row["lds"])
            scr = float(row["scr"])
            vgrp = float(row["vgpr"])
            sgrp = float(row["sgpr"])
            fbar = float(row["fbar"])
            feth_size = float(row["FETCH_SIZE"])
            write_size = float(row["WRITE_SIZE"])
            mem_write32B = float(row["MemWrites32B"])
            tcc_ea_rdreq_32b_sum = float(row["TCC_EA_RDREQ_32B_sum"])
            tcc_ea_rdreq_sum = float(row["TCC_EA_RDREQ_sum"])
            tcc_ea_wrreq_sum = float(row["TCC_EA_WRREQ_sum"])
            tcc_ea_wrreq_64b_sum = float(row["TCC_EA_WRREQ_64B_sum"])
            vfetchinsts = float(row["VFetchInsts"])
            ldsbankconflict = float(row["LDSBankConflict"])
            valuutilization = float(row["VALUUtilization"])
            valubusy = float(row["VALUBusy"])
            salubusy = float(row["SALUBusy"])
            sq_waves = float(row["SQ_WAVES"])
            sq_lds_bankconflict = float(row["SQ_LDS_BANK_CONFLICT"])
            tcc_hit_sum = float(row["TCC_HIT_sum"])
            tcc_miss_sum =float(row["TCC_MISS_sum"])
            sq_inst_salu = float(row["SQ_INSTS_SALU"])
            sq_inst_valu = float(row["SQ_INSTS_VALU"])
            float_time=float(row["DurationNs"])
            line_count += 1
        # print(f'Processed {line_count} lines.')
            
    
    if int_ops == 0 or float_time == 0.0:
        print ("[ERROR]")
    else:
        # print ("tccg-" + '{:2d}'.format(tccg_number) + " >> ops: ", int_ops, "\ttime(NS): ", "{0:.4f}".format(float_time), "\tGFLOPS: ", "{0:.4f}".format(int_ops / (float_time )))
        print ( '{:2d}'.format(tccg_number) , int_ops, "{0:.4f}".format(float_time), "{0:.4f}".format(int_ops / (float_time )), 
               "{0:.4f}".format(grd) , "{0:.4f}".format(wgr), "{0:.4f}".format(lsd), "{0:.4f}".format(scr) , "{0:.4f}".format(vgrp) ,
               "{0:.4f}".format(sgrp) , "{0:.4f}".format(fbar) , "{0:.4f}".format(feth_size) , "{0:.4f}".format(write_size) ,
               "{0:.4f}".format(mem_write32B) ,   "{0:.4f}".format(tcc_ea_rdreq_32b_sum) ,  "{0:.4f}".format(tcc_ea_rdreq_sum) ,
               "{0:.4f}".format(tcc_ea_wrreq_sum) , "{0:.4f}".format(tcc_ea_wrreq_64b_sum) , "{0:.4f}".format(vfetchinsts) ,
               "{0:.4f}".format(ldsbankconflict) , "{0:.4f}".format(valuutilization) , "{0:.4f}".format(valubusy) ,
               "{0:.4f}".format(salubusy) , "{0:.4f}".format(sq_waves) , "{0:.4f}".format(sq_lds_bankconflict) ,
               "{0:.4f}".format(tcc_hit_sum)  , "{0:.4f}".format(tcc_miss_sum) , "{0:.4f}".format(sq_inst_salu) , "{0:.4f}".format(sq_inst_valu)
               )
    
    f.close()

