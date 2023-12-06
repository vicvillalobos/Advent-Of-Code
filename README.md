# Advent-Of-Code
The solutions I come up with for (Advent of Code)[https://adventofcode.com/].


## Execution
I prefer to use docker compose to run a container with the solutions and use it as a playground.
If you have another python environment you can just run the files directly.

To run a challenge, run the following command (linux only):
```bash
./run_challenge <year> <day> <part>
```

## Requirements
I only use `pytest` and `alive_progress` so far. Requirements are installed in the dockerfile.

## Testing
To run the tests, run the following command (linux only):
```bash
./run_tests
```
alternatively, you can run the tests directly with pytest:
```bash
pytest .
```