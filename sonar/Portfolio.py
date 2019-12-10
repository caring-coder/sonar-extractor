class Portfolio:
    def __init__(self, key, name, project, organization):
        self.project = project
        self.organization = organization
        self.name = name
        self.key = key


def from_dict(dictionary):
    return Portfolio(dictionary["key"], dictionary["name"], dictionary["project"], dictionary["organization"])
