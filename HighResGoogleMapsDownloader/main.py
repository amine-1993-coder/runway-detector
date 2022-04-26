'''
Download satellite images from lat and lon coordinates.

'''

import csv

import lib.GoogleMapDownloader as gmd
import lib.CoordinateConverter

def func2():
    meta_data = csv.reader(open(
        "C:/Users/moham/PycharmProjects/SatelliteImageDownloader-main/HighResGoogleMapsDownloader/datasets_positive/#Database_structure.csv"),
        delimiter=',')

    for meta_row in meta_data:
        print(meta_row)
        if meta_row[0] == ('file_name'):
            continue
        line_count = 1
        print(meta_row[0])

        with open('C:/Users/moham/PycharmProjects/SatelliteImageDownloader-main/HighResGoogleMapsDownloader/datasets_positive/{}'.format(meta_row[0])) as csvfile:
            csvreader = csv.reader(csvfile, delimiter=',')


            for row in csvreader:
                if line_count == 0:
                    line_count += 1

                else:
                    file_name = "C:/Users/moham/PycharmProjects/SatelliteImageDownloader-main/HighResGoogleMapsDownloader/raw_data/{}_{:04d}".format(
                        meta_row[4].strip(), line_count)

                    # print('line: {} \t name: {}'.format(line_count, file_name))
                    line_count += 1

            image = gmd.run_example(latitude=float(row[int(meta_row[2])]),
                                        longitude=float(row[int(meta_row[3])]),
                                        img_size=1000,
                                        map_size=5000,
                                        file_name=file_name)
            source="C:/Users/moham/PycharmProjects/SatelliteImageDownloader-main/HighResGoogleMapsDownloader/raw_data/{}_{:04d}.png".format(
                        meta_row[4].strip(), line_count-1)

        import shutil
        shutil.copy(source,"C:/Users/moham/PycharmProjects/SatelliteImageDownloader-main/HighResGoogleMapsDownloader/raw_data/tested_images")
        shutil.move(source,"C:/Users/moham/PycharmProjects/SatelliteImageDownloader-main/HighResGoogleMapsDownloader/raw_data/testing")




    print('done')










if __name__ == '__main__':

    lib.CoordinateConverter.func1()
    func2()


#49.19472222222222,-123.18388888888889





