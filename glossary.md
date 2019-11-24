alert
Data Type
String
Typical Values
“green”, “yellow”, “orange”, “red”.
Description
The alert level from the PAGER earthquake impact scale.

cdi
Data Type
Decimal
Typical Values
[0.0, 10.0]
Description
The maximum reported intensity for the event. Computed by DYFI. While typically reported as a roman numeral, for the purposes of this API, intensity is expected as the decimal equivalent of the roman numeral. Learn more about magnitude vs. intensity.

code
Data Type
String
Typical Values
"2013lgaz", "c000f1jy", "71935551"
Description
An identifying code assigned by - and unique from - the corresponding source for the event.

depth
Data Type
Decimal
Typical Values
[0, 1000]
Description
Depth of the event in kilometers.
Additional Information
The depth where the earthquake begins to rupture. This depth may be relative to the WGS84 geoid, mean sea-level, or the average elevation of the seismic stations which provided arrival-time data for the earthquake location. The choice of reference depth is dependent on the method used to locate the earthquake, which varies by seismic network. Since ComCat includes data from many different seismic networks, the process for determining the depth is different for different events. The depth is the least-constrained parameter in the earthquake location, and the error bars are generally larger than the variation due to different depth determination methods.

Sometimes when depth is poorly constrained by available seismic data, the location program will set the depth at a fixed value. For example, 33 km is often used as a default depth for earthquakes determined to be shallow, but whose depth is not satisfactorily determined by the data, whereas default depths of 5 or 10 km are often used in mid-continental areas and on mid-ocean ridges since earthquakes in these areas are usually shallower than 33 km.

depthError
Data Type
Decimal
Typical Values
[0, 100]
Description
Uncertainty of reported depth of the event in kilometers.
Additional Information
The depth error, in km, defined as the largest projection of the three principal errors on a vertical line.

detail
Data Type
String
Description
Link to GeoJSON detail feed from a GeoJSON summary feed.
NOTE: When searching and using geojson with callback, no callback is included in the detail url.

dmin
Data Type
Decimal
Typical Values
[0.4, 7.1]
Description
Horizontal distance from the epicenter to the nearest station (in degrees). 1 degree is approximately 111.2 kilometers. In general, the smaller this number, the more reliable is the calculated depth of the earthquake.

felt
Data Type
Integer
Typical Values
[44, 843]
Description
The total number of felt reports submitted to the DYFI? system.

gap
Data Type
Decimal
Typical Values
[0.0, 180.0]
Description
The largest azimuthal gap between azimuthally adjacent stations (in degrees). In general, the smaller this number, the more reliable is the calculated horizontal position of the earthquake. Earthquake locations in which the azimuthal gap exceeds 180 degrees typically have large location and depth uncertainties.

horizontalError
Data Type
Decimal
Typical Values
[0, 100]
Description
Uncertainty of reported location of the event in kilometers.
Additional Information
The horizontal location error, in km, defined as the length of the largest projection of the three principal errors on a horizontal plane. The principal errors are the major axes of the error ellipsoid, and are mutually perpendicular. The horizontal and vertical uncertainties in an event's location varies from about 100 m horizontally and 300 meters vertically for the best located events, those in the middle of densely spaced seismograph networks, to 10s of kilometers for global events in many parts of the world. We report an "unknown" value if the contributing seismic network does not supply uncertainty estimates.

id
Data Type
String
Typical Values
A (generally) two-character network identifier with a (generally) eight-character network-assigned code.
Description
A unique identifier for the event. This is the current preferred id for the event, and may change over time. See the "ids" GeoJSON format property.

ids
Data Type
String
Typical Values
",ci15296281,us2013mqbd,at00mji9pf,"
Description
A comma-separated list of event ids that are associated to an event.

latitude
Data Type
Decimal
Typical Values
[-90.0, 90.0]
Description
Decimal degrees latitude. Negative values for southern latitudes.
Additional Information
An earthquake begins to rupture at a hypocenter which is defined by a position on the surface of the earth (epicenter) and a depth below this point (focal depth). We provide the coordinates of the epicenter in units of latitude and longitude. The latitude is the number of degrees north (N) or south (S) of the equator and varies from 0 at the equator to 90 at the poles. The longitude is the number of degrees east (E) or west (W) of the prime meridian which runs through Greenwich, England. The longitude varies from 0 at Greenwich to 180 and the E or W shows the direction from Greenwich. Coordinates are given in the WGS84 reference frame. The position uncertainty of the hypocenter location varies from about 100 m horizontally and 300 meters vertically for the best located events, those in the middle of densely spaced seismograph networks, to 10s of kilometers for global events in many parts of the world.

locationSource
Data Type
String
Typical Values
ak, at, ci, hv, ld, mb, nc, nm, nn, pr, pt, se, us, uu, uw
Description
The network that originally authored the reported location of this event.

longitude
Data Type
Decimal
Typical Values
[-180.0, 180.0]
Description
Decimal degrees longitude. Negative values for western longitudes.
Additional Information
An earthquake begins to rupture at a hypocenter which is defined by a position on the surface of the earth (epicenter) and a depth below this point (focal depth). We provide the coordinates of the epicenter in units of latitude and longitude. The latitude is the number of degrees north (N) or south (S) of the equator and varies from 0 at the equator to 90 at the poles. The longitude is the number of degrees east (E) or west (W) of the prime meridian which runs through Greenwich, England. The longitude varies from 0 at Greenwich to 180 and the E or W shows the direction from Greenwich. Coordinates are given in the WGS84 reference frame. The position uncertainty of the hypocenter location varies from about 100 m horizontally and 300 meters vertically for the best located events, those in the middle of densely spaced seismograph networks, to 10s of kilometers for global events in many parts of the world.

mag
Data Type
Decimal
Typical Values
[-1.0, 10.0]
Description
The magnitude for the event. See also magType.
Additional Information
The magnitude reported is that which the U.S. Geological Survey considers official for this earthquake, and was the best available estimate of the earthquake’s size, at the time that this page was created. Other magnitudes associated with web pages linked from here are those determined at various times following the earthquake with different types of seismic data. Although they are legitimate estimates of magnitude, the U.S. Geological Survey does not consider them to be the preferred "official" magnitude for the event.

Earthquake magnitude is a measure of the size of an earthquake at its source. It is a logarithmic measure. At the same distance from the earthquake, the amplitude of the seismic waves from which the magnitude is determined are approximately 10 times as large during a magnitude 5 earthquake as during a magnitude 4 earthquake. The total amount of energy released by the earthquake usually goes up by a larger factor: for many commonly used magnitude types, the total energy of an average earthquake goes up by a factor of approximately 32 for each unit increase in magnitude.

There are various ways that magnitude may be calculated from seismograms. Different methods are effective for different sizes of earthquakes and different distances between the earthquake source and the recording station. The various magnitude types are generally defined so as to yield magnitude values that agree to within a few-tenths of a magnitude-unit for earthquakes in a middle range of recorded-earthquake sizes, but the various magnitude-types may have values that differ by more than a magnitude-unit for very large and very small earthquakes as well as for some specific classes of seismic source. This is because earthquakes are commonly complex events that release energy over a wide range of frequencies and at varying amounts as the faulting or rupture process occurs. The various types of magnitude measure different aspects of the seismic radiation (e.g., low-frequency energy vs. high-frequency energy). The relationship among values of different magnitude types that are assigned to a particular seismic event may enable the seismologist to better understand the processes at the focus of the seismic event. The various magnitude-types are not all available at the same time for a particular earthquake.

Preliminary magnitudes based on incomplete but rapidly-available data are sometimes estimated and reported. For example, the Tsunami Warning Centers will calculate a preliminary magnitude and location for an event as soon as sufficient data are available to make an estimate. In this case, time is of the essence in order to broadcast a warning if tsunami waves are likely to be generated by the event. Such preliminary magnitudes are superseded by improved estimates of magnitude as more data become available.

For large earthquakes of the present era, the magnitude that is ultimately selected as the preferred magnitude for reporting to the public is commonly a moment magnitude that is based on the scalar seismic-moment of an earthquake determined by calculation of the seismic moment-tensor that best accounts for the character of the seismic waves generated by the earthquake. The scalar seismic-moment, a parameter of the seismic moment-tensor, can also be estimated via the multiplicative product rigidity of faulted rock x area of fault rupture x average fault displacement during the earthquake.

magError
Data Type
Decimal
Typical Values
[0, 100]
Description
Uncertainty of reported magnitude of the event. The estimated standard error of the magnitude. The uncertainty corresponds to the specific magnitude type being reported and does not take into account magnitude variations and biases between different magnitude scales. We report an "unknown" value if the contributing seismic network does not supply uncertainty estimates.

magNst
Data Type
Integer
Description
The total number of seismic stations used to calculate the magnitude for this earthquake.

magSource
Data Type
String
Typical Values
ak, at, ci, hv, ld, mb, nc, nm, nn, pr, pt, se, us, uu, uw
Description
Network that originally authored the reported magnitude for this event.

magType
Data Type
String
Typical Values
“Md”, “Ml”, “Ms”, “Mw”, “Me”, “Mi”, “Mb”, “MLg”
Description
The method or algorithm used to calculate the preferred magnitude for the event.
Additional Information
See Magnitude Types Table.

mmi
Data Type
Decimal
Typical Values
[0.0, 10.0]
Description
The maximum estimated instrumental intensity for the event. Computed by ShakeMap. While typically reported as a roman numeral, for the purposes of this API, intensity is expected as the decimal equivalent of the roman numeral. Learn more about magnitude vs. intensity.

net
Data Type
String
Typical Values
ak, at, ci, hv, ld, mb, nc, nm, nn, pr, pt, se, us, uu, uw
Description
The ID of a data contributor. Identifies the network considered to be the preferred source of information for this event.

nph
Number of Phases Used
String
Description
Number of P and S arrival-time observations used to compute the hypocenter location. Increased numbers of arrival-time observations generally result in improved earthquake locations.

nst
Data Type
Integer
Description
The total number of seismic stations used to determine earthquake location.
Additional Information
Number of seismic stations which reported P- and S-arrival times for this earthquake. This number may be larger than the Number of Phases Used if arrival times are rejected because the distance to a seismic station exceeds the maximum allowable distance or because the arrival-time observation is inconsistent with the solution.

place
Data Type
String
Description
Textual description of named geographic region near to the event. This may be a city name, or a Flinn-Engdahl Region name.
Additional Information
We use a GeoNames dataset to reference populated places that are in close proximity to a seismic event. GeoNames has compiled a list of cities in the United States where the population is 1,000 or greater (cities1000.txt). This is the primary list that we use when selecting nearby places. In order to provide the public with a better understanding for the location of an event we try to list a variety of places in our nearby places list. This includes the closest known populated place in relation to the seismic event (which based on our dataset will have a population of 1,000 or greater). We also include the next 3 closest places that have a population of 10,000 or greater, and finally make sure to include the closest capital city to the seismic event.

The reference point for the descriptive locations is usually either the City Hall of the town (or prominent intersection in the middle of town if there is no City Hall), but please refer to the GeoNames website for the most accurate information on their data.

If there is no nearby city within 300 kilometers (or if the nearby cities database is unavailable for some reason), the Flinn-Engdahl (F-E) seismic and geographical regionalization scheme is used. The boundaries of these regions are defined at one-degree intervals and therefore differ from irregular political boundaries. For example, F-E region 545 (Northern Italy) also includes small parts of France, Switzerland, Austria and Slovenia and F-E region 493 (Chesapeake Bay Region) includes all of the State of Delaware, plus parts of the District of Columbia, Maryland, New Jersey, Pennsylvania and Virginia. Beginning with January 2000, the 1995 revision to the F-E code has been used in the QED and PDE listings.

As an agency of the U.S. Government, we are expected to use the names and spellings approved by the U.S. Board on Geographic Names. Any requests to approve additional names should be made to the U.S. Board on Geographic Names.

rms
Data Type
Decimal
Typical Values
[0.13,1.39]
Description
The root-mean-square (RMS) travel time residual, in sec, using all weights. This parameter provides a measure of the fit of the observed arrival times to the predicted arrival times for this location. Smaller numbers reflect a better fit of the data. The value is dependent on the accuracy of the velocity model used to compute the earthquake location, the quality weights assigned to the arrival time data, and the procedure used to locate the earthquake.

sig
Data Type
Integer
Typical Values
[0, 1000]
Description
A number describing how significant the event is. Larger numbers indicate a more significant event. This value is determined on a number of factors, including: magnitude, maximum MMI, felt reports, and estimated impact.

sources
Data Type
String
Typical Values
",us,nc,ci,"
Description
A comma-separated list of network contributors.

status
Data Type
String
Typical Values
“automatic”, “reviewed”, “deleted”
Description
Indicates whether the event has been reviewed by a human.
Additional Information
Status is either automatic or reviewed. Automatic events are directly posted by automatic processing systems and have not been verified or altered by a human. Reviewed events have been looked at by a human. The level of review can range from a quick validity check to a careful reanalysis of the event.

time
Data Type
Long Integer
Description
Time when the event occurred. Times are reported in milliseconds since the epoch ( 1970-01-01T00:00:00.000Z), and do not include leap seconds. In certain output formats, the date is formatted for readability.
Additional Information
We indicate the date and time when the earthquake initiates rupture, which is known as the "origin" time. Note that large earthquakes can continue rupturing for many 10's of seconds. We provide time in UTC (Coordinated Universal Time). Seismologists use UTC to avoid confusion caused by local time zones and daylight savings time. On the individual event pages, times are also provided for the time at the epicenter, and your local time based on the time your computer is set.

tsunami
Data Type
Integer
Description
This flag is set to "1" for large events in oceanic regions and "0" otherwise. The existence or value of this flag does not indicate if a tsunami actually did or will exist. If the flag value is "1", the event will include a link to the NOAA Tsunami website for tsunami information. The USGS is not responsible for Tsunami warning; we are simply providing a link to the authoritative NOAA source.
See http://www.tsunami.gov/ for all current tsunami alert statuses.

type
Data Type
String
Typical Values
“earthquake”, “quarry”
Description
Type of seismic event.

types
Data Type
String
Typical Values
“,cap,dyfi,general-link,origin,p-wave-travel-times,phase-data,”
Description
A comma-separated list of product types associated to this event.

tz
Data Type
Integer
Typical Values
[-1200, +1200]
Description
Timezone offset from UTC in minutes at the event epicenter.

updated
Data Type
Long Integer
Description
Time when the event was most recently updated. Times are reported in milliseconds since the epoch. In certain output formats, the date is formatted for readability.

url
Data Type
String
Description
Link to USGS Event Page for event.