# from restuarant import Restuarant
from Review import Review

class Customer:
    all_customers = []

    def __init__(self, given_name, family_name):
        self._given_name = given_name
        self._family_name = family_name
        self.all_customers.append(self)

    def given_name(self):
        return self._given_name

    def changing_given_name(self, new_given_name):
        self._given_name = new_given_name

    def family_name(self):
        return self._family_name

    def changing_family_name(self, new_family_name):
        self._family_name = new_family_name

    def full_name(self):
        return f"{self._given_name} {self._family_name}"

    @classmethod
    def all(cls):
        customers = []
        for each_customer in cls.all_customers:
             customers.append(each_customer.full_name())
        return customers

    def restaurants(self):
        restuarant_list = []
        for each_review in Review.all():
          if each_review.customer() == self:
            restuarant_list.append(each_review.restaurant())
        return restuarant_list  
        
    def add_review(self,restaurant,rating):
        review = Review(self,restaurant,rating)
        return review
    
    def num_reviews(self):
        each_review_list = []
        for each_customer in Review.all():
            if each_customer.customer() == self:
                each_review_list.append(each_customer)
        
        return len(each_review_list)
    @classmethod
    def find_by_name(cls,name):
        for each_name in cls.all_customers:
            if each_name.full_name() == name:
                return f'Name Found:{name}' 

            else:
                return "name not found"
    @classmethod
    def find_all_by_given_name(cls,name):
        given_names_list = []
        for each_given_name in cls.all_customers:
            if each_given_name.given_name() == name:
                given_names_list.append(each_given_name.full_name())
        return given_names_list


  

# new = Review("Simon","hilton",5)
 
# customer1 = Customer("Simon", "Nganga")


# we are  get  the customers name when we use the given_name() method
# print(customer1.given_name())

# we are now able to change the name using  changing_given_name() method

# customer1.changing_given_name("Brian")
# print(customer1.given_name())

# output will be Brian
# Here we get the customer's family name
# print(customer1.family_name())

# we can also change the family name

# customer1.changing_family_name("Wachira")
# when we print ut the name again  we find the name is changed to Wachira
# print(customer1.family_name())

# now we can get the full name  by running full_name()

# print(customer1.full_name())

# now we want that returns all customer instances customer.all()method
# print(Customer.all())


# print(customer1.restaurants())

# print(customer1.restaurants())


# add a review
# customer1.add_review("hilton",5)

# print(customer1.num_reviews())


# create some customers
# customer1 = Customer("Simon", "Nganga")
# customer2 = Customer("Alice", "Johnson")

# customer1 adds a review for a restaurant
# customer1.add_review("hilton", 5)

# customer2 adds a review for a restaurant
# customer2.add_review("marriott", 4)

# get the number of reviews for each customer
# print(customer1.num_reviews()) # Output: 1 
# print(customer2.num_reviews()) # Output: 1

# print(Customer.find_by_name('Simon Nganga'))

# print(Customer.find_all_by_given_name('Simon'))