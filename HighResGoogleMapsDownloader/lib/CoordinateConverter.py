import pandas as pd


def func1():
    # csv_file = "airport-data.csv"

    df = pd.read_csv(
        "C:/Users/moham/PycharmProjects/SatelliteImageDownloader-main/HighResGoogleMapsDownloader/datasets_positive/airport-data.csv",
        usecols=['ARP Latitude Sec', 'ARP Longitude Sec', 'DD_Latitudes', 'DD_Longitudes', 'Api_key_used'])

    '''   count = 0
    count += 1
    count = count + 1
    for j in range(0,count):
        dfj = pd.read_csv("C:/Users/moham/PycharmProjects/SatelliteImageDownloader-main/HighResGoogleMapsDownloader/datasets_positive/airport-data.csv")
        dfj = pd.read_csv(io.StringIO(dfj.to_csv(index=False)))
        dfj = pd.DataFrame(columns=['ARP Latitude Sec', 'ARP Longitude Sec', 'DD_Latitudes', 'DD_Longitudes'])
        dfj = dfj.append({'ARP Latitude Sec': sys.argv[2], 'ARP Longitude Sec': sys.argv[3]}, ignore_index=True)

    df = pd.concat([df, dfj], ignore_index=True, axis=0)'''

    latitudes = df['ARP Latitude Sec']
    longitudes = df['ARP Longitude Sec']

    def lat_lon_converter(latitudes, longitudes):
        """
        Converts lat and long seconds to degree decimal.

        lat = 229559.8190N  ---->> 63.766616388888885
        lon = 0618238.0220W ---->> -171.73278388888886

        GoogleMapDownloader.py takes degree decimal
        """

        lat = []
        lon = []

        for i in latitudes:
            if i[-1] == "N":  # North
                i = i[:-1]
            elif i[-1] == "S":  # South
                i = "-" + i[:-1]

            i = float(i)
            degree = i // 3600
            remainder = i % 3600
            mins = remainder // 60
            secs = remainder % 60
            dd = degree + mins / 60 + secs / 3600
            lat.append(dd)

        for i in longitudes:
            if i[-1] == "E":  # East
                i = i[:-1]
            elif i[-1] == "W":  # West
                i = "-" + i[:-1]

            i = float(i)
            degree = i // 3600
            remainder = i % 3600
            mins = remainder // 60
            secs = remainder % 60
            dd = degree + mins / 60 + secs / 3600
            lon.append(dd)

        return lat, lon

    lat, lon = lat_lon_converter(latitudes, longitudes)

    df["DD_Latitudes"] = lat
    df["DD_Longitudes"] = lon
    df.to_csv(
        "C:/Users/moham/PycharmProjects/SatelliteImageDownloader-main/HighResGoogleMapsDownloader/datasets_positive/airport-data.csv",
        index=False)
    df.to_csv(index=False)


if __name__ == '__main__':

    func1()
