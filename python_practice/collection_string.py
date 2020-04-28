import datetime

def learn_string():
    print(len("arunveersingh"))

    names = ";".join(["arun", "veer", "singh"])
    print(names)
    print(names.split(";"))

    print("tuple generated using partition", "arunveersingh".partition("veer"))

    first, separator, last = "Jammu:Kanyakumari".partition(":")
    print(first, separator, last)

    location = "I am {} degree north and {} degree south".format(25.6, 56.3)
    print(location)

    location = "I am {0} degree north and {1} degree south".format(25.6, 56.3)
    print(location)

    statement = "{0} is better than {1}. {2} is better than {0}.".format("Tokyo", "France", "Paris")
    print(statement)

    statement2 = "Galactic position is x = {pos[0]}, y = {pos[1]}".format(pos=(23, 46))
    print(statement2)

    statement3 = f"current time is {datetime.datetime.now().isoformat()}"
    print(statement3)


learn_string()
