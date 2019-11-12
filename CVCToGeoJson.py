import csv #
import os
for i in range(6):
    f = open("month"+str(i+1)+"tanom.geojson", "a")
    f.write('{"type":"FeatureCollection",\n');
    f.write('"features":[\n');
    f.close()
with open('datapoints.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    counterIndiv = [0,0,0,0,0,0];
    lowest = 0;
    highest = 0;
    for row in csv_reader:
        if line_count == 0:
            print(f'Column names are {", ".join(row)}')
            line_count += 1
        else:
            #{ "type": "Feature", "properties": { "id": "ak16994521", "mag": 2.3, "time": 1507425650893, "felt": null, "tsunami": 0 }, "geometry": { "type": "Point", "coordinates": [ -151.5129, 63.1016, 0.0 ] } },
            if row[5] != '':
                decomposedDate = row[1].split('/');
                month = decomposedDate[0];
                counterIndiv[int(month)-1] = counterIndiv[int(month)-1] + 1;
                fileToRead = "month"+month+"tanom.geojson";
                f = open(fileToRead, "a");
                f.write('\n{"type":"Feature",');
                if float(row[5])<lowest:
                    lowest = float(row[5]);
                if float(row[5])>highest:
                    highest = float(row[5]);
                row[5] = float(row[5]);

                #f.write('"properties": { "tanom_bin":'+row[4]+',"tanom":'+row[5]+',"num_records": '+row[0]+'}, ');
                f.write('"properties":{"tanom":'+str(row[5])+'},');
                f.write('"geometry":{"type":"Point","coordinates":['+row[2]+','+row[3]+']}},');
                f.close();
                #print(f'\t{row[0]} works in the {row[1]} department, and was born in {row[2]}.')
                line_count += 1
    print(f'Processed {line_count} lines.')
    print(counterIndiv);
    print('Lowest: ',lowest);
    print('Highest: ',highest);

for i in range(6):
    f = open("month"+str(i+1)+"tanom.geojson", "a")
    f.write('\n]');
    f.write('\n}');
    f.close()
