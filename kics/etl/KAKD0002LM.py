import os
import math
import sqlite3
import numpy as np
import pandas as pd
from datetime import datetime

# 최종수정일자 : 2021.03.16

########################### KAKD0002LM ###########################
# DESCRIPTION:
#   국가그룹별 요구자본 산출
# SOURCE:
#   KICS_BOZ_CD_RISK_NL -> KICS_BOZ_GRP_RISK_NL
#   KICS_CORR_BOZ_NL -> KICS_CORR_BOZ_INR_NL
# TARGET: 
#   KICS_CNTR_RISK_NL
##################################################################

