# Property-based testing with Python

## Requirements

PyTest for unit testing:

```
pip install pytest
```

Hypothesis for property-based testing:

```
pip install hypothesis
```

## Run

```
pytest test_[example].py
```

Verbose mode for PyTest:

```
pytest test_[example].py -v
```

Verbose mode for PyTest and Hypothesis:

```
pytest test_[example].py -v -s
```

## Further reading

By [Scott Wlaschin](https://twitter.com/ScottWlaschin):
* [Part 1 - An introduction to property-based testing](https://fsharpforfunandprofit.com/posts/property-based-testing/)
* [Part 2 - Choosing properties for property-based testing](https://fsharpforfunandprofit.com/posts/property-based-testing-2/)
