import os
from base.chart import Chart
from configs.common import example_dir


class ChartAnalyzer:

    def __init__(self, chart_json: str):
        """
        init a chart analyzer
        :param chart_json: chart file name(str)
        """
        self._chart = None
        self.load(chart_json)

    def load(self, chart_json: str):
        """
        (re)load a chart
        :param chart_json: chart file name(str)
        :return:
        """
        if chart_json is None:
            chart_json = os.path.join(example_dir, "nhelv.json")
        self._chart = Chart(chart_json)
        # init max time
        self._calc_max_time()

    # get overall chart info
    def get_max_tick(self) -> int:
        """
        get the maximum tick of the chart
        :return:
        """
        return self._chart.pages[-1].end_tick

    def get_max_time(self) -> float:
        """
        get the maximum time of the chart
        :return:
        """
        return self._max_time

    # chart queries
    def calc_time_by_tick(self, tick: int) -> float:
        """
        calculate absolute time by tick number
        :param tick: 
        :return:
        """
        pass

    # internal functions
    def _calc_max_time(self):
        """
        calculate the maximum time of the chart
        called by constructor
        :return:
        """
        self._max_time = 0.0
        for tid in range(len(self._chart.tempos) - 1):
            self._max_time += (self._chart.tempos[tid + 1].tick - self._chart.tempos[tid].tick) * \
                             self._chart.tempos[tid].value / 1000000 / self._chart.time_base


def test():
    nhelv = os.path.join(example_dir, "nhelv.json")
    analyzer = ChartAnalyzer(nhelv)
    print(f"max tick: {analyzer.get_max_tick()}")
    print(f"max time: {analyzer.get_max_time()}")


if __name__ == '__main__':
    test()
