import json


def read_html_file() -> str:
    """ Loads a html file """
    with open("animals_template.html", "r") as html_file:
        content = html_file.read()

    return content


def load_data(file_path):
    """ Loads a JSON file """
    with open(file_path, "r") as handle:
        return json.load(handle)


def get_information(animals_data: list[dict]) -> str:
    """ Gets the required characteristics out of a data file and returns them in a string for html output """
    information = ""

    for animal in animals_data:
        #filter data
        name = animal.get("name", None)
        if name is None:  # skips the complete animal if the name doesn't exist
            continue

        location = animal.get("locations", ["/"])[0]
        characteristics = animal.get("characteristics", {})
        diet = characteristics.get("diet", "/")
        type_ = characteristics.get("type", "/")

        #file modulation to html objects inside a string
        information += (f'<li class="cards__item">'
                        f'<div class="card__title">{name}</div>'
                        f'<p class="card__text">')

        #adding list with data
        information += (f"<strong>Diet:</strong> {diet}<br/>\n"
                        f"<strong>Location:</strong> {location}<br/>\n")

        #checking if animal for the list has a type
        if type_ != "/":
            information += f"<strong>Type:</strong> {type_}<br/>\n"

        #end of file
        information += f"</p>\n</li>\n"

    return information


def create_file_text(html_info: str, animal_info: str) -> str:
    """ Creates the content for the new html file by adding content to a template """
    result = html_info.replace("__REPLACE_ANIMALS_INFO__", animal_info)

    return result


def new_html_file(new_file_text: str):
    """ Creates a new html file with the code we want to display to the user."""
    with open("animals.html", "w") as new_file:
        new_file.write(new_file_text)


def main():
    #Variable functions
    animals_data = load_data('animals_data.json')
    animal_information = get_information(animals_data)
    html_info = read_html_file()

    #Creating new file
    new_html_file(create_file_text(html_info, animal_information))


if __name__ == "__main__":
    main()
