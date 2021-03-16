import os
import math
import sqlite3
import numpy as np
import pandas as pd
from datetime import datetime

# 최종수정일자 : 2021.03.16

########################### KAKD0008LM ###########################
# DESCRIPTION:
#   보종단위별 위험액 산출
# SOURCE:
#   KICS_CORR_PREM_RSV_NL
#   KICS_PRM_RSV_EXPO
#   KICS_RISK_COEF_NL
#   KICS_BOZ_GRP_MAP_NL
# TARGET: 
#   KICS_BOZ_CD_RISK_NL
##################################################################

