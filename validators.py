def validate_order(order):
    errors=[]
    if not isinstance(order, dict):
        return ["Order must be an object"]
    if not order.get("patient_name"):
        errors.append("Patient name is empty")
    if not order.get("medicine"):
        errors.append("Medicine is empty")
    try:
        quantity = int(order.get("quantity",))
        if quantity <= 0:
            errors.append("Quantity must be positive")
    except (ValueError, TypeError):
        errors.append("Quantity must be a whole number")
        
    return errors