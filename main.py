import matplotlib.pyplot as plt
import pandas as pd


class Graph:
    def __init__(self, figure_num: int, path: str, time_idx: int, sensitive_idx: int, moderate_idx: int,
                 average_idx: int, x_label: str,
                 y_label: str,
                 title: str):
        self.dataframe = 0
        self.figure_num = figure_num
        self.path = path
        self.time_idx = time_idx
        self.sensitive_idx = sensitive_idx
        self.moderate_idx = moderate_idx
        self.average_idx = average_idx
        self.x_label = x_label
        self.y_label = y_label
        self.title = title

    def parse(self):
        self.dataframe = pd.read_csv(self.path)
        self.dataframe = self.dataframe['info'].str.split(' ', expand=True)
        self.dataframe[self.sensitive_idx] = self.dataframe[self.sensitive_idx].astype(int)
        self.dataframe[self.moderate_idx] = self.dataframe[self.moderate_idx].astype(int)
        self.dataframe[self.average_idx] = self.dataframe[self.average_idx].astype(int)

    def generate_graph(self):
        # graph
        plt.figure(self.figure_num)
        plt.title(self.title, size=25)
        ax = plt.gca()

        # sensitive
        plt.xlabel(self.x_label, size=20)
        ax.axes.xaxis.set_ticks([])
        plt.plot(self.dataframe[self.time_idx], self.dataframe[self.sensitive_idx], color="orange",
                 label="sensitive")

        # moderate
        plt.ylabel(self.y_label, size=20)
        plt.plot(self.dataframe[self.time_idx], self.dataframe[self.moderate_idx],
                 label="moderate")

        # average
        # plt.plot(self.dataframe[self.time_idx], self.dataframe[self.average_idx], color="gray", label="average")

        # remind box
        plt.legend(loc='best', shadow=True, fontsize="xx-large")

        plt.show()

    def start(self):
        self.parse()
        self.generate_graph()


def main():
    path = "PoseQualityLog/TestQualityLog.txt"
    graph = Graph(figure_num=1, path=path, time_idx=1, sensitive_idx=3, moderate_idx=4, average_idx=5,
                  x_label="Time",
                  y_label="Pose quality",
                  title="Cu4 Lidar pose quality")
    graph.start()


if __name__ == '__main__':
    main()
