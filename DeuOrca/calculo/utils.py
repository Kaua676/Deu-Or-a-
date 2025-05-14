def calcular_total(subtotal, desconto=0, imposto=0):
    total = float(subtotal) - float(desconto)
    total += total * (float(imposto) / 100)
    return round(total, 2)
