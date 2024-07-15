# transit_time

To use the transit calculator, you must be logged into one of the GBO data reduction machines (maxwell, newton, plack, thales, leibniz) OR observing machines (titania or ariel). This script will output the transit time in UTC as well as the azimuth and elevation coordinates at the time of transit. Note that it is currently hardwired to search for transits with the telescope locked out at 90.5º azimuth. 

To print the input requirements, please type 

    ~dbautist/GSI/transit_time help 

into the linux command line. This will print a list of arguments and tell you how they need to be formatted. It is important to follow the formatting requirements when entering the commands. 

## Example script call

The script will output three lines of information: 

1. The time of transit in UTC

2. The azimuth during transit --  note that this is locked at 90.5º

3. Elevation during transit

Example output of a source that WOULD transit the beam during the observing window:

    $ ~dbautist/GSI/transit_time 2024-07-14T16:30:00 2024-07-14T17:30:00 10h44m50.96s 24d47m45.4s
    transit time: 2024-07-14T16:58:00.480
    az: 90.50056375743543 deg
    el: 42.80892655000921 deg


Example output of a source that WOULD NOT cross the beam during the observing window:

    $ ~dbautist/GSI/transit_time 2024-07-14T16:30:00 2024-07-14T17:30:00 10h44m50.96s 53d47m45.4s
    transit time: 2024-07-14T16:56:17.232
    az: 49.13687045647204 deg
    el: 50.49507113802659 deg
    WARNING:: your source may not transit the beam.
    Please try another source or observing window :)

## Observing windows
The time needs to be in UTC in YYYY-MM-DDTHH:MM:SS format. For example: `2024-07-14T16:00:00.00`. 

## Source Coordinates:
These coordinates should be in the form J2000, I have not tested this in Galactic coordinates and it may cause problems. Please convert the coordinates to J2000 if this is the case. :)

The right ascension of the source should be in units of hour, minute, second (HMS). This is the form that they would appear in a catalog file or on SIMBAD. 

An RA from a catalog would look something like `10:44:50.96` and would need to be converted to `10h44m50.96s` by deleting the colons and replacing them with d,m,s. 

The declination of the source should be in units of degree, minute, second (DMS). This is the form that they would appear in a catalog file or on SIMBAD. 

A DEC from a catalog would look something like `24:47:45.4` and would need to be converted to `24d47m45.4s` by deleting the semicolons and replacing them with h,m,s. 
