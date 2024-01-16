from csv_ical import Convert
convert = Convert()
convert.CSV_FILE_LOCATION = ‘test.csv’
convert.SAVE_LOCATION = ‘test.ics’
convert.read_ical(convert.SAVE_LOCATION)
convert.make_csv()
convert.save_csv(convert.CSV_FILE_LOCATION)