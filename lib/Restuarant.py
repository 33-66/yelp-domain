from Review import Review


class Restuarant:
    def __init__(self, name):
        self._name = name

    def name(self):
        if type(self._name) == str:
            return self._name
        else:
            return "invalid input"

    def reviews(self):
        all_restuarant_reviews = []
        for each_review in Review.all():
            if each_review.restaurant() == self._name:
                all_restuarant_reviews.append(each_review)
        return all_restuarant_reviews

    def customers(self):
        
        customer_list = []
        for each_customer in Review.all():
            if each_customer.restaurant() == self._name:
                customer_list.append(each_customer.customer())
        return customer_list

    def average_star_rating(self):
        reviews = self.reviews()
        if not reviews:  # Check if there are no reviews
            return 0  # Return 0 if no reviews are available

        total = sum(review.rating() for review in reviews)
        return total / len(reviews)


# so we have  a method .name() when we run it we get  the name which should be a string else invalid input

restuarant1 = Restuarant("Hilton")
# print(restuarant1.name())

all_reviews = restuarant1.reviews()
for each_restuarant in all_reviews:
    print(
        f"Restaurant: {each_restuarant.restaurant()}, Rating: {each_restuarant.ratings}"
    )


#  Now we  get a list of all  customers  who reviewed that hotel

print(restuarant1.customers())

restuarant1


