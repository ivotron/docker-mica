#!/bin/bash

usage() {
  echo "Usage: $0 [options]"
  echo ""
  echo "Available options:"
  echo ""
  echo "  -n <name>        name to associate to the output."
  echo "  -i <image>       image name (as passed to docker run)."
  echo "  -f <run-flags>   flags passed to docker run (e.g. --rm, --net, etc.)."
  echo "  -c <command>     command to profile."
  echo "  -p <pre-command> commands to execute prior to the execution prior to"
  echo "                   the one given in -c. This command is *not* profiled."
  echo "  -r               whether to recompile MICA. When passed, gcc, g++,"
  echo "                   make should be available inside the container."
  exit 1
}

recompile=false

while getopts "f:i:n:c:p:w:r" o; do
  case "${o}" in
    i)
      image=${OPTARG}
      ;;
    n)
      name=${OPTARG}
      ;;
    f)
      flags=${OPTARG}
      ;;
    c)
      cmd=${OPTARG}
      ;;
    p)
      pre=${OPTARG}
      ;;
    r)
      recompile=true
      ;;
    *)
      usage
      ;;
  esac
done
shift $((OPTIND-1))

if [ -z "$image" ] ; then
  echo "Expecting image name in -i"
  exit 1
fi
if [ -z "$cmd" ] ; then
  echo "Expecting command with -c"
  exit 1
fi

# TODO check versions for all dependencies

docker info &> /dev/null
if [ $? -ne 0 ] ; then
  echo "Unable to invoke docker"
  exit 1
fi

jq --version &> /dev/null
if [ $? -ne 0 ] ; then
  echo "Unable to invoke jq"
  exit 1
fi

# attempt to install mica if it doesn't exist
if [ ! -d `pwd`/pin/source/tools/mica ] ; then
  echo "Unable to find mica folder. Will attempt to install it now."

  mkdir -p `pwd`/pin/source/tools/mica

  docker run --rm -v `pwd`:/mnt ivotron/mica

  if [ ! -d `pwd`/pin/source/tools/mica ] ; then
    echo "Unable to install mica."
    exit 1
  fi

  cp pin/source/tools/mica/mica.conf.example pin/source/tools/mica/mica.conf
  sed -i -e 's/ilp_one/all/' pin/source/tools/mica/mica.conf
  sed -i -e 's/itypes_spec_file.*/itypes_spec_file: \/pin\/source\/tools\/mica\/itypes_default.spec/' pin/source/tools/mica/mica.conf
fi

# pull image explicitly
docker pull $image &> /dev/null

# check for dependencies inside container
if [ "$recompile" = true ] ; then
  for p in gcc g++ make ; do
    docker run --rm --entrypoint=/bin/bash $image -c "$p -v" &> /dev/null
    if [ $? -ne 0 ] ; then
      echo "Unable to find $p in given container"
      exit 1
    fi
  done
fi

docker kill $name &> /dev/null
docker rm $name &> /dev/null

if [ ! -f output.csv ] ; then
  csvheader="container,process,"
  csvheader+="instruction_cnt,"
  csvheader+="ilp_cycle_count_win_size_32,"
  csvheader+="ilp_cycle_count_win_size_64,"
  csvheader+="ilp_cycle_count_win_size_128,"
  csvheader+="ilp_cycle_count_win_size_256,"
  csvheader+="itypes_instruction_cnt,"
  csvheader+="itypes_mem_read_cnt,"
  csvheader+="itypes_mem_write_cnt,"
  csvheader+="itypes_control_cnt,"
  csvheader+="itypes_arith_cnt,"
  csvheader+="itypes_fp_cnt,"
  csvheader+="itypes_stack_cnt,"
  csvheader+="itypes_shift_cnt,"
  csvheader+="itypes_string_cnt,"
  csvheader+="itypes_sse_cnt,"
  csvheader+="itypes_system_cnt,"
  csvheader+="itypes_nop_cnt,"
  csvheader+="itypes_other_cnt,"
  csvheader+="ppm_instruction_cnt,"
  csvheader+="ppm_GAg_mispred_cnt_4bits,"
  csvheader+="ppm_PAg_mispred_cnt_4bits,"
  csvheader+="ppm_GAs_mispred_cnt_4bits,"
  csvheader+="ppm_PAs_mispred_cnt_4bits,"
  csvheader+="ppm_GAg_mispred_cnt_8bits,"
  csvheader+="ppm_PAg_mispred_cnt_8bits,"
  csvheader+="ppm_GAs_mispred_cnt_8bits,"
  csvheader+="ppm_PAs_mispred_cnt_8bits,"
  csvheader+="ppm_GAg_mispred_cnt_12bits,"
  csvheader+="ppm_PAg_mispred_cnt_12bits,"
  csvheader+="ppm_GAs_mispred_cnt_12bits,"
  csvheader+="ppm_PAs_mispred_cnt_12bits,"
  csvheader+="reg_total_reg_use_cnt,"
  csvheader+="reg_total_reg_age,"
  csvheader+="reg_reg_age_cnt_1,"
  csvheader+="reg_reg_age_cnt_2,"
  csvheader+="reg_reg_age_cnt_4,"
  csvheader+="reg_reg_age_cnt_8,"
  csvheader+="reg_reg_age_cnt_16,"
  csvheader+="reg_reg_age_cnt_32,"
  csvheader+="reg_reg_age_cnt_64,"
  csvheader+="stride_mem_read_cnt,"
  csvheader+="stride_mem_read_local_stride_0,"
  csvheader+="stride_mem_read_local_stride_8,"
  csvheader+="stride_mem_read_local_stride_64,"
  csvheader+="stride_mem_read_local_stride_512,"
  csvheader+="stride_mem_read_local_stride_4096,"
  csvheader+="stride_mem_read_local_stride_32768,"
  csvheader+="stride_mem_read_local_stride_262144,"
  csvheader+="stride_mem_read_global_stride_0,"
  csvheader+="stride_mem_read_global_stride_8,"
  csvheader+="stride_mem_read_global_stride_64,"
  csvheader+="stride_mem_read_global_stride_512,"
  csvheader+="stride_mem_read_global_stride_4096,"
  csvheader+="stride_mem_read_global_stride_32768,"
  csvheader+="stride_mem_read_global_stride_262144,"
  csvheader+="stride_mem_write_cnt,"
  csvheader+="stride_mem_write_local_stride_0,"
  csvheader+="stride_mem_write_local_stride_8,"
  csvheader+="stride_mem_write_local_stride_64,"
  csvheader+="stride_mem_write_local_stride_512,"
  csvheader+="stride_mem_write_local_stride_4096,"
  csvheader+="stride_mem_write_local_stride_32768,"
  csvheader+="stride_mem_write_local_stride_262144,"
  csvheader+="stride_mem_write_global_stride_0,"
  csvheader+="stride_mem_write_global_stride_8,"
  csvheader+="stride_mem_write_global_stride_64,"
  csvheader+="stride_mem_write_global_stride_512,"
  csvheader+="stride_mem_write_global_stride_4096,"
  csvheader+="stride_mem_write_global_stride_32768,"
  csvheader+="stride_mem_write_global_stride_262144,"
  csvheader+="memfootprint_num_64-byte_blocks_data,"
  csvheader+="memfootprint_num_4KB_pages_data,"
  csvheader+="memfootprint_num_64-byte_blocks_instr,"
  csvheader+="memfootprint_num_4KB_pages_instr,"
  csvheader+="memstackdist_mem_access_cnt,"
  csvheader+="memstackdist_cold_ref_cnt,"
  csvheader+="memstackdist_acc_cnt_2^0-2^1,"
  csvheader+="memstackdist_acc_cnt_2^1-2^2,"
  csvheader+="memstackdist_acc_cnt_2^2-2^3,"
  csvheader+="memstackdist_acc_cnt_2^3-2^4,"
  csvheader+="memstackdist_acc_cnt_2^4-2^5,"
  csvheader+="memstackdist_acc_cnt_2^5-2^6,"
  csvheader+="memstackdist_acc_cnt_2^6-2^7,"
  csvheader+="memstackdist_acc_cnt_2^7-2^8,"
  csvheader+="memstackdist_acc_cnt_2^8-2^9,"
  csvheader+="memstackdist_acc_cnt_2^9-2^10,"
  csvheader+="memstackdist_acc_cnt_2^10-2^11,"
  csvheader+="memstackdist_acc_cnt_2^11-2^12,"
  csvheader+="memstackdist_acc_cnt_2^12-2^13,"
  csvheader+="memstackdist_acc_cnt_2^13-2^14,"
  csvheader+="memstackdist_acc_cnt_2^14-2^15,"
  csvheader+="memstackdist_acc_cnt_2^15-2^16,"
  csvheader+="memstackdist_acc_cnt_2^16-2^17,"
  csvheader+="memstackdist_acc_cnt_2^17-2^18,"
  csvheader+="memstackdist_acc_cnt_over_2^18"
  echo $csvheader > output.csv
fi

echo "profiling $name"

docker run --rm \
  -v `pwd`/entrypoint_for_profiling.sh:/root/entrypoint_for_profiling.sh \
  -v `pwd`/pin:/pin \
  -e PRE="$pre" \
  -e CMD="$cmd" \
  -e RECOMPILE=$recompile \
  --privileged \
  --entrypoint=/root/entrypoint_for_profiling.sh \
  $flags $image &> /tmp/error

if [ $? -ne 0 ] ; then
  printf "${name}," >> output.csv
  printf "0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0," >> output.csv
  printf "0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0," >> output.csv
  printf "0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0," >> output.csv
  printf "0,0,0,0,0,0" >> output.csv
  echo "-------------------------------" >> error.log
  echo "Error while executing $name" >> error.log
  echo "-------------------------------" >> error.log
  cat /tmp/error >> error.log
  echo "-------------------------------" >> error.log
  echo "Error while executing $name"
  exit 0
fi

# get number of processes (by getting the num of files that got generated)
num_procs=`ls pin/source/tools/mica/ilp_full_int_*.out | wc -l`

for p in `seq 1 $((num_procs-1))` ; do

  # we start the sequence at 1 instead of 0, since the
  # the first set of '*.out' files corresponds to the invocation
  # of the shell in entrypoint_for_profiling.sh, i.e. p=0 is the 'sh -c'
  # part of the arguments to pintool

  printf "${name},${p}," >> output.csv

  for atype in ilp itypes ppm reg stride memfootprint memreusedist ; do
    files=(`ls pin/source/tools/mica/${atype}_full_int_*.out`)
    file="${files[$((p))]}"

    line=$(head -n 1 $file)
    line=`echo $line | sed 's/ /,/g'`

    printf "$line" >> output.csv
  done
  printf "\n" >> output.csv
done
