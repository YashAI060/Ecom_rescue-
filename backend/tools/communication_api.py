# communication_api.py
def send_apology_dm(handle, message):
    print(f"[TOOL] DM SENT to {handle}: {message}")
    return True

def flag_for_human(alert_id):
    print(f"[TOOL] ALERT {alert_id} FLAGGED for human intervention.")
    return True
