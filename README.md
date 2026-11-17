# METAR Decoder v1.7

A small Python program that reads METAR weather reports from a text file, extracts key values into structured data, and prints a short summary.

## What it does

- Reads METAR lines from `metars.txt`
- Extracts the station, time, wind direction, wind speed, temperature and dew point (including negative values written as `M02`)
- Extracts visibility, weather, clouds and altimeter
- Handles wind gusts (`G`), variable wind (`VRB`) and two- or three-digit wind speeds (e.g. `270105G120KT`)
- Decodes the variable wind direction group (e.g. `010V070` → varying between 010° and 070°)
- Stores dew point as `None` when it is missing (e.g. `27/`)
- Skips malformed lines and prints which line was skipped
- Loads the parsed reports into a pandas DataFrame
- Lists stations with wind speed above 10 knots (with their wind speed)
- Calculates the average temperature across all valid reports
- Prints "NO DATA AVAILABLE!" instead of crashing if no report could be parsed
- Parsing is split into `parse_metar()` and its helper functions
- Identifies each token by its format instead of its position

## How to run it

Requires Python 3.9 or newer and pandas:

```
pip install pandas
```

```
python metar_decoder.py
```

`metars.txt` must be in the same folder as the script.

## Output fields

Each parsed report is a dictionary with these keys:

| Key | Example | Meaning |
|---|---|---|
| `origin` | `MHTG` | Station code |
| `time` | `051500Z` | Day and time (UTC) |
| `wind_direction` | `240` | Degrees, `None` for `VRB` |
| `wind_speed` | `10` | Knots |
| `wind_gust` | `25` | Knots, `None` if no gust |
| `variable_wind_start` | `10` | Degrees, `None` if not reported |
| `variable_wind_end` | `70` | Degrees, `None` if not reported |
| `visibility` | `9999` | Meters, or `CAVOK` |
| `weather` | `['-RA']` | Weather codes |
| `clouds` | `['FEW040']` | Cloud layers |
| `temperature_C` | `27` | Degrees Celsius |
| `dew_point` | `15` | Degrees Celsius, `None` if missing |
| `altimeter` | `A3012` | Altimeter setting |

## Example output

```
Mistake on METAR report: MHSC 051500Z

 --STATIONS ABOVE 10KTS--
   origin  wind_speed
1    MHLM          12
3    MPTO          15
10   MHDD         105
11   MHEE         105

 --AVERAGE TEMPERATURE--
23.86 degrees Celsius

--PROGRAM COMPLETE--
```

It also prints the full list of parsed reports before the summary. I left it out here because it is too long. The numbers on the left of the station table are the row numbers (index) from the full DataFrame.

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
- one line with a variable wind group (`010V070`)

## Known limitations

- CAVOK, RMK and RVR are recognised but not interpreted

## What I practiced

- Reading files with `open`
- Using `.split()`, `.strip()` and `.removesuffix()` to clean up data
- Lists and dictionaries
- Loops and conditions
- Handling errors with `try/except`
- Handling variations in format with `.startswith()` and `.isdigit()`
- Writing helper functions that `return` values, including optional arguments
- Refactoring without changing the output
- Guarding against division by zero
- Slicing from the front instead of fixed positions, so values of different lengths still work
- Writing precise checks so one token type isn't mistaken for another (`010V070` vs `VRB03KT`)
- Testing with expected results and checking that no lines were silently dropped
- pandas basics: creating a DataFrame, selecting columns, filtering rows, `.mean()` and `df.empty`

## Planned improvements

- ~~Move all the parsing to its own function (`parse_metar()`)~~
- ~~Parse gusts and VRB winds~~
- ~~Identify tokens by their format instead of their position~~
- ~~Handle AUTO and METAR prefixes~~
- ~~Store dew point values~~
- ~~Parse three-digit wind speeds~~
- ~~Decode the variable wind group (`010V070`)~~
- Interpret CAVOK, RMK and RVRs
- ~~Rewrite the summaries with pandas~~
- Add a temperature/dew point spread column (fog risk)
- Analyse real METAR data with pandas
