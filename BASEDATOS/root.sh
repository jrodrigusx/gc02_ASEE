#!/bin/sh
unset WAS_ROOTMACRO_CALL_MADE
. /scratch/app/user/product/21.0.0/dbhome_1/install/utl/rootmacro.sh "$@"
. /scratch/app/user/product/21.0.0/dbhome_1/install/utl/rootinstall.sh

#The following script is added by:oracle.rdbms.scheduler:21.0.0.0.0
/scratch/app/user/product/21.0.0/dbhome_1/install/root_schagent.sh

#The above script is added by:oracle.rdbms.scheduler:21.0.0.0.0

#
# Root Actions related to network
#
/scratch/app/user/product/21.0.0/dbhome_1/network/install/sqlnet/setowner.sh 

#
# Invoke standalone rootadd_rdbms.sh
#
/scratch/app/user/product/21.0.0/dbhome_1/rdbms/install/rootadd_rdbms.sh

/scratch/app/user/product/21.0.0/dbhome_1/rdbms/install/rootadd_filemap.sh 
