import sys
import string

product_commodity_map = {
	"foodgrains" : [ "rice", "wheat", "dal" ],
	"furniture" : [ "table", "sofa", "chair" ],
	"electronics" : [ "mobile", "tv", "tablet" ],
	"cosmetics" : [ "cream", "perfume", "lotion" ],
	}

product_gst_slab = {
	"foodgrains" : 0,
	"furniture"	: 8,
	"cosmetics"	: 24,
	"electronics" : 18
}

class ProductCategory:

	def __init__(self, gst_slab,units_purchased,unit_price):
		
		self.unit_price = unit_price
		self.units_purchased = units_purchased
		self.gst_slab = gst_slab

	def calculate_total_price(self):
		total_price = self.unit_price + (self.unit_price*self.gst_slab/100)
		self.total_price = total_price
		print(total_price)

def main():

	units_purchased = int(sys.argv[1])
	commodity = str(sys.argv[2]).lower()
	unit_price = float(sys.argv[3])

	product = [x for x in product_commodity_map if commodity in product_commodity_map[x]][0]

	item = ProductCategory(product_gst_slab[product],units_purchased,unit_price)
	item.calculate_total_price()
	

if __name__ == "__main__":
    main()
		