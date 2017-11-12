import logging
import os

import matplotlib.pyplot as plt
import pandas as pd


class MonthlyReportException(Exception):
    pass


class MonthlyReport(object):
    """

    """
    DEPENDENT_VARIABLES = ['OrderTurnOver', 'OrderProfit']
    INDEPENDENT_VARIABLE = 'Sales_Person'

    def __init__(self, dataset, months_ago, path):
        if months_ago == 0:
            raise MonthlyReportException('you cannot use 0 when selecting months.')
        elif not isinstance(months_ago, int):
            raise MonthlyReportException('we need an integer as type for a month')
        self.month = months_ago if months_ago < 0 else months_ago * -1
        self.dataset = dataset
        self.path = path
        self.selected_month = None
        self.images = {}
        self.tables = {}

    def describe_past_month(self):
        """
        calculate necessary metrics for a specific month to get insight.
        build visuals based on the metrics
        :return:
        """
        df = self._read_dataset(self.dataset)
        df = MonthlyReport._calculate_metrics(df)
        df = MonthlyReport._set_order_date_per_month(df)
        df, self.selected_month = self._select_month(df)
        self._build_visuals(df)
        return vars(self)

    @staticmethod
    def _calculate_metrics(df):
        """
        calculate metrics from the raw data.
        :param df: Dataframe
        :return: Dataframe
        """
        df['OrderTurnOver'] = df['UnitPrice'] * df['OrderQty']
        df['OrderProfit'] = df['OrderTurnOver'] - (df['Unit_Cost'] * df['OrderQty'])
        return df

    def _read_dataset(self, dataset):
        """
        pickled dataframe is much faster to read
        :param dataset: path to dataset
        :return: pandas dataframe
        """
        logging.info('reading dataset {} ...'.format(self.dataset))
        path, ext = os.path.splitext(dataset)
        path_pickled = '.'.join((path, 'pickle'))
        if os.path.exists(path_pickled):
            return pd.read_pickle(path_pickled)
        return pd.read_excel(dataset)

    def _build_visuals(self, df):
        """
        build images for 2 variables wrt the indipendend.
        :param df: Dataframe
        :return: Dataframe
        """
        logging.info('creating visuals ...')
        for metric in MonthlyReport.DEPENDENT_VARIABLES:
            df_plot = df[[metric, MonthlyReport.INDEPENDENT_VARIABLE]]
            df_plot = df_plot.groupby(MonthlyReport.INDEPENDENT_VARIABLE).sum().unstack()
            self.images[metric] = self._build_image(df_plot, metric)
            self.tables[metric] = df_plot

    def _build_image(self, df, metric):
        """
        create a plot and a png image.
        :param df: Dataframe
        :param metric: name of the metric
        :return: Dataframe
        """
        df.plot(kind='bar')
        path_figure = os.path.join(self.path, metric + '.png')
        logging.info('outputting figure to {}'.format(path_figure))
        plt.savefig(path_figure, bbox_inches='tight')
        plt.close()
        return path_figure

    @staticmethod
    def _set_order_date_per_month(df):
        """
        convert dates to monthly dates so that we can group on the month.
        :param df: Dataframe
        :return: Dataframe
        """
        df['OrderDate'] = map(lambda x: x.strftime('%Y-%m'), df['OrderDate'])
        return df

    def _select_month(self, df):
        """
        select a slice of the dataframe based on the month
        :param df: Dataframe
        :return: Dataframe
        """
        past_months = sorted(df.groupby('OrderDate').groups.keys())
        selected_month = past_months[self.month]
        df_selected_month = df[df['OrderDate'] == selected_month]
        return df_selected_month, selected_month

