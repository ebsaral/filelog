# writer 1.0.0

Hello.

I am an easy debugger which prints into files. I can also read. In case you need me ever.

Simplicity within a certain complexity.

# Install

`pip install writer`

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


## Example

```code=python
Writer() >> {'allah': 'birdir'}
# creates a file called debug.log and saves into
>>> {"allah": "birdir"}

test = Reader() # reads from debug.log
print test
>>> {'allah': 'birdir'}

# delete callback
import os
Writer(callback: lambda x: os.remove(x)) >> {'test': 'callback'} # deletes the file
```
