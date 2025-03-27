# 3つのテストを書く
import math

def calc_tax(price ,tax_rate):
    # 税金
    sales_tax = tax_rate * price
    #小数点以下の切り捨て math.floor
    return price + math.floor(sales_tax)

