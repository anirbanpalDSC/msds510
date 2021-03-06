"""
This module initializes the object with a dictionary-based
record. If no records is provided, the instance attributes
are not set.
"""

import datetime as dt


class Avenger:

    def __init__(self, record=None):
        """
        :param record: record (dict): Dictionary-based record of Avenger data
        """

        if record:
            self.record = record
            self.url_value = record["url"]
            self.alias = record["name_alias"]
            self.appearances_count = record["appearances"]
            self.current = record["current"]
            self.death1 = record["death1"]
            self.death2 = record["death2"]
            self.death3 = record["death3"]
            self.death4 = record["death4"]
            self.death5 = record["death5"]
            self.first_appearance = record["full_reserve_avengers_intro"]
            self.gender_value = record["gender"]
            self.honorary = record["honorary"]
            self.notes_value = record["notes"]
            self.probationary_introl = record["probationary_introl"]
            self.return1 = record["return1"]
            self.return2 = record["return2"]
            self.return3 = record["return3"]
            self.return4 = record["return4"]
            self.return5 = record["return5"]
            self.year_value = record["year"]
            self.years_since_joining_value = record["years_since_joining"]

    def url(self):
        """
        Returns:
            str: The URL of the comic character on the Marvel Wiki
        """
        return self.url_value

    def name_alias(self):
        """
        Returns:
            str: The full name or alias of the character
        """
        return self.alias

    def appearances(self):
        """
        Returns:
            int: The number of comic books that character
            appeared in as of April 30

        """
        return int(self.appearances_count)

    def is_current(self):
        """

        Returns:
            bool: Is the member currently active on an
            avengers affiliated team? (True/False)

        """

        if not self.current.strip():
            return None
        else:
            return True if self.current == 'YES' else False

    def gender(self):
        """

        Returns:
            str: The recorded gender of the character

        """
        return self.gender_value

    def year(self):
        """

        Returns:
            int: The year the character was introduced
            as a full or reserve member of the Avengers

        """
        return int(self.year_value)

    def get_month(self):
        months = ["jan", "feb", "mar", "apr", "may", "jun",
                  "jul", "aug", "sep", "oct", "nov", "dec"]

        for i in range(0, len(months)):
            if months[i] in self.first_appearance.lower():
                return i + 1
        return 0

    def date_joined(self):
        """

        Returns:
            datetime.date: The date the character joined

        """

        return (dt.date(self.year(), self.get_month(), 1))

    def days_since_joining(self):
        """

        Returns:
            int: The number of integer days since the character joined

        """
        rval = dt.date.today() - self.date_joined()
        rval = rval.days
        return rval

    def years_since_joining(self):
        """

        Returns:
            int: The number of integer years since the character joined

        """

        return dt.date.today().year - self.year()

    def notes(self):
        """STRIP OFF TRAILING NEWLINES AND SPACES

        Returns:
            str: Descriptions of deaths and resurrections.

        """
        return self.notes_value.strip()

    def __str__(self):
        """

        Returns:
            str: A human-readable value for this character

        """
        return self.name_alias()

    def __repr__(self):
        """

        Returns:
            str: String representation of object.  Useful for debugging.
        """

        return "Avenger(" + ",".join(key + "=" + val
                                     for key, val in self.record.items()
                                     if key == 'name_alias'
                                     or key == 'url') + ")"

    def to_markdown(self, recordslist, outfile):
        """takes a list of records, formats them
        and prints them to an output file.
        Args:
            recordslist: list of top 10 avenger records
            outfile: a file location string.
        Result:
            prints the contents to a formatted outfile.
        """
        with open(outfile, 'w') as ofile:
            for idx, rc in enumerate(recordslist):
                avenger = Avenger(rc)
                ofile.write("# " + str(idx + 1) + ". "
                            + avenger.name_alias() + "\n\n")
                ofile.write("* Number of Appearances: "
                            + str(avenger.appearances()) + "\n")
                ofile.write("* Year Joined: " + str(avenger.year()) + "\n")
                ofile.write("* Years Since Joining: "
                            + str(avenger.years_since_joining()) + "\n")

                ofile.write("* URL: " + avenger.url() + "\n\n")
                ofile.write("## Notes \n\n")
                ofile.write(avenger.notes() + "\n\n")

"""
Test method for Avengers class
"""

if __name__ == '__main__':
    pym_record = {
        'appearances': '1269',
        'current': 'YES',
        'death1': 'YES',
        'death2': '',
        'death3': '',
        'death4': '',
        'death5': '',
        'full_reserve_avengers_intro': 'Sep-63',
        'gender': 'MALE',
        'honorary': 'Full',
        'name_alias': 'Henry Jonathan "Hank" Pym',
        'notes': 'Merged with Ultron in Range of Ultron Vol. 1. A funeral was held. \n',
        'probationary_introl': '',
        'return1': 'NO',
        'return2': '',
        'return3': '',
        'return4': '',
        'return5': '',
        'url': 'http://marvel.wikia.com/Henry_Pym_(Earth-616)',
        'year': '1963',
        'years_since_joining': '52'
    }

hank_pym = Avenger(pym_record)
print('Name/Alias: {}'.format(hank_pym.name_alias()))
print('URL: {}'.format(hank_pym.url()))
print('Is Current?: {}'.format(hank_pym.is_current()))
print('Gender: {}'.format(hank_pym.gender()))
print('Year Joined: {}'.format(hank_pym.year()))
print('Date Joined: {}'.format(hank_pym.date_joined()))
print('Days Since Joined: {}'.format(hank_pym.days_since_joining()))
print('Years Since Joining: {}'.format(hank_pym.years_since_joining()))
print('Notes: {}'.format(hank_pym.notes()))
print('__str__: {}'.format(hank_pym.__str__()))
print('__repr__: {}'.format(hank_pym.__repr__()))
