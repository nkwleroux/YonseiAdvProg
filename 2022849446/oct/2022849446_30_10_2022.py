from matplotlib import pyplot as plt
import fileinput
import os
import pandas as pd

dir_path = os.path.dirname(os.path.realpath(__file__))

# Task 1


def stringManipulation(s):
    fileOut = fileinput.input(dir_path + '\\text.txt')

    words = dict()
    try:
        for line in fileOut:
            line = line.rstrip()
            line = line.lower()
            line = line.translate({113: None, 111: None})
            line = line.split()
            for (i, word) in enumerate(line):
                words.update({i: word})

            print("Words added to the dict():", words)
    except:
        print('File cannot be read:', fileOut)
        exit()


def listStringToInt(list):
    return [int(i) for i in list]

# Task 2


def open_xlsx_temperature(path):
    xls = pd.ExcelFile(path)

    temperatures = []
    for sheet_name in xls.sheet_names:
        if ("2017" in path or "2018" in path):
            df = pd.read_excel(path, sheet_name=sheet_name,
                               index_col=None, usecols="B")
            extract_data = df[1:].to_numpy()
        else:
            df = pd.read_excel(path, sheet_name=sheet_name,
                               index_col=None, usecols="C")
            extract_data = df[2:].to_numpy()

        # Extract data from the excel file and converts it into a list
        extract_data = [int((i[0].split(" | "))[0]) for i in extract_data]
        temperatures.append(extract_data)

    print("temperatures in : ", path, temperatures)

    return temperatures


def getAverageTemperature(data):
    return round(sum(data) / len(data), 1)

# Task 3


def plot_data(data, year):
    fig = plt.figure()

    colors = ["blue", "green", "red", "orange", "purple"]

    lineChartData = []

    # Invert data
    for j in range(12):
        newlist = []
        for i in range(5):
            newlist += [data[i][j]]
        lineChartData.append(newlist)

    ax = plt.subplot2grid((2, 5), (0, 0), colspan=5)
    ax.plot(lineChartData)
    ax.legend(["2016", "2017", "2018", "2019", "2020"], loc="upper right")

    for i in range(len(data)):
        makeGraph(plt.subplot2grid((2, 5), (1, i), colspan=1),
                  data[i], year+i, colors[i])

    fig.suptitle("Average temperature per month for the years 2017-2022")
    fig.align_labels()
    fig.tight_layout()

    plt.show()


def makeGraph(ax, data, year, c):
    ax.bar(range(len(data)), data, width=0.5, color=c)

    ax.set_title(year)
    ax.set_xlabel("Month")
    ax.set_ylabel("Temperature")
    ax.axis([-1, 13, min(data)-1, max(data) + 1])


def main():
    print("Student id:", 2022849446)

    # Task 1
    stringManipulation("test sentences used on the string manipulation task")

    # Task 2
    dataPath = dir_path + "\\seoul_temperature"
    averages = []
    averages.append([getAverageTemperature(i)
                    for i in open_xlsx_temperature(dataPath + "\\2016.xlsx")])
    averages.append([getAverageTemperature(i)
                    for i in open_xlsx_temperature(dataPath + "\\2017.xlsx")])
    averages.append([getAverageTemperature(i)
                    for i in open_xlsx_temperature(dataPath + "\\2018.xlsx")])
    averages.append([getAverageTemperature(i)
                    for i in open_xlsx_temperature(dataPath + "\\2019.xlsx")])
    averages.append([getAverageTemperature(i)
                    for i in open_xlsx_temperature(dataPath + "\\2020.xlsx")])

    # Task 3
    plot_data(averages, 2016)


if __name__ == "__main__":
    main()
