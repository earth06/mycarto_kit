# coding: utf-8

import cartopy.crs as ccrs
from cartopy.mpl.ticker import LatitudeFormatter,LongitudeFormatter
from cartopy.mpl.gridliner import LONGITUDE_FORMATTER, LATITUDE_FORMATTER
import cartopy.feature as cfeature
import numpy as np
import matplotlib.ticker as mticker
import matplotlib.path as mpath

def set_geogrid(ax,resolution='110m'
               ,dlon=60,dlat=30
               ,manual_ticks=False,xticks=None,yticks=None
               ,linewidth=0.5,fontsize=15,labelsize=15
               ,color='grey' ,alpha=0.8,linestyle='-' ):
    """
    parameter
    -------------
    ax        :cartopy.mpl.geoaxes
    dlon      :float  grid interval of longitude
    dlat      :float  grid interval of latitude
    linewidth,fontsize,labelsize,alpha :float
    color     :string
    return 
    -------------
    ax
    """
    ax.coastlines(resolution=resolution)
    gl = ax.gridlines(crs=ccrs.PlateCarree()
                      , draw_labels=False,
                      linewidth=linewidth, alpha=alpha
                      , color=color,linestyle=linestyle)
    if manual_ticks == False: 
        xticks=np.arange(0,360.1,dlon)
        yticks=np.arange(-90,90.1,dlat)
    gl.xlocator = mticker.FixedLocator(xticks)    
    gl.ylocator = mticker.FixedLocator(yticks)

    if (type(ax.projection)==type(ccrs.PlateCarree())): 
        ax.set_xticks(xticks,crs=ccrs.PlateCarree())
        ax.set_yticks(yticks,crs=ccrs.PlateCarree())
    
        latfmt=LatitudeFormatter()
        lonfmt=LongitudeFormatter(zero_direction_label=True)
        ax.xaxis.set_major_formatter(lonfmt)
        ax.yaxis.set_major_formatter(latfmt)
        ax.axes.tick_params(labelsize=labelsize)
    return ax
def set_feature(ax,scale='110m'):
    '''
    set LAND ,OCEAN,RIVERS,LAKES color
    parameter
    -----------
    ax    :cartopy.mpl.geoaxes
    return
    ----------
    ax    :as above
    '''
    ax.add_feature(cfeature.LAND.with_scale(scale))
    ax.add_feature(cfeature.OCEAN.with_scale(scale))
    ax.add_feature(cfeature.COASTLINE.with_scale(scale))
#    ax.add_feature(cfeature.BORDERS, linestyle=':')
    ax.add_feature(cfeature.LAKES.with_scale(scale), alpha=0.5)
    ax.add_feature(cfeature.RIVERS.with_scale(scale))
    return ax

def Polarmap(ax):
    """
    display cricular map
    this configure is available only in South and North Polar Stereo

    Parameter
    --------------
    ax     :cartopy.mpl.geoaxes
    """
    theta = np.linspace(0,2*np.pi,100)
    center,radius=[0.5,0.5],0.5
    verts=np.vstack([np.sin(theta),np.cos(theta)]).T
    circle=mpath.Path(verts*radius+center)

    ax.set_boundary(circle,transform=ax.transAxes)

    return ax
