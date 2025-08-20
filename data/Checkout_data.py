from faker import Faker

faker = Faker(locale="FR_fr")

class Checkout_info:

    @staticmethod
    def checkoutinformation_form():
        return {
            "firstName" : faker.first_name(),
            "lastName" : faker.last_name(),
            "zipCode" : "92350"
        }
