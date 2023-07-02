import ruamel.yaml

with open("config/inputs/inputs.yaml") as file:
    data = file.read()
inputs = ruamel.yaml.load(data, Loader=ruamel.yaml.Loader)

if __name__ == "__main__":
    print(inputs["inputs"])
    print(len(inputs["inputs"]))