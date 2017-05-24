import csv

txt_file = r"SP500.txt" #Reades the text file to be converted
csv_file = r"SP500.csv" #Creates Output csv File Name to write to

in_txt = csv.reader(open(txt_file, 'r'), delimiter = ",") #Converts txt file to csv format
out_csv = csv.writer(open(csv_file, 'w', newline = '')) #writes data to csv file deleting line spaces

out_csv.writerows(in_txt) #
