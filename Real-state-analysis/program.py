import os
import csv
try:
    import statistics
except:
    import stats_for_python2 as statistics

from data_types import Purchase



def load_file(filename):
    with open(filename, 'r') as fin:
        # with open(filename, 'r') as fin:
        reader = csv.DictReader(fin)
        purchases = []
        for row in reader:
            p = Purchase.create_from_dict(row)
            purchases.append(p)


    return purchases


# def load_file_old(filename):
#     with open(filename, 'r', encoding='utf-8') as fin:
#         header = fin.readline().strip()
#
#         lines = []
#         for line in fin:
#             line_data = line.strip().split(',')
#             lines.append(line_data)
#
#     return []

def get_price(p):
    return p.price


def query_data(data): #: list[Purchase]):
    data.sort(key=get_price)
    data.sort(key=lambda p: p.price)


    high_purchase_price = data[-1]

    print("The most expensive house costs $ {}".format(high_purchase_price.price))

    lower_purchase_price = data[0]
    print("The leat expensive house costs $ {}".format(lower_purchase_price.price))



    # # Loopy version
    # # Average price?
    #
    # prices = []
    # for purchase in data:
    #     prices.append(purchase.price)
    #

    #
    # prices = []
    # for purchase in data:
    #     if(purchase.beds == 2):
    #         prices.append (purchase.price)
    #

    two_bed_homes = (
        p  # projection or items
        for p in data  # the set to process
        if announce (p, '2-bedrooms, found {}'.format (p.beds)) and p.beds == 2  # test / condition
    )

    homes = []
    for h in two_bed_homes:
        if len (homes) > 5:
            break
        homes.append (h)

    ave_price = statistics.mean ((announce (p.price, 'price') for p in homes))
    ave_baths = statistics.mean ((p.baths for p in homes))
    ave_sqft = statistics.mean ((p.sq__ft for p in homes))
    print ("Average 2-bedroom home is ${:,}, baths={}, sq ft={:,}"
           .format (int (ave_price), round (ave_baths, 1), round (ave_sqft, 1)))


def announce(item, msg):
    print("Pulling item {} for {}".format(item, msg))
    return item

def main():
    print_header()
    filename = get_data_file()
    data = load_file(filename)
    query_data(data)


def print_header():
    print('--------------------')
    print('   REAL STATE APP')
    print('--------------------')
    print()


def get_data_file():
    base_folder = os.path.dirname(__file__)

    return os.path.join(base_folder, 'data', 'data.csv')


if __name__ == '__main__':
    main()