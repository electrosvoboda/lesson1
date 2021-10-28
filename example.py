def get_vat(payment, percent=18):
    try:
        payment = float(payment)
        percent = int(percent)
        vat = payment / 100 * 18
        vat = round(vat, 2)
        return "Summa NDS: {}. Percent = {}".format(vat, percent)
    except (TypeError, ValueError):
        print("Failure type data")


result = get_vat(58, 12)
print(result)