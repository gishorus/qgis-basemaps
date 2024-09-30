
# This script is inspired by Klas Karlsson at https://bit.ly/4eDbx1O. Credit to Klas Karlsson.
# I expaned the script to include more basemaps from xyzservices


from qgis.PyQt.QtCore import QSettings
from qgis.utils import iface

sources = []
sources.append(['connections-xyz', 'OpenStreetMap', '', '', 'OpenStreetMap', 'https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', '', '30', '0'])
sources.append(['connections-xyz', 'Google Maps', '', '', 'Google', 'https://mt1.google.com/vt/lyrs=m&x={x}&y={y}&z={z}', '', '30', '0'])
sources.append(['connections-xyz', 'Google Satellite', '', '', 'Google', 'https://mt1.google.com/vt/lyrs=s&x={x}&y={y}&z={z}', '', '30', '0'])
sources.append(['connections-xyz', 'Google Terrain', '', '', 'Google', 'https://mt1.google.com/vt/lyrs=p&x={x}&y={y}&z={z}', '', '30', '0'])
sources.append(['connections-xyz', 'Google Hybrid', '', '', 'Google', 'https://mt1.google.com/vt/lyrs=y&x={x}&y={y}&z={z}', '', '30', '0'])
sources.append(['connections-xyz', 'BaseMapDE.Color', '', '', 'Map data: (C) dl-de/by-2-0', 'https://sgx.geodatenzentrum.de/wmts_basemapde/tile/1.0.0/de_basemapde_web_raster_farbe/default/GLOBAL_WEBMERCATOR/{z}/{y}/{x}.png', '', '30', '0'])
sources.append(['connections-xyz', 'BaseMapDE.Grey', '', '', 'Map data: (C) dl-de/by-2-0', 'https://sgx.geodatenzentrum.de/wmts_basemapde/tile/1.0.0/de_basemapde_web_raster_grau/default/GLOBAL_WEBMERCATOR/{z}/{y}/{x}.png', '', '30', '0'])
sources.append(['connections-xyz', 'CartoDB.DarkMatter', '', '', '(C) OpenStreetMap contributors (C) CARTO', 'https://a.basemaps.cartocdn.com/dark_all/{z}/{x}/{y}.png', '', '30', '0'])
sources.append(['connections-xyz', 'CartoDB.DarkMatterNoLabels', '', '', '(C) OpenStreetMap contributors (C) CARTO', 'https://a.basemaps.cartocdn.com/dark_nolabels/{z}/{x}/{y}.png', '', '30', '0'])
sources.append(['connections-xyz', 'CartoDB.DarkMatterOnlyLabels', '', '', '(C) OpenStreetMap contributors (C) CARTO', 'https://a.basemaps.cartocdn.com/dark_only_labels/{z}/{x}/{y}.png', '', '30', '0'])
sources.append(['connections-xyz', 'CartoDB.Positron', '', '', '(C) OpenStreetMap contributors (C) CARTO', 'https://a.basemaps.cartocdn.com/light_all/{z}/{x}/{y}.png', '', '30', '0'])
sources.append(['connections-xyz', 'CartoDB.PositronNoLabels', '', '', '(C) OpenStreetMap contributors (C) CARTO', 'https://a.basemaps.cartocdn.com/light_nolabels/{z}/{x}/{y}.png', '', '30', '0'])
sources.append(['connections-xyz', 'CartoDB.PositronOnlyLabels', '', '', '(C) OpenStreetMap contributors (C) CARTO', 'https://a.basemaps.cartocdn.com/light_only_labels/{z}/{x}/{y}.png', '', '30', '0'])
sources.append(['connections-xyz', 'CartoDB.Voyager', '', '', '(C) OpenStreetMap contributors (C) CARTO', 'https://a.basemaps.cartocdn.com/rastertiles/voyager/{z}/{x}/{y}.png', '', '30', '0'])
sources.append(['connections-xyz', 'CartoDB.VoyagerLabelsUnder', '', '', '(C) OpenStreetMap contributors (C) CARTO', 'https://a.basemaps.cartocdn.com/rastertiles/voyager_labels_under/{z}/{x}/{y}.png', '', '30', '0'])
sources.append(['connections-xyz', 'CartoDB.VoyagerNoLabels', '', '', '(C) OpenStreetMap contributors (C) CARTO', 'https://a.basemaps.cartocdn.com/rastertiles/voyager_nolabels/{z}/{x}/{y}.png', '', '30', '0'])
sources.append(['connections-xyz', 'CartoDB.VoyagerOnlyLabels', '', '', '(C) OpenStreetMap contributors (C) CARTO', 'https://a.basemaps.cartocdn.com/rastertiles/voyager_only_labels/{z}/{x}/{y}.png', '', '30', '0'])
sources.append(['connections-xyz', 'CyclOSM', '', '', 'CyclOSM | Map data: (C) OpenStreetMap contributors', 'https://a.tile-cyclosm.openstreetmap.fr/cyclosm/{z}/{x}/{y}.png', '', '30', '0'])
sources.append(['connections-xyz', 'Esri.AntarcticBasemap', '', '', 'Imagery provided by NOAA National Centers for Envi', 'https://tiles.arcgis.com/tiles/C8EMgrsFcRFL6LrL/arcgis/rest/services/Antarctic_Basemap/MapServer/tile/{z}/{y}/{x}', '', '30', '0'])
sources.append(['connections-xyz', 'Esri.AntarcticImagery', '', '', 'Earthstar Geographics', 'http://server.arcgisonline.com/ArcGIS/rest/services/Polar/Antarctic_Imagery/MapServer/tile/{z}/{y}/{x}', '', '30', '0'])
sources.append(['connections-xyz', 'Esri.ArcticImagery', '', '', 'Earthstar Geographics', 'http://server.arcgisonline.com/ArcGIS/rest/services/Polar/Arctic_Imagery/MapServer/tile/{z}/{y}/{x}', '', '30', '0'])
sources.append(['connections-xyz', 'Esri.ArcticOceanBase', '', '', 'Tiles &copy; Esri &mdash; Esri, DeLorme, NAVTEQ, T', 'http://server.arcgisonline.com/ArcGIS/rest/services/Polar/Arctic_Ocean_Base/MapServer/tile/{z}/{y}/{x}', '', '30', '0'])
sources.append(['connections-xyz', 'Esri.ArcticOceanReference', '', '', 'Tiles &copy; Esri &mdash; Esri, DeLorme, NAVTEQ, T', 'http://server.arcgisonline.com/ArcGIS/rest/services/Polar/Arctic_Ocean_Reference/MapServer/tile/{z}/{y}/{x}', '', '30', '0'])
sources.append(['connections-xyz', 'Esri.NatGeoWorldMap', '', '', 'Tiles (C) Esri -- National Geographic, Esri, DeLor', 'https://server.arcgisonline.com/ArcGIS/rest/services/NatGeo_World_Map/MapServer/tile/{z}/{y}/{x}', '', '30', '0'])
sources.append(['connections-xyz', 'Esri.OceanBasemap', '', '', 'Tiles (C) Esri -- Sources: GEBCO, NOAA, CHS, OSU, ', 'https://server.arcgisonline.com/ArcGIS/rest/services/Ocean/World_Ocean_Base/MapServer/tile/{z}/{y}/{x}', '', '30', '0'])
sources.append(['connections-xyz', 'Esri.WorldGrayCanvas', '', '', 'Tiles (C) Esri -- Esri, DeLorme, NAVTEQ', 'https://server.arcgisonline.com/ArcGIS/rest/services/Canvas/World_Light_Gray_Base/MapServer/tile/{z}/{y}/{x}', '', '30', '0'])
sources.append(['connections-xyz', 'Esri.WorldImagery', '', '', 'Tiles (C) Esri -- Source: Esri, i-cubed, USDA, USG', 'https://server.arcgisonline.com/ArcGIS/rest/services/World_Imagery/MapServer/tile/{z}/{y}/{x}', '', '30', '0'])
sources.append(['connections-xyz', 'Esri.WorldPhysical', '', '', 'Tiles (C) Esri -- Source: US National Park Service', 'https://server.arcgisonline.com/ArcGIS/rest/services/World_Physical_Map/MapServer/tile/{z}/{y}/{x}', '', '30', '0'])
sources.append(['connections-xyz', 'Esri.WorldShadedRelief', '', '', 'Tiles (C) Esri -- Source: Esri', 'https://server.arcgisonline.com/ArcGIS/rest/services/World_Shaded_Relief/MapServer/tile/{z}/{y}/{x}', '', '30', '0'])
sources.append(['connections-xyz', 'Esri.WorldStreetMap', '', '', 'Tiles (C) Esri -- Source: Esri, DeLorme, NAVTEQ, U', 'https://server.arcgisonline.com/ArcGIS/rest/services/World_Street_Map/MapServer/tile/{z}/{y}/{x}', '', '30', '0'])
sources.append(['connections-xyz', 'Esri.WorldTerrain', '', '', 'Tiles (C) Esri -- Source: USGS, Esri, TANA, DeLorm', 'https://server.arcgisonline.com/ArcGIS/rest/services/World_Terrain_Base/MapServer/tile/{z}/{y}/{x}', '', '30', '0'])
sources.append(['connections-xyz', 'Esri.WorldTopoMap', '', '', 'Tiles (C) Esri -- Esri, DeLorme, NAVTEQ, TomTom, I', 'https://server.arcgisonline.com/ArcGIS/rest/services/World_Topo_Map/MapServer/tile/{z}/{y}/{x}', '', '30', '0'])
sources.append(['connections-xyz', 'FreeMapSK', '', '', '(C) OpenStreetMap contributors, visualization CC-B', 'https://a.freemap.sk/T/{z}/{x}/{y}.jpeg', '', '30', '0'])
sources.append(['connections-xyz', 'Gaode.Normal', '', '', '&copy; <a href="http://www.gaode.com/">Gaode.com</', 'http://webrd01.is.autonavi.com/appmaptile?lang=zh_cn&size=1&scale=1&style=7&x={x}&y={y}&z={z}', '', '30', '0'])
sources.append(['connections-xyz', 'Gaode.Satellite', '', '', '&copy; <a href="http://www.gaode.com/">Gaode.com</', 'http://webst01.is.autonavi.com/appmaptile?style=6&x={x}&y={y}&z={z}', '', '30', '0'])
sources.append(['connections-xyz', 'HikeBike.HikeBike', '', '', '(C) OpenStreetMap contributors', 'https://tiles.wmflabs.org/hikebike/{z}/{x}/{y}.png', '', '30', '0'])
sources.append(['connections-xyz', 'HikeBike.HillShading', '', '', '(C) OpenStreetMap contributors', 'https://tiles.wmflabs.org/hillshading/{z}/{x}/{y}.png', '', '30', '0'])
sources.append(['connections-xyz', 'JusticeMap.americanIndian', '', '', 'Justice Map', 'https://www.justicemap.org/tile/county/indian/{z}/{x}/{y}.png', '', '30', '0'])
sources.append(['connections-xyz', 'JusticeMap.asian', '', '', 'Justice Map', 'https://www.justicemap.org/tile/county/asian/{z}/{x}/{y}.png', '', '30', '0'])
sources.append(['connections-xyz', 'JusticeMap.black', '', '', 'Justice Map', 'https://www.justicemap.org/tile/county/black/{z}/{x}/{y}.png', '', '30', '0'])
sources.append(['connections-xyz', 'JusticeMap.hispanic', '', '', 'Justice Map', 'https://www.justicemap.org/tile/county/hispanic/{z}/{x}/{y}.png', '', '30', '0'])
sources.append(['connections-xyz', 'JusticeMap.income', '', '', 'Justice Map', 'https://www.justicemap.org/tile/county/income/{z}/{x}/{y}.png', '', '30', '0'])
sources.append(['connections-xyz', 'JusticeMap.multi', '', '', 'Justice Map', 'https://www.justicemap.org/tile/county/multi/{z}/{x}/{y}.png', '', '30', '0'])
sources.append(['connections-xyz', 'JusticeMap.nonWhite', '', '', 'Justice Map', 'https://www.justicemap.org/tile/county/nonwhite/{z}/{x}/{y}.png', '', '30', '0'])
sources.append(['connections-xyz', 'JusticeMap.plurality', '', '', 'Justice Map', 'https://www.justicemap.org/tile/county/plural/{z}/{x}/{y}.png', '', '30', '0'])
sources.append(['connections-xyz', 'JusticeMap.white', '', '', 'Justice Map', 'https://www.justicemap.org/tile/county/white/{z}/{x}/{y}.png', '', '30', '0'])
sources.append(['connections-xyz', 'MtbMap', '', '', '(C) OpenStreetMap contributors & USGS', 'http://tile.mtbmap.cz/mtbmap_tiles/{z}/{x}/{y}.png', '', '30', '0'])
sources.append(['connections-xyz', 'NASAGIBS.ASTER_GDEM_Greyscale_Shaded_Relief', '', '', 'Imagery provided by services from the Global Image', 'https://gibs.earthdata.nasa.gov/wmts/epsg3857/best/ASTER_GDEM_Greyscale_Shaded_Relief/default/GoogleMapsCompatible_Level12/{z}/{y}/{x}.jpg', '', '30', '0'])
sources.append(['connections-xyz', 'NASAGIBS.BlueMarble', '', '', 'Imagery provided by services from the Global Image', 'https://gibs.earthdata.nasa.gov/wmts/epsg3857/best/BlueMarble_NextGeneration/default/GoogleMapsCompatible_Level8/{z}/{y}/{x}.jpeg', '', '30', '0'])
sources.append(['connections-xyz', 'NASAGIBS.BlueMarble3031', '', '', 'Imagery provided by services from the Global Image', 'https://gibs.earthdata.nasa.gov/wmts/epsg3031/best/BlueMarble_NextGeneration/default/500m/{z}/{y}/{x}.jpeg', '', '30', '0'])
sources.append(['connections-xyz', 'NASAGIBS.BlueMarble3413', '', '', 'Imagery provided by services from the Global Image', 'https://gibs.earthdata.nasa.gov/wmts/epsg3413/best/BlueMarble_NextGeneration/default/500m/{z}/{y}/{x}.jpeg', '', '30', '0'])
sources.append(['connections-xyz', 'NASAGIBS.BlueMarbleBathymetry3031', '', '', 'Imagery provided by services from the Global Image', 'https://gibs.earthdata.nasa.gov/wmts/epsg3031/best/BlueMarble_ShadedRelief_Bathymetry/default/500m/{z}/{y}/{x}.jpeg', '', '30', '0'])
sources.append(['connections-xyz', 'NASAGIBS.BlueMarbleBathymetry3413', '', '', 'Imagery provided by services from the Global Image', 'https://gibs.earthdata.nasa.gov/wmts/epsg3413/best/BlueMarble_ShadedRelief_Bathymetry/default/500m/{z}/{y}/{x}.jpeg', '', '30', '0'])
sources.append(['connections-xyz', 'NASAGIBS.MEaSUREsIceVelocity3031', '', '', 'Imagery provided by services from the Global Image', 'https://gibs.earthdata.nasa.gov/wmts/epsg3031/best/MEaSUREs_Ice_Velocity_Antarctica/default/500m/{z}/{y}/{x}', '', '30', '0'])
sources.append(['connections-xyz', 'NASAGIBS.MEaSUREsIceVelocity3413', '', '', 'Imagery provided by services from the Global Image', 'https://gibs.earthdata.nasa.gov/wmts/epsg3413/best/MEaSUREs_Ice_Velocity_Greenland/default/500m/{z}/{y}/{x}', '', '30', '0'])
sources.append(['connections-xyz', 'NASAGIBS.ModisAquaBands721CR', '', '', 'Imagery provided by services from the Global Image', 'https://gibs.earthdata.nasa.gov/wmts/epsg3857/best/MODIS_Aqua_CorrectedReflectance_Bands721/default//GoogleMapsCompatible_Level9/{z}/{y}/{x}.jpg', '', '30', '0'])
sources.append(['connections-xyz', 'NASAGIBS.ModisAquaTrueColorCR', '', '', 'Imagery provided by services from the Global Image', 'https://gibs.earthdata.nasa.gov/wmts/epsg3857/best/MODIS_Aqua_CorrectedReflectance_TrueColor/default//GoogleMapsCompatible_Level9/{z}/{y}/{x}.jpg', '', '30', '0'])
sources.append(['connections-xyz', 'NASAGIBS.ModisTerraAOD', '', '', 'Imagery provided by services from the Global Image', 'https://map1.vis.earthdata.nasa.gov/wmts-webmerc/MODIS_Terra_Aerosol/default//GoogleMapsCompatible_Level6/{z}/{y}/{x}.png', '', '30', '0'])
sources.append(['connections-xyz', 'NASAGIBS.ModisTerraBands367CR', '', '', 'Imagery provided by services from the Global Image', 'https://map1.vis.earthdata.nasa.gov/wmts-webmerc/MODIS_Terra_CorrectedReflectance_Bands367/default//GoogleMapsCompatible_Level9/{z}/{y}/{x}.jpg', '', '30', '0'])
sources.append(['connections-xyz', 'NASAGIBS.ModisTerraBands721CR', '', '', 'Imagery provided by services from the Global Image', 'https://gibs.earthdata.nasa.gov/wmts/epsg3857/best/MODIS_Terra_CorrectedReflectance_Bands721/default//GoogleMapsCompatible_Level9/{z}/{y}/{x}.jpg', '', '30', '0'])
sources.append(['connections-xyz', 'NASAGIBS.ModisTerraChlorophyll', '', '', 'Imagery provided by services from the Global Image', 'https://map1.vis.earthdata.nasa.gov/wmts-webmerc/MODIS_Terra_L2_Chlorophyll_A/default//GoogleMapsCompatible_Level7/{z}/{y}/{x}.png', '', '30', '0'])
sources.append(['connections-xyz', 'NASAGIBS.ModisTerraLSTDay', '', '', 'Imagery provided by services from the Global Image', 'https://map1.vis.earthdata.nasa.gov/wmts-webmerc/MODIS_Terra_Land_Surface_Temp_Day/default//GoogleMapsCompatible_Level7/{z}/{y}/{x}.png', '', '30', '0'])
sources.append(['connections-xyz', 'NASAGIBS.ModisTerraSnowCover', '', '', 'Imagery provided by services from the Global Image', 'https://map1.vis.earthdata.nasa.gov/wmts-webmerc/MODIS_Terra_NDSI_Snow_Cover/default//GoogleMapsCompatible_Level8/{z}/{y}/{x}.png', '', '30', '0'])
sources.append(['connections-xyz', 'NASAGIBS.ModisTerraTrueColorCR', '', '', 'Imagery provided by services from the Global Image', 'https://map1.vis.earthdata.nasa.gov/wmts-webmerc/MODIS_Terra_CorrectedReflectance_TrueColor/default//GoogleMapsCompatible_Level9/{z}/{y}/{x}.jpg', '', '30', '0'])
sources.append(['connections-xyz', 'NASAGIBS.ViirsEarthAtNight2012', '', '', 'Imagery provided by services from the Global Image', 'https://map1.vis.earthdata.nasa.gov/wmts-webmerc/VIIRS_CityLights_2012/default//GoogleMapsCompatible_Level8/{z}/{y}/{x}.jpg', '', '30', '0'])
sources.append(['connections-xyz', 'NASAGIBS.ViirsTrueColorCR', '', '', 'Imagery provided by services from the Global Image', 'https://gibs.earthdata.nasa.gov/wmts/epsg3857/best/VIIRS_SNPP_CorrectedReflectance_TrueColor/default//GoogleMapsCompatible_Level9/{z}/{y}/{x}.jpg', '', '30', '0'])
sources.append(['connections-xyz', 'OPNVKarte', '', '', 'Map memomaps.de CC-BY-SA, map data (C) OpenStreetM', 'https://tileserver.memomaps.de/tilegen/{z}/{x}/{y}.png', '', '30', '0'])
sources.append(['connections-xyz', 'OneMapSG.Default', '', '', '![](https://docs.onemap.sg/maps/images/oneMap64-01', 'https://maps-a.onemap.sg/v3/Default/{z}/{x}/{y}.png', '', '30', '0'])
sources.append(['connections-xyz', 'OneMapSG.Grey', '', '', '![](https://docs.onemap.sg/maps/images/oneMap64-01', 'https://maps-a.onemap.sg/v3/Grey/{z}/{x}/{y}.png', '', '30', '0'])
sources.append(['connections-xyz', 'OneMapSG.LandLot', '', '', '![](https://docs.onemap.sg/maps/images/oneMap64-01', 'https://maps-a.onemap.sg/v3/LandLot/{z}/{x}/{y}.png', '', '30', '0'])
sources.append(['connections-xyz', 'OneMapSG.Night', '', '', '![](https://docs.onemap.sg/maps/images/oneMap64-01', 'https://maps-a.onemap.sg/v3/Night/{z}/{x}/{y}.png', '', '30', '0'])
sources.append(['connections-xyz', 'OneMapSG.Original', '', '', '![](https://docs.onemap.sg/maps/images/oneMap64-01', 'https://maps-a.onemap.sg/v3/Original/{z}/{x}/{y}.png', '', '30', '0'])
sources.append(['connections-xyz', 'OpenAIP', '', '', 'openAIP Data (CC-BY-NC-SA)', 'https://1.tile.maps.openaip.net/geowebcache/service/tms/1.0.0/openaip_basemap@EPSG%3A900913@png/{z}/{x}/{y}.png', '', '30', '0'])
sources.append(['connections-xyz', 'OpenFireMap', '', '', 'Map data: (C) OpenStreetMap contributors | Map sty', 'http://openfiremap.org/hytiles/{z}/{x}/{y}.png', '', '30', '0'])
sources.append(['connections-xyz', 'OpenRailwayMap', '', '', 'Map data: (C) OpenStreetMap contributors | Map sty', 'https://a.tiles.openrailwaymap.org/standard/{z}/{x}/{y}.png', '', '30', '0'])
sources.append(['connections-xyz', 'OpenSeaMap', '', '', 'Map data: (C) OpenSeaMap contributors', 'https://tiles.openseamap.org/seamark/{z}/{x}/{y}.png', '', '30', '0'])
sources.append(['connections-xyz', 'OpenSnowMap.pistes', '', '', 'Map data: (C) OpenStreetMap contributors & ODbL, (', 'https://tiles.opensnowmap.org/pistes/{z}/{x}/{y}.png', '', '30', '0'])
sources.append(['connections-xyz', 'OpenStreetMap.BZH', '', '', '(C) OpenStreetMap contributors, Tiles courtesy of ', 'https://tile.openstreetmap.bzh/br/{z}/{x}/{y}.png', '', '30', '0'])
sources.append(['connections-xyz', 'OpenStreetMap.BlackAndWhite', '', '', '(C) OpenStreetMap contributors', 'http://a.tiles.wmflabs.org/bw-mapnik/{z}/{x}/{y}.png', '', '30', '0'])
sources.append(['connections-xyz', 'OpenStreetMap.CH', '', '', '(C) OpenStreetMap contributors', 'https://tile.osm.ch/switzerland/{z}/{x}/{y}.png', '', '30', '0'])
sources.append(['connections-xyz', 'OpenStreetMap.DE', '', '', '(C) OpenStreetMap contributors', 'https://tile.openstreetmap.de/{z}/{x}/{y}.png', '', '30', '0'])
sources.append(['connections-xyz', 'OpenStreetMap.HOT', '', '', '(C) OpenStreetMap contributors, Tiles style by Hum', 'https://a.tile.openstreetmap.fr/hot/{z}/{x}/{y}.png', '', '30', '0'])
sources.append(['connections-xyz', 'OpenStreetMap.Mapnik', '', '', '(C) OpenStreetMap contributors', 'https://tile.openstreetmap.org/{z}/{x}/{y}.png', '', '30', '0'])
sources.append(['connections-xyz', 'OpenTopoMap', '', '', 'Map data: (C) OpenStreetMap contributors, SRTM | M', 'https://a.tile.opentopomap.org/{z}/{x}/{y}.png', '', '30', '0'])
sources.append(['connections-xyz', 'SafeCast', '', '', 'Map data: (C) OpenStreetMap contributors | Map sty', 'https://s3.amazonaws.com/te512.safecast.org/{z}/{x}/{y}.png', '', '30', '0'])
sources.append(['connections-xyz', 'Strava.All', '', '', 'Map tiles by <a href="https://labs.strava.com/heat', 'https://heatmap-external-a.strava.com/tiles/all/hot/{z}/{x}/{y}.png', '', '30', '0'])
sources.append(['connections-xyz', 'Strava.Ride', '', '', 'Map tiles by <a href="https://labs.strava.com/heat', 'https://heatmap-external-a.strava.com/tiles/ride/hot/{z}/{x}/{y}.png', '', '30', '0'])
sources.append(['connections-xyz', 'Strava.Run', '', '', 'Map tiles by <a href="https://labs.strava.com/heat', 'https://heatmap-external-a.strava.com/tiles/run/bluered/{z}/{x}/{y}.png', '', '30', '0'])
sources.append(['connections-xyz', 'Strava.Water', '', '', 'Map tiles by <a href="https://labs.strava.com/heat', 'https://heatmap-external-a.strava.com/tiles/water/blue/{z}/{x}/{y}.png', '', '30', '0'])
sources.append(['connections-xyz', 'Strava.Winter', '', '', 'Map tiles by <a href="https://labs.strava.com/heat', 'https://heatmap-external-a.strava.com/tiles/winter/hot/{z}/{x}/{y}.png', '', '30', '0'])
sources.append(['connections-xyz', 'SwissFederalGeoportal.JourneyThroughTime', '', '', '© swisstopo', 'https://wmts.geo.admin.ch/1.0.0/ch.swisstopo.zeitreihen/default/18641231/3857/{z}/{x}/{y}.png', '', '30', '0'])
sources.append(['connections-xyz', 'SwissFederalGeoportal.NationalMapColor', '', '', '© swisstopo', 'https://wmts.geo.admin.ch/1.0.0/ch.swisstopo.pixelkarte-farbe/default/current/3857/{z}/{x}/{y}.jpeg', '', '30', '0'])
sources.append(['connections-xyz', 'SwissFederalGeoportal.NationalMapGrey', '', '', '© swisstopo', 'https://wmts.geo.admin.ch/1.0.0/ch.swisstopo.pixelkarte-grau/default/current/3857/{z}/{x}/{y}.jpeg', '', '30', '0'])
sources.append(['connections-xyz', 'SwissFederalGeoportal.SWISSIMAGE', '', '', '© swisstopo', 'https://wmts.geo.admin.ch/1.0.0/ch.swisstopo.swissimage/default/current/3857/{z}/{x}/{y}.jpeg', '', '30', '0'])
sources.append(['connections-xyz', 'TopPlusOpen.Color', '', '', 'Map data: (C) dl-de/by-2-0', 'http://sgx.geodatenzentrum.de/wmts_topplus_open/tile/1.0.0/web/default/WEBMERCATOR/{z}/{y}/{x}.png', '', '30', '0'])
sources.append(['connections-xyz', 'TopPlusOpen.Grey', '', '', 'Map data: (C) dl-de/by-2-0', 'http://sgx.geodatenzentrum.de/wmts_topplus_open/tile/1.0.0/web_grau/default/WEBMERCATOR/{z}/{y}/{x}.png', '', '30', '0'])
sources.append(['connections-xyz', 'USGS.USImagery', '', '', 'Tiles courtesy of the U.S. Geological Survey', 'https://basemap.nationalmap.gov/arcgis/rest/services/USGSImageryOnly/MapServer/tile/{z}/{y}/{x}', '', '30', '0'])
sources.append(['connections-xyz', 'USGS.USImageryTopo', '', '', 'Tiles courtesy of the U.S. Geological Survey', 'https://basemap.nationalmap.gov/arcgis/rest/services/USGSImageryTopo/MapServer/tile/{z}/{y}/{x}', '', '30', '0'])
sources.append(['connections-xyz', 'USGS.USTopo', '', '', 'Tiles courtesy of the U.S. Geological Survey', 'https://basemap.nationalmap.gov/arcgis/rest/services/USGSTopo/MapServer/tile/{z}/{y}/{x}', '', '30', '0'])
sources.append(['connections-xyz', 'WaymarkedTrails.cycling', '', '', 'Map data: (C) OpenStreetMap contributors | Map sty', 'https://tile.waymarkedtrails.org/cycling/{z}/{x}/{y}.png', '', '30', '0'])
sources.append(['connections-xyz', 'WaymarkedTrails.hiking', '', '', 'Map data: (C) OpenStreetMap contributors | Map sty', 'https://tile.waymarkedtrails.org/hiking/{z}/{x}/{y}.png', '', '30', '0'])
sources.append(['connections-xyz', 'WaymarkedTrails.mtb', '', '', 'Map data: (C) OpenStreetMap contributors | Map sty', 'https://tile.waymarkedtrails.org/mtb/{z}/{x}/{y}.png', '', '30', '0'])
sources.append(['connections-xyz', 'WaymarkedTrails.riding', '', '', 'Map data: (C) OpenStreetMap contributors | Map sty', 'https://tile.waymarkedtrails.org/riding/{z}/{x}/{y}.png', '', '30', '0'])
sources.append(['connections-xyz', 'WaymarkedTrails.skating', '', '', 'Map data: (C) OpenStreetMap contributors | Map sty', 'https://tile.waymarkedtrails.org/skating/{z}/{x}/{y}.png', '', '30', '0'])
sources.append(['connections-xyz', 'WaymarkedTrails.slopes', '', '', 'Map data: (C) OpenStreetMap contributors | Map sty', 'https://tile.waymarkedtrails.org/slopes/{z}/{x}/{y}.png', '', '30', '0'])
sources.append(['connections-xyz', 'nlmaps.grijs', '', '', 'Kaartgegevens (C) Kadaster', 'https://service.pdok.nl/brt/achtergrondkaart/wmts/v2_0/grijs/EPSG:3857/{z}/{x}/{y}.png', '', '30', '0'])
sources.append(['connections-xyz', 'nlmaps.luchtfoto', '', '', 'Kaartgegevens (C) Kadaster', 'https://service.pdok.nl/hwh/luchtfotorgb/wmts/v1_0/Actueel_ortho25/EPSG:3857/{z}/{x}/{y}.jpeg', '', '30', '0'])
sources.append(['connections-xyz', 'nlmaps.pastel', '', '', 'Kaartgegevens (C) Kadaster', 'https://service.pdok.nl/brt/achtergrondkaart/wmts/v2_0/pastel/EPSG:3857/{z}/{x}/{y}.png', '', '30', '0'])
sources.append(['connections-xyz', 'nlmaps.standaard', '', '', 'Kaartgegevens (C) Kadaster', 'https://service.pdok.nl/brt/achtergrondkaart/wmts/v2_0/standaard/EPSG:3857/{z}/{x}/{y}.png', '', '30', '0'])
sources.append(['connections-xyz', 'nlmaps.water', '', '', 'Kaartgegevens (C) Kadaster', 'https://service.pdok.nl/brt/achtergrondkaart/wmts/v2_0/water/EPSG:3857/{z}/{x}/{y}.png', '', '30', '0'])
sources.append(['connections-xyz', 'Bing VirtualEarth', '', '', 'Microsoft', 'http://ecn.t3.tiles.virtualearth.net/tiles/a{q}.jpeg?g=1', '', '30', '1'])

for source in sources:
    connectionType = source[0]
    connectionName = source[1]
    
    QSettings().setValue(f"qgis/{connectionType}/{connectionName}/authcfg", source[2])
    QSettings().setValue(f"qgis/{connectionType}/{connectionName}/password", source[3])
    QSettings().setValue(f"qgis/{connectionType}/{connectionName}/referer", source[4])
    QSettings().setValue(f"qgis/{connectionType}/{connectionName}/url", source[5])
    QSettings().setValue(f"qgis/{connectionType}/{connectionName}/username", source[6])
    QSettings().setValue(f"qgis/{connectionType}/{connectionName}/zmax", source[7])
    QSettings().setValue(f"qgis/{connectionType}/{connectionName}/zmin", source[8])

iface.reloadConnections()
