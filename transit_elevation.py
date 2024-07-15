from astropy.time import Time
from astropy import units as u
from astropy.coordinates import AltAz, EarthLocation, SkyCoord
import numpy as np
import argparse

def get_time_and_el(tstart, tstop, RA, DEC):
    """
    input time in UTC
    RA in HMS
    DEC in DMS
    time format: YYYY-MM-DDTHH:MM:SS
    """

    times = [tstart, tstop]
    t = Time(times, format="isot", scale="utc")
    time_step = 5e-6#1.1574073869269342e-05 # MJD second
    dt = np.diff(t.mjd)

    mjd_times = []

    dt = np.diff(t.mjd)
    N = int(dt[0]//time_step)

    for i in range(N):
        mjd_times.append(t[0].mjd + i*time_step)

    obs_time = Time(mjd_times, format="mjd")

    # define GBT location
    GBT = EarthLocation.of_site('Green Bank Telescope')
    aa = AltAz(location=GBT, obstime=obs_time)
    coord = SkyCoord(RA, DEC)
    altaz = coord.transform_to(aa)

    closest_index = np.argmin(np.abs(altaz.az.deg - 90.5))
    transit_time = obs_time[closest_index]

    transit_coords = AltAz(location=GBT, obstime=obs_time[closest_index])
    altaz = coord.transform_to(transit_coords)

    print(f"transit time: {transit_time.isot}")
    print(f"az: {altaz.az.deg} deg")
    print(f"el: {altaz.alt.deg} deg")

    if np.abs(altaz.az.deg - 90.5) > 0.1:
        print("WARNING:: your source may not transit the beam.\nPlease try another source or observing window :)")

    return transit_time.isot, altaz.az.deg, altaz.alt.deg

if __name__=="__main__":
    parser = argparse.ArgumentParser(description="")
    parser.add_argument("tstart", help='start time of observing window. Format: YYYY-MM-DDTHH:MM:SS Example: 2024-07-14T16:30:00.00')
    parser.add_argument("tstop", help='stop time of observing window. Format: YYYY-MM-DDTHH:MM:SS')
    parser.add_argument("RA",help='source right ascencsion. Format: HMS. Example: 10h44m50.96s')
    parser.add_argument("DEC", help='source declination. Format: DMS. Example: 24d47m45.4s')
    args = parser.parse_args()

    get_time_and_el(args.tstart, args.tstop, args.RA, args.DEC)