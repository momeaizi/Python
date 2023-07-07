
class CsvReader():
    def __init__(self, filename=None, sep=',', header=False, skip_top=0, skip_bottom=0):
        self.filename = filename
        self.sep = sep
        self.header = header
        self.skip_top = skip_top
        self.skip_bottom = skip_bottom

    def __enter__(self):
        try:
            self.file = open(self.filename)
        except FileNotFoundError:
            return None

        self.data = []
        self.header_row = None
        self.num_fields = None

        self.num_fields = None

        for _ in range(self.skip_top):
            next(self.file)

        for line in self.file:
            fields = line.strip().split(self.sep)

            if self.num_fields is None:
                self.num_fields = len(fields)
            elif len(fields) != self.num_fields:
                return None
            self.data.append(fields)
            # print(len(fields), " : ", *fields)

        for _ in range(self.skip_bottom):
            self.data.pop()

        return self


    def __exit__(self, exc_type, exc_value, traceback):
        try:
            self.file.close()
        except AttributeError:
            return None

    def getdata(self):
        """ Retrieves the data/records from skip_top to skip bottom.
        Return:
        nested list (list(list, list, ...)) representing the data.
        """

        return self.data

    def getheader(self):
        """ Retrieves the header from csv file.
        Returns:
        list: representing the data (when self.header is True).
        None: (when self.header is False).
        """
        return self.header_row


with CsvReader('bad.csv' , header=False) as reader:

    if reader is None:
        print("bad csv file")
        exit(1)

    data = reader.getdata()

    for record in data:
        for field in record:
            print("{:<15}".format(field), end='')
        print('\n')

    print(reader.getheader())
