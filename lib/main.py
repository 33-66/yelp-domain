from    Customer import Customer
from  Restuarant import Restuarant
from Review import Review

customer1 = Customer("Simon", "Nganga")
customer2 = Customer("Brian", "Wachira")
customer3 = Customer("Samuel" ,"Bearnard")
# Customer.given_name( ) method should returm the  first name  in a full namme.
print(customer1.given_name())
# we  should be  able to change the first name  using Customer. changing_given_name()
# the  name will be changed to Samuel the new name created
customer1.changing_given_name("Samuel")
print(customer1.given_name())
# customer.Family_name() is  a method that returns the second name  of the customer
print(customer1.family_name())
# we can also change it using changing_family_name() to a new family name
customer1.changing_family_name("williams")
print(customer1.family_name())
# now we can now print out a full_name using  the customer.full_naamw()
print(customer1.full_name())

# Customer.all() which returns all customer names
print(Customer.all())

# Restuarant
restuarant1 = Restuarant("Mellow")
restuarant2 = Restuarant("bingos")
# Restuarant.name() returns the name of the restuarant
print(restuarant1.name())


# Review
review1 = Review("Brian Wachira","bingos",7)
review2 = Review("simon Nganga","Mellow",4)
# Review.rating() reurns the rating of the restuarant
print(review1.rating())
#  review .all( ) returns all reviews
all_reviews = Review.all()
for each_review in all_reviews :
     print (f"Name:{each_review.customer()} Hotel:{each_review.restaurant()} Rating:{each_review.rating()}")

# OBJECT RELATIONSHIP /METHODS
    #  Review
# review.customer() should return the name of the customer
print(review1.customer())
# review.restaurant() returns  the name of the restuarant
print(review2.restaurant())

# Restuarant
# restuarant.reviews() returns a list of all reviews for that restuarant
all_reviews = restuarant1.reviews()
for each_restuarant in all_reviews:
     print(
         f"Restaurant: {each_restuarant.restaurant()}, Rating: {each_restuarant.ratings}"
     )
# restuarant.customer() returns a list of those who reviewed a certin restuarant
print(restuarant1.customers())

# Customer

# customer.restaurant() returns the list of restuarants a customer has reviewed

# customer.add_review and its associated to that customer
customer1.add_review("Hilton",5)

# Aggregate and Association Methods
# Customer.num_reviews() return total number of review 
print(customer1.num_reviews())
# customer.find_by_name() returns first full name
print(Customer.find_by_name("Samuel williams"))
# however if name not found  it will  give an output
print(Customer.find_by_name("Samuel william"))
# Customer.find_all_by_given_name() returns  a list of all the given_names  that are similar
print(Customer.find_all_by_given_name("Samuel"))

# RESTUARANT
