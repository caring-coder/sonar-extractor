def from_dict(dictionary):
    return Paging(int(dictionary["total"]), int(dictionary["pageSize"]))


class Paging:
    def __init__(self, nb_elements, nb_elmements_by_page):
        self.nb_elmements_by_page = nb_elmements_by_page
        self.nb_elements = nb_elements
