from timing import countdown_timer
import csv


def writer(input_variable, filename):
    outfile = open(filename, 'w')
    out = csv.writer(outfile,delimiter = ' ')
    out.writerows(map(lambda x: [x], input_variable))
    outfile.close()