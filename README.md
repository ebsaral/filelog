# filewriter 1.0.7

Hello.

I am an easy debugger which prints into files. I can also read. In case you need me ever.

Simplicity within a certain complexity.

# Install

`pip install filewriter`

# Documentation

## param: filename

Name of the file. The extension `.log` will be added. 
Default: `debug`
ENV name: `READABLE_GLOBAL_VARIABLE_NAME`

## param: debug

If set True, prints what's going on.
Default: True

## param: json

If set True, it will enable json conversion
Default: True

## param: callback

If set (a function), the function gets executed with the path of created file.
Default: None

## Examples

```python
from filewriter import Writer, Reader, FReader, Reverse

# creates a file called debug.log and saves into
Writer() << {'allah': 'birdir'}
>>> {"allah": "birdir"}

# reverse the operator, if that's easier to read
# https://docs.python.org/3/reference/simple_stmts.html#assignment-statements
Reverse({'allah': 'birdir'}) >> Writer()
>>> {"allah": "birdir"}

# reads from debug.log
test = Reader() 
print(test)
>>> {'allah': 'birdir'}

# formatted reader
FReader() >> f"Output {readable}"

# delete callback
import os
Writer(callback: lambda filename: os.remove(filename)) >> {'test': 'callback'} # deletes the file
```



# API

## filewriter.Writer

Env Name: `READABLE_GLOBAL_VARIABLE_NAME` Default: `readable`

```python

Writer(
    filename="debug",
    debug=True,
    json=True,
    callback=None,
)

```

## filewriter.Reader

Env Name: `READABLE_GLOBAL_VARIABLE_NAME` Default: `readable`

```python

Reader(
    filename="debug",
    debug=True,
    json=True,
    callback=None,
)

```

## filewriter.FReader

Env Name: `READABLE_GLOBAL_VARIABLE_NAME` Default: `readable`

```python

FReader(
    filename="debug",
    debug=True,
    json=True,
    callback=None,
)

```

Twitter: @ebsaral
