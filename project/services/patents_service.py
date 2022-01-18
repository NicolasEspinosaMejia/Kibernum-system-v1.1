import json
from datetime import date

from project.constants import Constants
from project.resources.utils.generals_utils import GeneralsUtils
from project.services.service import Service


class PatentsService(Service):
    """[summary]

    Args:
        Service ([type]): [description]

    Returns:
        [type]: [description]
    """

    __DICTIONARY__ = {
        0: "A",
        1: "B",
        2: "C",
        3: "D",
        4: "E",
        5: "F",
        6: "G",
        7: "H",
        8: "I",
        9: "J",
        10: "K",
        11: "L",
        12: "M",
        13: "N",
        14: "O",
        15: "P",
        16: "Q",
        17: "R",
        18: "S",
        19:"T",
        20: "U",
        21: "V",
        22: "W",
        23: "X",
        24: "Y",
        25: "Z",
        "identification": {
            2: 5,
            1: 4
        }
    }

    def __init__(self, compose, repository):
        self.compose = compose
        self.repository = repository
        Service.__init__(self, compose)

    def get_patent(self, data):
        """[summary]

        Args:
            data ([type]): [description]
        """

        if not isinstance(data, dict):
            raise TypeError(
                "The 'data' is not in the correct format")

        if self.check_data_for_patent(data):
            raise ValueError(
                "The validation does not meet the minimum requirements")

        identification = data["identification"]
        result = self.get_patent_from_identifier(identification)

        return result

    def get_patent_from_identifier(self, identification):
        """[summary]

        Args:
            identification ([type]): [description]
        """
        patent_letter = ""
        result = {
            "data": [],
            "details": ""
        }

        if identification == 0:
            result["detail"] = "The identifier sent to process does not" +\
                "exist in the available patents"

        if identification > 0 and\
           identification <= 999:
            patent_letter = self.__DICTIONARY__[0]
            letters_of_patent = patent_letter*4

        if patent_letter is None or\
           len(patent_letter) == 0:
               patent_letter = self.__DICTIONARY__[int(identification/999)]
               identification = int(identification%999)

        if patent_letter is not None:
            letters_of_patent = patent_letter*4

        if len(str(identification)) < 3:
            missing_zeros = self.__DICTIONARY__["identification"][len(str(identification))] - len(str(identification))
            identification = str(identification).zfill(missing_zeros)

        patent = f"{letters_of_patent}{identification}"
        result["data"] = patent
        result["details"] = "The identifier was processed correctly to" +\
            "obtain the patent"

        return result

    def check_data_for_patent(self, data):
        """This method is in charge of performing a check on the
           attributes that the methods that use it must have mandatory

        Args:
            data (dict): This attribute refers to a dictionary, which
                         contains the configuration attributes for validations

        Returns:
            [dict]: Returns an element already constituted to send to the stored procedure
        """
        result = False

        if "identification" not in data or\
           isinstance(data["identification"], str) or\
           data["identification"] >= 24975:
            result = True

        return result
