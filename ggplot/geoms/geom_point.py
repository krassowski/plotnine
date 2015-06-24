from __future__ import (absolute_import, division, print_function,
                        unicode_literals)

import numpy as np
import matplotlib.lines as mlines

from ..utils import make_rgba
from .geom import geom


class geom_point(geom):
    DEFAULT_AES = {'alpha': 1, 'color': 'black', 'fill': None,
                   'shape': 'o', 'size': 5}
    REQUIRED_AES = {'x', 'y'}
    DEFAULT_PARAMS = {'stat': 'identity', 'position': 'identity'}

    _units = {'shape'}

    def draw_groups(self, data, scales, coordinates, ax, **params):
        """
        Plot all groups
        """
        pinfos = self._make_pinfos(data, params)
        for pinfo in pinfos:
            self.draw(pinfo, scales, coordinates, ax, **params)

    @staticmethod
    def draw(pinfo, scales, coordinates, ax, **params):
        pinfo['fill'] = make_rgba(pinfo['fill'],
                                  pinfo['alpha'])

        if pinfo['fill'] is None:
            pinfo['fill'] = pinfo['color']

        ax.scatter(x=pinfo['x'],
                   y=pinfo['y'],
                   facecolor=pinfo['fill'],
                   color=pinfo['color'],
                   marker=pinfo['shape'],
                   # Our size is in 'points' while
                   # scatter wants 'points^2'
                   s=np.square(pinfo['size']),
                   zorder=pinfo['zorder'],
                   alpha=pinfo['alpha'])

    @staticmethod
    def draw_legend(data, da, lyr):
        """
        Draw a point in the box

        Parameters
        ----------
        data : dataframe
        params : dict
        lyr : layer

        Returns
        -------
        out : DrawingArea
        """
        data.is_copy = None
        if data['fill'] is None:
            data['fill'] = data['color']
        key = mlines.Line2D([0.5*da.width],
                            [0.5*da.height],
                            alpha=data['alpha'],
                            marker=data['shape'],
                            markersize=data['size'],
                            markerfacecolor=data['fill'],
                            markeredgecolor=data['color'])
        da.add_artist(key)
        return da
