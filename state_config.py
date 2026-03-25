"""
State configuration for this MassachusettsDischargeWatch instance.

All state-specific values are centralized here. To deploy for a new state,
run: python deploy_new_state.py <STATE_CODE>

This file is overwritten by deploy_new_state.py — do not add logic here.
"""

STATE_CODE = "MA"
STATE_NAME = "Massachusetts"
APP_NAME = "MassachusettsDischargeWatch"
APP_TAGLINE = "Massachusetts Discharge Monitoring"
DOMAIN = "massachusettsdischargewatch.org"
DATA_FILE = "ma_exceedances_launch_ready.csv"
CONTACT_EMAIL = "data@massachusettsdischargewatch.org"
MAILING_ADDRESS = ""
TIMEZONE_LABEL = "EST"
EPA_REGION = 1
