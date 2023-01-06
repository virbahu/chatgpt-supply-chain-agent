import numpy as np
def calculate_sc_decision(context, inventory_level, demand_forecast, lead_time, service_target=0.95):
    from scipy.stats import norm
    z = norm.ppf(service_target)
    demand_std = demand_forecast * 0.2
    safety_stock = round(z * demand_std * (lead_time**0.5))
    reorder_point = round(demand_forecast * lead_time + safety_stock)
    action = "order" if inventory_level <= reorder_point else "hold"
    order_qty = max(0, round(demand_forecast * lead_time * 2 - inventory_level)) if action == "order" else 0
    return {"action": action, "order_qty": order_qty, "safety_stock": safety_stock, "reorder_point": reorder_point, "context": context}
if __name__=="__main__":
    from scipy.stats import norm
    print(calculate_sc_decision("low_inventory_alert", 150, 50, 7))
