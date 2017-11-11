import logging
import os

import matplotlib.pyplot as plt
import pandas as pd


class DescriptionException(Exception):
    pass


class Description(object):
    METRICS_TO_PLOT = ['OrderTurnOver', 'OrderProfit']

    def __init__(self, dataset, month, path):
        if month == 0:
            raise DescriptionException('you cannot use 0 when selecting months.')
        elif not isinstance(month, int):
            raise DescriptionException('we need an integer as type for a month')
        self.month = month if month < 0 else month * -1
        self.dataset = dataset
        self.path = path
        self.selected_month = None
        self.images = {}
        self.tables = {}

    @staticmethod
    def _calculate_metrics(df):
        df['OrderTurnOver'] = df['UnitPrice'] * df['OrderQty']
        df['OrderProfit'] = df['OrderTurnOver'] - (df['Unit_Cost'] * df['OrderQty'])
        return df

    def describe_past_month(self):
        logging.info('reading dataset {} ...'.format(self.dataset))
        df = self._read_dataset(self.dataset)
        df = Description._calculate_metrics(df)
        df = Description._set_order_date_per_month(df)
        df, self.selected_month = self._select_month(df)
        self._build_visuals(df)
        return vars(self)

    def _read_dataset(self, dataset):
        """
        pickled dataframe is much faster to read
        :param dataset: path to dataset
        :return: pandas dataframe
        """
        path, ext = os.path.splitext(dataset)
        path_pickled = '.'.join((path, 'pickle'))
        if os.path.exists(path_pickled):
            return pd.read_pickle(path_pickled)
        return pd.read_excel(dataset)

    def _build_visuals(self, df):
        for metric in Description.METRICS_TO_PLOT:
            df_plot = df[[metric, 'Sales_Person']]
            df_plot = df_plot.groupby('Sales_Person').sum().unstack()
            self.images[metric] = self._build_image(df_plot, metric)
            self.tables[metric] = df_plot

    def _build_image(self, df, metric):
        df.plot(kind='bar')
        path_figure = os.path.join(self.path, metric + '.png')
        logging.info('outputting figure to {}'.format(path_figure))
        plt.savefig(path_figure, bbox_inches='tight')
        plt.close()
        return path_figure

    @staticmethod
    def _set_order_date_per_month(df):
        df = df.sort('OrderDate')
        df['OrderDate'] = map(lambda x: x.strftime('%Y-%m'), df['OrderDate'])
        return df

    def _select_month(self, df):
        past_months = df.groupby('OrderDate').groups.keys()
        selected_month = past_months[self.month]
        df_selected_month = df[df['OrderDate'] == selected_month]
        return df_selected_month, selected_month

