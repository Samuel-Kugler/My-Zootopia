import json


def load_data(file_path):
    """ Loads a JSON file """
    with open(file_path, "r") as handle:
        return json.load(handle)


def get_information(animals_data: list[dict]):
    for animal in animals_data:
        #filter data
        name = animal.get("name", None)
        if name is None:  # skips the complete animal if the name doesn't exist
            continue

        location = animal.get("locations", ["/"])[0]
        characteristics = animal.get("characteristics", {})
        diet = characteristics.get("diet", "/")
        type_ = characteristics.get("type", "/")

        #Output
        print(f"Name: {name}")
        print(f"Diet: {diet}")
        print(f"Location: {location}")

        if type_ != "/":
            print(f"Type: {type_}")

        print()


def main():
    animals_data = load_data('animals_data.json')

    get_information(animals_data)


if __name__ == "__main__":
    main()
