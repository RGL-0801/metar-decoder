# METAR Decoder v1.5

A small Python program that reads METAR weather reports from a text file, extracts key values into structured data, and prints a short summary.

## What it does

- Reads METAR lines from `metars.txt`
- Extracts the station, time, wind direction, wind speed, temperature and dew point (including negative values written as `M02`)
- Extracts visibility, weather, clouds and altimeter
- Handles wind gusts (`G`), variable wind (`VRB`) and two- or three-digit wind speeds (e.g. `270105G120KT`)
- Stores dew point as `None` when it is missing (e.g. `27/`)
- Skips malformed lines and prints which line was skipped
- Lists stations with wind speed above 10 knots
- Calculates the average temperature across all valid reports
- Parsing is split into `parse_metar()` and its helper functions
- Identifies each token by its format instead of its position

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
MHDD
MHEE

 --AVERAGE TEMPERATURE--
23.9 degrees Celsius.

--PROGRAM COMPLETE--
```

It also prints the full list of parsed reports before the summary. I left it out here because it is too long.

## About the data

`metars.txt` contains **made-up practice data**, not real weather reports. It includes:

- one incomplete line (`MHSC`) to test error handling
- two lines with negative temperatures or dew points to test the `M` prefix
- one line with wind gusts to test the `G` prefix
- one line with `VRB` to test variable wind
- one line with `CAVOK` and `RMK` to test CAVOK visibility and stopping at RMK
- one line with `AUTO` and the `METAR` prefix to test that they are skipped
- one line with `-RA` to test weather abbreviations
- one line with no dew point (`27/`) to test missing data
- lines with three-digit wind speeds and gusts (`270105G120KT`, `090105KT`)
- one line with `VRB` and a gust (`VRB05G15KT`)
- one line with a variable wind group (`010V070`), not decoded yet

## Known limitations

- The variable wind group (like `010V070`) is not decoded yet; it currently ends up in the weather list
- CAVOK, RMK and RVR are recognised but not interpreted

## What I practiced

- Reading files with `open`
- Using `.split()`, `.strip()` and `.removesuffix()` to clean up data
- Lists and dictionaries
- Loops and conditions
- Handling errors with `try/except`
- Handling variations in format with `.startswith()`
- Writing helper functions that `return` values
- Refactoring without changing the output
- Guarding against division by zero
- Slicing from the front instead of fixed positions, so values of different lengths still work
- Testing with expected results and checking that no lines were silently dropped

## Planned improvements

- ~~Move all the parsing to its own function (`parse_metar()`)~~
- ~~Parse gusts and VRB winds~~
- ~~Identify tokens by their format instead of their position~~
- ~~Handle AUTO and METAR prefixes~~
- ~~Store dew point values~~
- ~~Parse three-digit wind speeds~~
- Decode the variable wind group (`010V070`)
- Interpret CAVOK, RMK and RVRs
- Analyse real METAR data with pandas
