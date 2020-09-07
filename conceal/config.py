# config.py
import toml


def configure(input_file):
    inp = toml.load(input_file)
    return inp
    print("Loaded Config: ✔")
