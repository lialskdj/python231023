#주민번호 체크.py

import re

def is_valid_korean_rrn(rrn):
    # Regular expression pattern for Korean RRN: 6 digits - (1 or 2) followed by 6 digits
    pattern = r'^\d{6}-(1|2)\d{6}$'
    
    if re.match(pattern, rrn):
        return True
    else:
        return False

# Sample Korean resident registration numbers
sample_rrns = ["920101-1234567", "010203-2123456", "880505-2323232", "040607-1122334", "751214-2000001",
               "990909-1111111", "060310-2222222", "000101-1111111", "123456-0000001", "770808-2222221"]

for rrn in sample_rrns:
    if is_valid_korean_rrn(rrn):
        print(f"Valid RRN: {rrn}")
    else:
        print(f"Invalid RRN: {rrn}")
