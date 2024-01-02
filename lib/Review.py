class Review:
    all_reviews = []

    def __init__(self, customer, restaurant, rating):
        self.customers = customer
        self.restaurants = restaurant
        self.ratings = rating
        self.all_reviews.append(self)

    def rating(self):
        if type(self.ratings) == int:
            return self.ratings
        else:
            return "invalid input"

    @classmethod
    def all(cls):
        return cls.all_reviews
       

    def customer(self):
        return self.customers

    def restaurant(self):
        return self.restaurants


# we are expected  if u run  rating  it should be a number

# review1 = Review("Simon", "Hilton", 5)
# review1.rating()
# print(review1.rating())
# output invalid output
# review2 = Review("Brian", "Hilton", 5)
# print(review2.rating())
# output  5

# we need all ratings so we use .all()  method

# all_reviews = Review.all()
# for each_review in all_reviews :
    # print (f"{each_review.restaurant()},{each_review.rating()}")

# we want a method to print out the name of the customer for each review
# print(review1.customer())
# print(review2.customer())

#  now we can also get the name of each reviewed restuarant
# print(review1.restaurant())
# print(review2.restaurant())
