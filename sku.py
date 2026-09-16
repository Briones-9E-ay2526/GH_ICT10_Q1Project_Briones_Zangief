from pyscript import document, display

def create_SKU(e):
    ctgy = document.getElementById ("categories") # categories
    ctgy_code = (ctgy.value)

    prd = document.getElementById("product") # products
    prd_code = (prd.value)

    quant = document.getElementById("qty") # quantities
    quant_code = (quant.value)

    sku = ctgy_code + "-" + prd_code + "-" + quant_code #for the sku maker

    display(f'{sku}', target="output")