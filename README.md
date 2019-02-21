# Property-based testing in Python

## The origin of this repository

:seedling: This repository was created to complement the [_Property-based testing_ workshop](https://github.com/delr3ves/WeCodeProperties) by [Sergio Arroyo Cuevas](https://twitter.com/delr3ves) with another programming language.

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

To run all the available tests:

```
pytest test*
```

Verbose mode for PyTest:

```
pytest test_[example].py -v
```

Verbose mode for PyTest and Hypothesis:

```
pytest test_[example].py -v -s
```

## How to play

### Knowing Hypothesis library to define properties in tests

Branches:

* `sum-properties`
* `fibonacci-properties`
* `collection-properties`

You have the production code and you only have to add the test code. 

There is a branch with a possible solution for each one: `[branch]-solved`.

[Know more about Hypothesis library](https://hypothesis.readthedocs.io/en/latest/index.html).

### Knowing the real magic of property-based testing

Start with `scaffolding` branch and follow the next steps:

1. TDD workflow for sum operation, Fibonacci series and common operations with collections (append an element, remove an element, concatenation, removing duplications)
2. Additional final refactor step: improve the testing code when specifying properties.

## Further reading

By [Scott Wlaschin](https://twitter.com/ScottWlaschin):
* [Part 1 - An introduction to property-based testing](https://fsharpforfunandprofit.com/posts/property-based-testing/)
* [Part 2 - Choosing properties for property-based testing](https://fsharpforfunandprofit.com/posts/property-based-testing-2/)
