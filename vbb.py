import reporter
import csv

company_file = open('NASDAQ.csv')
csv_reader = csv.reader(company_file)
company_list = list(csv_reader)
t_list = []
report_done = False
for company in company_list:
    if company[5] == 'Technology':
        r = reporter.Reporter(company)
        t_list.append(r)

for i in range(5):
    t_list[i].start()

counter = 4
list_len = len(t_list)

while not report_done:
    if t_list[counter].driver_done:
        counter += 1
        t_list[counter].start()
    if counter == list_len:
        report_done = True
