# METAR Decoder

A small Python program that reads METAR weather reports from a text file, extracts key values into structured data, and prints a short summary.

## What it does

- Reads METAR lines from `metars.txt`
- Extracts the station, time, wind direction, wind speed, and temperature (including negative temperatures written as `M02`)
- Skips malformed lines and prints which line was skipped
- Lists stations with wind speed above 10 knots
- Calculates the average temperature across all valid reports

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
19.5 degrees Celsius.

--PROGRAM COMPLETE--
```

It also prints the full list of parsed reports before the summary. I skipped it because it would be too long to include.

## About the data

`metars.txt` contains **made-up practice data**, not real weather reports. It includes:

- one incomplete line (`MHSC`) to test error handling
- two lines with negative temperatures or dew points to test the `M` prefix

## Known limitations

- Wind gusts (for example `G25`) are ignored. Only the sustained speed is recorded.
- Reports with variable wind (`VRB`) would be skipped as invalid.

## What I practiced

- Reading files with `open`
- Using `.split()` and `.strip()` to clean up data
- Lists and Dictionaries
- Loops and conditions
- Handling Errors with `try/except`

## Planned improvements

- Move all the parsing processes to its dedicated function (`parse_metar()`)
- Parse gusts and variable winds