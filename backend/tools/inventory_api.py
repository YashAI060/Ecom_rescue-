# inventory_api.py
def pause_ads(sku):
    print(f"[TOOL] ADS PAUSED for {sku}")
    return True

def update_stock(sku, level):
    print(f"[TOOL] STOCK UPDATED for {sku} to {level}")
    return True
