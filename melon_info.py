"""Print out all the melons in our inventory."""


#from melons import melon_names, melon_prices, melon_seedlessness, melon_average_weight, melon_flesh_color, melon_rind_color

# CASABA
# price: 2.5
# seedless: False
# flesh_color: None
# rind_color: None
# average_weight: None

from melons import melons_dict


def print_melon(name):
    """Print each melon with corresponding attribute information."""

    # price = melon[name][1]
    # seedless = melons_dict[name][2]
    # flesh_color = melon[name][3]
    # rind_color = melon[name][4]
    # average_weight = melon[name][5]

    print(melons_dict[name]["price"])

    price = melons_dict[name]["price"]
    seedless = melons_dict[name]["seedless"]
    flesh_color = melons_dict[name]["flesh_color"]
    rind_color = melons_dict[name]["rind_color"]
    average_weight = melons_dict[name]["average_weight"]

    print(name.upper())
    print(f"price: {price}")
    print(f"seedless: {seedless}")
    print(f"flesh_color: {flesh_color}")
    print(f"rind_color: {rind_color}")
    print(f"average_weight: {average_weight}")


for melon in melons_dict:
    print_melon(melon)
