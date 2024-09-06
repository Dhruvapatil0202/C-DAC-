
import csv

students_data = [{"ID": "1",
                  "Name" : "Rahul",
                  "Age" : 10,
                  "Grade": 'A'},
                 {"ID": "2",
                  "Name" : "Rahul",
                  "Age" : 20,
                  "Grade": 'A'},
                 {"ID": "3",
                  "Name" : "Rahul",
                  "Age" : 30,
                  "Grade": 'A'},
                 {"ID": "4",
                  "Name" : "Rahul",
                  "Age" : 50,
                  "Grade": 'A'}]


def writeToFile(file_name, data):

    with open(file_name,'w', newline = "") as file:
        fields = data[0].keys()
        writer = csv.DictWriter(file, fieldnames= fields)
        writer.writeheader()
        writer.writerows(data)

writeToFile('students.csv', students_data)


