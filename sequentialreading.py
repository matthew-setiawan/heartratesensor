import max30102
import hrcalc

m = max30102.MAX30102()

# 100 samples are read and used for HR/SpO2 calculation in a single loop
while True:
    red, ir = m.read_seq()
    print(red,ir)