from book.models import Publisher

def load_Publisher():
    for i in range(10): 
        Publisher.objects.create(name = f"Name{i}", 
                address = f"Address{i}", 
                city = f"City{i}",
                state_province = f"state_province{i}", 
                country = f"country{i}"
                )
