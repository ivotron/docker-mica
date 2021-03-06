#!/usr/bin/env python
import pandas as pd

df = pd.read_csv('/data/output.csv')

df['itypes_mem_read_cnt']                   = df['itypes_mem_read_cnt'].astype(float)
df['itypes_mem_write_cnt']                  = df['itypes_mem_write_cnt'].astype(float)
df['itypes_control_cnt']                    = df['itypes_control_cnt'].astype(float)
df['itypes_arith_cnt']                      = df['itypes_arith_cnt'].astype(float)
df['itypes_fp_cnt']                         = df['itypes_fp_cnt'].astype(float)
df['itypes_stack_cnt']                      = df['itypes_stack_cnt'].astype(float)
df['itypes_shift_cnt']                      = df['itypes_shift_cnt'].astype(float)
df['itypes_string_cnt']                     = df['itypes_string_cnt'].astype(float)
df['itypes_sse_cnt']                        = df['itypes_sse_cnt'].astype(float)
df['itypes_system_cnt']                     = df['itypes_system_cnt'].astype(float)
df['itypes_nop_cnt']                        = df['itypes_nop_cnt'].astype(float)
df['itypes_other_cnt']                      = df['itypes_other_cnt'].astype(float)
df['ppm_GAg_mispred_cnt_4bits']             = df['ppm_GAg_mispred_cnt_4bits'].astype(float)
df['ppm_PAg_mispred_cnt_4bits']             = df['ppm_PAg_mispred_cnt_4bits'].astype(float)
df['ppm_GAs_mispred_cnt_4bits']             = df['ppm_GAs_mispred_cnt_4bits'].astype(float)
df['ppm_PAs_mispred_cnt_4bits']             = df['ppm_PAs_mispred_cnt_4bits'].astype(float)
df['ppm_GAg_mispred_cnt_8bits']             = df['ppm_GAg_mispred_cnt_8bits'].astype(float)
df['ppm_PAg_mispred_cnt_8bits']             = df['ppm_PAg_mispred_cnt_8bits'].astype(float)
df['ppm_GAs_mispred_cnt_8bits']             = df['ppm_GAs_mispred_cnt_8bits'].astype(float)
df['ppm_PAs_mispred_cnt_8bits']             = df['ppm_PAs_mispred_cnt_8bits'].astype(float)
df['ppm_GAg_mispred_cnt_12bits']            = df['ppm_GAg_mispred_cnt_12bits'].astype(float)
df['ppm_PAg_mispred_cnt_12bits']            = df['ppm_PAg_mispred_cnt_12bits'].astype(float)
df['ppm_GAs_mispred_cnt_12bits']            = df['ppm_GAs_mispred_cnt_12bits'].astype(float)
df['ppm_PAs_mispred_cnt_12bits']            = df['ppm_PAs_mispred_cnt_12bits'].astype(float)
df['reg_reg_age_cnt_1']                     = df['reg_reg_age_cnt_1'].astype(float)
df['reg_reg_age_cnt_2']                     = df['reg_reg_age_cnt_2'].astype(float)
df['reg_reg_age_cnt_4']                     = df['reg_reg_age_cnt_4'].astype(float)
df['reg_reg_age_cnt_8']                     = df['reg_reg_age_cnt_8'].astype(float)
df['reg_reg_age_cnt_16']                    = df['reg_reg_age_cnt_16'].astype(float)
df['reg_reg_age_cnt_32']                    = df['reg_reg_age_cnt_32'].astype(float)
df['reg_reg_age_cnt_64']                    = df['reg_reg_age_cnt_64'].astype(float)
df['stride_mem_read_local_stride_0']        = df['stride_mem_read_local_stride_0'].astype(float)
df['stride_mem_read_local_stride_8']        = df['stride_mem_read_local_stride_8'].astype(float)
df['stride_mem_read_local_stride_64']       = df['stride_mem_read_local_stride_64'].astype(float)
df['stride_mem_read_local_stride_512']      = df['stride_mem_read_local_stride_512'].astype(float)
df['stride_mem_read_local_stride_4096']     = df['stride_mem_read_local_stride_4096'].astype(float)
df['stride_mem_read_local_stride_32768']    = df['stride_mem_read_local_stride_32768'].astype(float)
df['stride_mem_read_local_stride_262144']   = df['stride_mem_read_local_stride_262144'].astype(float)
df['stride_mem_read_global_stride_0']       = df['stride_mem_read_global_stride_0'].astype(float)
df['stride_mem_read_global_stride_8']       = df['stride_mem_read_global_stride_8'].astype(float)
df['stride_mem_read_global_stride_64']      = df['stride_mem_read_global_stride_64'].astype(float)
df['stride_mem_read_global_stride_512']     = df['stride_mem_read_global_stride_512'].astype(float)
df['stride_mem_read_global_stride_4096']    = df['stride_mem_read_global_stride_4096'].astype(float)
df['stride_mem_read_global_stride_32768']   = df['stride_mem_read_global_stride_32768'].astype(float)
df['stride_mem_read_global_stride_262144']  = df['stride_mem_read_global_stride_262144'].astype(float)
df['stride_mem_write_local_stride_0']       = df['stride_mem_write_local_stride_0'].astype(float)
df['stride_mem_write_local_stride_8']       = df['stride_mem_write_local_stride_8'].astype(float)
df['stride_mem_write_local_stride_64']      = df['stride_mem_write_local_stride_64'].astype(float)
df['stride_mem_write_local_stride_512']     = df['stride_mem_write_local_stride_512'].astype(float)
df['stride_mem_write_local_stride_4096']    = df['stride_mem_write_local_stride_4096'].astype(float)
df['stride_mem_write_local_stride_32768']   = df['stride_mem_write_local_stride_32768'].astype(float)
df['stride_mem_write_local_stride_262144']  = df['stride_mem_write_local_stride_262144'].astype(float)
df['stride_mem_write_global_stride_0']      = df['stride_mem_write_global_stride_0'].astype(float)
df['stride_mem_write_global_stride_8']      = df['stride_mem_write_global_stride_8'].astype(float)
df['stride_mem_write_global_stride_64']     = df['stride_mem_write_global_stride_64'].astype(float)
df['stride_mem_write_global_stride_512']    = df['stride_mem_write_global_stride_512'].astype(float)
df['stride_mem_write_global_stride_4096']   = df['stride_mem_write_global_stride_4096'].astype(float)
df['stride_mem_write_global_stride_32768']  = df['stride_mem_write_global_stride_32768'].astype(float)
df['stride_mem_write_global_stride_262144'] = df['stride_mem_write_global_stride_262144'].astype(float)
df['memstackdist_acc_cnt_2^0-2^1']          = df['memstackdist_acc_cnt_2^0-2^1'].astype(float)
df['memstackdist_acc_cnt_2^1-2^2']          = df['memstackdist_acc_cnt_2^1-2^2'].astype(float)
df['memstackdist_acc_cnt_2^2-2^3']          = df['memstackdist_acc_cnt_2^2-2^3'].astype(float).astype(float)
df['memstackdist_acc_cnt_2^3-2^4']          = df['memstackdist_acc_cnt_2^3-2^4'].astype(float)
df['memstackdist_acc_cnt_2^4-2^5']          = df['memstackdist_acc_cnt_2^4-2^5'].astype(float)
df['memstackdist_acc_cnt_2^5-2^6']          = df['memstackdist_acc_cnt_2^5-2^6'].astype(float)
df['memstackdist_acc_cnt_2^6-2^7']          = df['memstackdist_acc_cnt_2^6-2^7'].astype(float)
df['memstackdist_acc_cnt_2^7-2^8']          = df['memstackdist_acc_cnt_2^7-2^8'].astype(float)
df['memstackdist_acc_cnt_2^8-2^9']          = df['memstackdist_acc_cnt_2^8-2^9'].astype(float)
df['memstackdist_acc_cnt_2^9-2^10']         = df['memstackdist_acc_cnt_2^9-2^10'].astype(float)
df['memstackdist_acc_cnt_2^10-2^11']        = df['memstackdist_acc_cnt_2^10-2^11'].astype(float)
df['memstackdist_acc_cnt_2^11-2^12']        = df['memstackdist_acc_cnt_2^11-2^12'].astype(float)
df['memstackdist_acc_cnt_2^12-2^13']        = df['memstackdist_acc_cnt_2^12-2^13'].astype(float)
df['memstackdist_acc_cnt_2^13-2^14']        = df['memstackdist_acc_cnt_2^13-2^14'].astype(float)
df['memstackdist_acc_cnt_2^14-2^15']        = df['memstackdist_acc_cnt_2^14-2^15'].astype(float)
df['memstackdist_acc_cnt_2^15-2^16']        = df['memstackdist_acc_cnt_2^15-2^16'].astype(float)
df['memstackdist_acc_cnt_2^16-2^17']        = df['memstackdist_acc_cnt_2^16-2^17'].astype(float)
df['memstackdist_acc_cnt_2^17-2^18']        = df['memstackdist_acc_cnt_2^17-2^18'].astype(float)
df['memstackdist_acc_cnt_over_2^18']        = df['memstackdist_acc_cnt_over_2^18'].astype(float)

df['itypes_mem_read_cnt_normalized']                   = df['itypes_mem_read_cnt'] / df['itypes_instruction_cnt']
df['itypes_mem_write_cnt_normalized']                  = df['itypes_mem_write_cnt'] / df['itypes_instruction_cnt']
df['itypes_control_cnt_normalized']                    = df['itypes_control_cnt'] / df['itypes_instruction_cnt']
df['itypes_arith_cnt_normalized']                      = df['itypes_arith_cnt'] / df['itypes_instruction_cnt']
df['itypes_fp_cnt_normalized']                         = df['itypes_fp_cnt'] / df['itypes_instruction_cnt']
df['itypes_stack_cnt_normalized']                      = df['itypes_stack_cnt'] / df['itypes_instruction_cnt']
df['itypes_shift_cnt_normalized']                      = df['itypes_shift_cnt'] / df['itypes_instruction_cnt']
df['itypes_string_cnt_normalized']                     = df['itypes_string_cnt'] / df['itypes_instruction_cnt']
df['itypes_sse_cnt_normalized']                        = df['itypes_sse_cnt'] / df['itypes_instruction_cnt']
df['itypes_system_cnt_normalized']                     = df['itypes_system_cnt'] / df['itypes_instruction_cnt']
df['itypes_nop_cnt_normalized']                        = df['itypes_nop_cnt'] / df['itypes_instruction_cnt']
df['itypes_other_cnt_normalized']                      = df['itypes_other_cnt'] / df['itypes_instruction_cnt']
df['ppm_GAg_mispred_cnt_4bits_normalized']             = df['ppm_GAg_mispred_cnt_4bits'] / df['ppm_instruction_cnt']
df['ppm_PAg_mispred_cnt_4bits_normalized']             = df['ppm_PAg_mispred_cnt_4bits'] / df['ppm_instruction_cnt']
df['ppm_GAs_mispred_cnt_4bits_normalized']             = df['ppm_GAs_mispred_cnt_4bits'] / df['ppm_instruction_cnt']
df['ppm_PAs_mispred_cnt_4bits_normalized']             = df['ppm_PAs_mispred_cnt_4bits'] / df['ppm_instruction_cnt']
df['ppm_GAg_mispred_cnt_8bits_normalized']             = df['ppm_GAg_mispred_cnt_8bits'] / df['ppm_instruction_cnt']
df['ppm_PAg_mispred_cnt_8bits_normalized']             = df['ppm_PAg_mispred_cnt_8bits'] / df['ppm_instruction_cnt']
df['ppm_GAs_mispred_cnt_8bits_normalized']             = df['ppm_GAs_mispred_cnt_8bits'] / df['ppm_instruction_cnt']
df['ppm_PAs_mispred_cnt_8bits_normalized']             = df['ppm_PAs_mispred_cnt_8bits'] / df['ppm_instruction_cnt']
df['ppm_GAg_mispred_cnt_12bits_normalized']            = df['ppm_GAg_mispred_cnt_12bits'] / df['ppm_instruction_cnt']
df['ppm_PAg_mispred_cnt_12bits_normalized']            = df['ppm_PAg_mispred_cnt_12bits'] / df['ppm_instruction_cnt']
df['ppm_GAs_mispred_cnt_12bits_normalized']            = df['ppm_GAs_mispred_cnt_12bits'] / df['ppm_instruction_cnt']
df['ppm_PAs_mispred_cnt_12bits_normalized']            = df['ppm_PAs_mispred_cnt_12bits'] / df['ppm_instruction_cnt']
df['reg_reg_age_cnt_1_normalized']                     = df['reg_reg_age_cnt_1'] / df['reg_total_reg_age']
df['reg_reg_age_cnt_2_normalized']                     = df['reg_reg_age_cnt_2'] / df['reg_total_reg_age']
df['reg_reg_age_cnt_4_normalized']                     = df['reg_reg_age_cnt_4'] / df['reg_total_reg_age']
df['reg_reg_age_cnt_8_normalized']                     = df['reg_reg_age_cnt_8'] / df['reg_total_reg_age']
df['reg_reg_age_cnt_16_normalized']                    = df['reg_reg_age_cnt_16'] / df['reg_total_reg_age']
df['reg_reg_age_cnt_32_normalized']                    = df['reg_reg_age_cnt_32'] / df['reg_total_reg_age']
df['reg_reg_age_cnt_64_normalized']                    = df['reg_reg_age_cnt_64'] / df['reg_total_reg_age']
df['stride_mem_read_local_stride_0_normalized']        = df['stride_mem_read_local_stride_0'] / df['stride_mem_read_cnt']
df['stride_mem_read_local_stride_8_normalized']        = df['stride_mem_read_local_stride_8'] / df['stride_mem_read_cnt']
df['stride_mem_read_local_stride_64_normalized']       = df['stride_mem_read_local_stride_64'] / df['stride_mem_read_cnt']
df['stride_mem_read_local_stride_512_normalized']      = df['stride_mem_read_local_stride_512'] / df['stride_mem_read_cnt']
df['stride_mem_read_local_stride_4096_normalized']     = df['stride_mem_read_local_stride_4096'] / df['stride_mem_read_cnt']
df['stride_mem_read_local_stride_32768_normalized']    = df['stride_mem_read_local_stride_32768'] / df['stride_mem_read_cnt']
df['stride_mem_read_local_stride_262144_normalized']   = df['stride_mem_read_local_stride_262144'] / df['stride_mem_read_cnt']
df['stride_mem_read_global_stride_0_normalized']       = df['stride_mem_read_global_stride_0'] / df['stride_mem_read_cnt']
df['stride_mem_read_global_stride_8_normalized']       = df['stride_mem_read_global_stride_8'] / df['stride_mem_read_cnt']
df['stride_mem_read_global_stride_64_normalized']      = df['stride_mem_read_global_stride_64'] / df['stride_mem_read_cnt']
df['stride_mem_read_global_stride_512_normalized']     = df['stride_mem_read_global_stride_512'] / df['stride_mem_read_cnt']
df['stride_mem_read_global_stride_4096_normalized']    = df['stride_mem_read_global_stride_4096'] / df['stride_mem_read_cnt']
df['stride_mem_read_global_stride_32768_normalized']   = df['stride_mem_read_global_stride_32768'] / df['stride_mem_read_cnt']
df['stride_mem_read_global_stride_262144_normalized']  = df['stride_mem_read_global_stride_262144'] / df['stride_mem_read_cnt']
df['stride_mem_write_local_stride_0_normalized']       = df['stride_mem_write_local_stride_0'] / df['stride_mem_write_cnt']
df['stride_mem_write_local_stride_8_normalized']       = df['stride_mem_write_local_stride_8'] / df['stride_mem_write_cnt']
df['stride_mem_write_local_stride_64_normalized']      = df['stride_mem_write_local_stride_64'] / df['stride_mem_write_cnt']
df['stride_mem_write_local_stride_512_normalized']     = df['stride_mem_write_local_stride_512'] / df['stride_mem_write_cnt']
df['stride_mem_write_local_stride_4096_normalized']    = df['stride_mem_write_local_stride_4096'] / df['stride_mem_write_cnt']
df['stride_mem_write_local_stride_32768_normalized']   = df['stride_mem_write_local_stride_32768'] / df['stride_mem_write_cnt']
df['stride_mem_write_local_stride_262144_normalized']  = df['stride_mem_write_local_stride_262144'] / df['stride_mem_write_cnt']
df['stride_mem_write_global_stride_0_normalized']      = df['stride_mem_write_global_stride_0'] / df['stride_mem_write_cnt']
df['stride_mem_write_global_stride_8_normalized']      = df['stride_mem_write_global_stride_8'] / df['stride_mem_write_cnt']
df['stride_mem_write_global_stride_64_normalized']     = df['stride_mem_write_global_stride_64'] / df['stride_mem_write_cnt']
df['stride_mem_write_global_stride_512_normalized']    = df['stride_mem_write_global_stride_512'] / df['stride_mem_write_cnt']
df['stride_mem_write_global_stride_4096_normalized']   = df['stride_mem_write_global_stride_4096'] / df['stride_mem_write_cnt']
df['stride_mem_write_global_stride_32768_normalized']  = df['stride_mem_write_global_stride_32768'] / df['stride_mem_write_cnt']
df['stride_mem_write_global_stride_262144_normalized'] = df['stride_mem_write_global_stride_262144'] / df['stride_mem_write_cnt']
df['memstackdist_acc_cnt_2^0-2^1_normalized']          = df['memstackdist_acc_cnt_2^0-2^1'] / df['memstackdist_mem_access_cnt']
df['memstackdist_acc_cnt_2^1-2^2_normalized']          = df['memstackdist_acc_cnt_2^1-2^2'] / df['memstackdist_mem_access_cnt']
df['memstackdist_acc_cnt_2^2-2^3_normalized']          = df['memstackdist_acc_cnt_2^2-2^3'] / df['memstackdist_mem_access_cnt']
df['memstackdist_acc_cnt_2^3-2^4_normalized']          = df['memstackdist_acc_cnt_2^3-2^4'] / df['memstackdist_mem_access_cnt']
df['memstackdist_acc_cnt_2^4-2^5_normalized']          = df['memstackdist_acc_cnt_2^4-2^5'] / df['memstackdist_mem_access_cnt']
df['memstackdist_acc_cnt_2^5-2^6_normalized']          = df['memstackdist_acc_cnt_2^5-2^6'] / df['memstackdist_mem_access_cnt']
df['memstackdist_acc_cnt_2^6-2^7_normalized']          = df['memstackdist_acc_cnt_2^6-2^7'] / df['memstackdist_mem_access_cnt']
df['memstackdist_acc_cnt_2^7-2^8_normalized']          = df['memstackdist_acc_cnt_2^7-2^8'] / df['memstackdist_mem_access_cnt']
df['memstackdist_acc_cnt_2^8-2^9_normalized']          = df['memstackdist_acc_cnt_2^8-2^9'] / df['memstackdist_mem_access_cnt']
df['memstackdist_acc_cnt_2^9-2^10_normalized']         = df['memstackdist_acc_cnt_2^9-2^10'] / df['memstackdist_mem_access_cnt']
df['memstackdist_acc_cnt_2^10-2^11_normalized']        = df['memstackdist_acc_cnt_2^10-2^11'] / df['memstackdist_mem_access_cnt']
df['memstackdist_acc_cnt_2^11-2^12_normalized']        = df['memstackdist_acc_cnt_2^11-2^12'] / df['memstackdist_mem_access_cnt']
df['memstackdist_acc_cnt_2^12-2^13_normalized']        = df['memstackdist_acc_cnt_2^12-2^13'] / df['memstackdist_mem_access_cnt']
df['memstackdist_acc_cnt_2^13-2^14_normalized']        = df['memstackdist_acc_cnt_2^13-2^14'] / df['memstackdist_mem_access_cnt']
df['memstackdist_acc_cnt_2^14-2^15_normalized']        = df['memstackdist_acc_cnt_2^14-2^15'] / df['memstackdist_mem_access_cnt']
df['memstackdist_acc_cnt_2^15-2^16_normalized']        = df['memstackdist_acc_cnt_2^15-2^16'] / df['memstackdist_mem_access_cnt']
df['memstackdist_acc_cnt_2^16-2^17_normalized']        = df['memstackdist_acc_cnt_2^16-2^17'] / df['memstackdist_mem_access_cnt']
df['memstackdist_acc_cnt_2^17-2^18_normalized']        = df['memstackdist_acc_cnt_2^17-2^18'] / df['memstackdist_mem_access_cnt']
df['memstackdist_acc_cnt_over_2^18_normalized']        = df['memstackdist_acc_cnt_over_2^18'] / df['memstackdist_mem_access_cnt']

# and rewrite the results, now including the normalized column
df.to_csv('/data/normalized_output.csv', index=False)
