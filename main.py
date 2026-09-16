from pyscript import document, display # importing document and display package


def create_order(e): #creating order
    document.getElementById("output1").innerHTML = " "

    #we get the input
    prod1 = document.getElementById("burger1")
    prod2 = document.getElementById("burger2")
    prod3 = document.getElementById("burger3")
    prod4 = document.getElementById("burger4")
    prod5 = document.getElementById("burger5")


    #we get the prices
    prices1 = float(prod1.value) * prod1.checked
    prices2 = float(prod2.value) * prod2.checked
    prices3 = float(prod3.value) * prod3.checked
    prices4 = float(prod4.value) * prod4.checked
    prices5 = float(prod5.value) * prod5.checked


    #detecting the size
    size = document.querySelector('input[name="size"]:checked')
    size_price = float(size.value)


    #calculation
    subtotal = prices1 + prices2 + prices3 + prices4 + prices5 + size_price # < sir it turns out that I forgot the size_price in the subtotal, my fault po
    vat = subtotal * 0.12
    total = subtotal + vat


    display(f'-----', target="output")
    display(f'Subtotal: PHP {subtotal}', target="output")
    display(f'VAT: PHP {vat}', target="output")
    display(f'Total: PHP {total}', target="output")