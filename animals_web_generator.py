import json
from json import JSONDecodeError


def error_html_template(error_type: str) -> str:
    """
    Holds a backup html file for error display.
    Args:
         error_type: str
    return: str
    """
    html_emergency_file = (f"<!doctype html>"
                           f"<html>"
                           f"<head>"
                           f"<meta charset='utf-8'>"
                           f"<meta name='viewport' content='width=device-width, initial-scale=1'>"
                           f"<title>Error!</title>"
                           f"</head>"
                           f"<body>"
                           f"<h1><strong>{error_type}</strong></h1>"
                           f"</body>"
                           f"</html>")

    return html_emergency_file


def read_html_file() -> str:
    """
    Loads a html file template.
     return: str
    """
    try:
        with open("animals_template.html", "r") as html_file:
            content = html_file.read()
    except FileNotFoundError:
        content = error_html_template("The html template file is missing.")
    except UnicodeDecodeError:
        content = error_html_template("The file couldn't be encoded correctly.")

    return content


def load_data(file_path) -> list[dict]:
    """
    Loads a JSON file and returns its data.
    return: list[dict]
    """
    try:
        with open(file_path, "r") as handle:
            json_file = json.load(handle)
    except FileNotFoundError:
        json_file = [{"name": "Error!", "characteristics": {"type": "File can't be found."}}]
    except JSONDecodeError:
        json_file = [{"name": "Error!", "characteristics": {"type": "File is corrupted."}}]
    except UnicodeDecodeError:
        json_file = [{"name": "Error!", "characteristics": {"type": "File can't be encoded."}}]

    return json_file


def serialize_animal(animal: dict, animal_name: str) -> str:
    """
    helper for get_information: serializes the data for a single animal as a html object.
    Args:
        animal: dict
        animal_name: str
    return: str
    """
    result_animal = ""

    #gets the interesting information
    pre_location = animal.get("locations", ["/"])
    location = "/"
    if len(pre_location) > 0:
        location = pre_location[0]

    characteristics = animal.get("characteristics", {})
    diet = characteristics.get("diet", "/")
    type_ = characteristics.get("type", "/")

    # file modulation to html objects inside a string
    result_animal += (f'<li class="cards__item">'
                      f'<div class="card__title">{animal_name}</div>'
                      f'<p class="card__text">')

    # checking if animal for the list has a diet
    if diet != "/":
        result_animal += f"<strong>Diet:</strong> {diet}<br/>\n"

    # checking if animal for the list has a location
    if location != "/":
        result_animal += f"<strong>Location:</strong> {location}<br/>\n"

    # checking if animal for the list has a type
    if type_ != "/":
        result_animal += f"<strong>Type:</strong> {type_}<br/>\n"

    # end of file
    result_animal += f"</p>\n</li>\n"

    return result_animal


def get_information(animals_data: list[dict]) -> str:
    """
    Gets the required characteristics out of a data file and returns them in a string for html output.
    Args:
        animals_data: lsts[dict]
    return: str
    """
    information = ""

    for animal in animals_data:
        #filter data
        name = animal.get("name", None)
        if name is None:  # skips the complete animal if the name doesn't exist
            continue

        #adding animal to our html string
        information += serialize_animal(animal, name)

    return information


def create_file_text(html_info: str, animal_info: str) -> str:
    """
     Creates the content for the new html file by adding content to a template.
     Args:
          html_info: str
          animal_info: str
    return: str
     """
    result = html_info.replace("__REPLACE_ANIMALS_INFO__", animal_info)

    return result


def new_html_file(new_file_text: str):
    """
    Creates a new html file with the code we want to display to the user.
    Args:
        new_file_text: str
    """
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
