import json
from datetime import date

from project.constants import Constants
from project.resources.utils.generals_utils import GeneralsUtils
from project.services.service import Service


class IdentifiersService(Service):
    """[summary]

    Args:
        Service ([type]): [description]

    Returns:
        [type]: [description]
    """

    __DICTIONARY__ = {
        "A": 0,
        "B": 1,
        "C": 2,
        "D": 3,
        "E": 4,
        "F": 5,
        "G": 6,
        "H": 7,
        "I": 8,
        "J": 9,
        "K": 10,
        "L": 11,
        "M": 12,
        "N": 13,
        "O": 14,
        "P": 15,
        "Q": 16,
        "R": 17,
        "S": 18,
        "T": 19,
        "U": 20,
        "V": 21,
        "W": 22,
        "X": 23,
        "Y": 24,
        "Z": 25
    }

    def __init__(self, compose, repository):
        self.compose = compose
        self.repository = repository
        Service.__init__(self, compose)

    def get_identification(self, data):
        """[summary]

        Args:
            data ([type]): [description]
        """

        if not isinstance(data, dict):
            raise TypeError(
                "The 'data' is not in the correct format")

        if self.check_data_for_identification(data):
            raise ValueError(
                "The validation does not meet the minimum requirements")

        patent = data["patent"]
        result = self.get_identification_from_patent(patent)

        return result

    def get_identification_from_patent(self, patent):
        """[summary]

        Args:
            identification ([type]): [description]
        """
        result = {
            "data": [],
            "details": ""
        }

        first_letter = patent[0:1]
        missing_records = patent[4:7]
        result["data"] = (self.__DICTIONARY__[first_letter] * 999) + int(missing_records)
        result["details"] = "The patent was processed correctly to" +\
            "obtain the identification"

        return result

    def check_data_for_identification(self, data):
        """This method is in charge of performing a check on the
           attributes that the methods that use it must have mandatory

        Args:
            data (dict): This attribute refers to a dictionary, which
                         contains the configuration attributes for validations

        Returns:
            [dict]: Returns an element already constituted to send to the stored procedure
        """
        result = False

        if "patent" not in data or\
           isinstance(data["patent"], int):
            result = True

        return result
