import datetime
now = datetime.datetime.now()
print("The time now is", now)

# Open the election results and read the file.
election_data = open(file_to_load, 'r')

# To do: perform analysis.

# Close the file.
election_data.close()