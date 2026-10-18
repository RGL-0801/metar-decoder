# METAR Decoder v1.2

A small Python program that reads METAR weather reports from a text file, extracts key values into structured data, and prints a short summary.

## What it does

- Reads METAR lines from `metars.txt`
- Extracts the station, time, wind direction, wind speed, and temperature (including negative temperatures written as `M02`)
- Extracts visibility, weather, clouds, altimeter, wind gusts and variable wind direction.
- Skips malformed lines and prints which line was skipped
- Lists stations with wind speed above 10 knots
- Calculates the average temperature across all valid reports
- Parsing is split into `parse_metar()` and its helper functions

## How to run it

```
python metar_decoder.py
```

`metars.txt` must be in the same folder as the script.

## Example output

```
Mistake on METAR report: MHSC 051500Z

 --STATIONS ABOVE 10KTS--
MHLM
MPTO

 --AVERAGE TEMPERATURE--
20.7 degrees Celsius.

--PROGRAM COMPLETE--
```

It also prints the full list of parsed reports before the summary. I skipped it because it would be too long to include.

## About the data

`metars.txt` contains **made-up practice data**, not real weather reports. It includes:

- one incomplete line (`MHSC`) to test error handling
- two lines with negative temperatures or dew points to test the `M` prefix
- one line with wind gusts to test the `G` prefix (v1.2)
- one line with `VRB` to test variable wind identification (v1.2)

## Known limitations

- Parsing three digit winds
- Handling CAVOK, RMK, and RVR
- Handling AUTO and METAR prefixes producing wrong values
- Ignores variable wind group (like "010V070")
- Doesn't store dew point

## What I practiced

- Reading files with `open`
- Using `.split()` and `.strip()` to clean up data
- Lists and Dictionaries
- Loops and conditions
- Handling Errors with `try/except`
- Handling variations in format with `.startswith()`
- Working with and calling functions with `return`
- Writing helper functions
- Refactoring without changing the output
- Guarding against division by zero

## Planned improvements

- ~~Move all the parsing processes to its dedicated function (`parse_metar()`)~~
- ~~Parse gusts and variable winds~~
- Identify tokens by their format instead of their position.
- Be able to identify and parse three digit wind speeds
- Handle CAVOK, RMK, and RVRs inside the raw METAR data
- Handle AUTO and METAR prefixes
- Store dew point values