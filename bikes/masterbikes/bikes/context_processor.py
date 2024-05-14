def total_carrito(request):
    total = 0
    if request.user.is_authenticated:
        if "carrito" in request.session:
            for key, value in request.session["carrito"].items():
                if "acumulado" in value:
                    total += int(value["acumulado"])
    return {"total_carrito": total}

def cantidad_producto(request):
    total = 0
    if request.user.is_authenticated:
        if "carrito" in request.session:
            for key, value in request.session["carrito"].items():
                if len(value) > 1:
                    total += int(value[1])
    return {"cantidad_producto": total}


