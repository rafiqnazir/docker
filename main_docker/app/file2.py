from faker import Faker
def fake_data():
	fake = Faker()
	return {'name':fake.name(),'address':fake.address()}
