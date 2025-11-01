
PYP_Iniparser
===============

module

Primitive (really!) parser for ini files


----------------


__Features__:

Parses any file and stores a dictionary of parameters.

[!NOTE]
Accepts only lines containing at least one equal ('=') sign:
```
Value= 10
OTHER_VALUE=100
yetAnothervalue = something else
```

this will produce dictionary:
```
{"Value":"10", "OTHER_VALUE":"100", "yetAnothervalue": "something else"}
```

in case of many equal signs the first will determine where the value starts:
```
Many_EQUALS = there is = a lot=of equals=
```

will create the pair:
```
{"Many_EQUALS": "there is = a lot=of equals=}
```

__Usage__:
```
from pyp_iniparser import PYP_Iniparser

parser = PYP_Iniparser()
parser.parse("path/to/your/inifile.ini")
print(parser.data)
```

By default parser produces only strings as values. By using:
```
parser.parse("path/to/your/inifile.ini", True)
```

you may enforce checking the types. Only float, int, boolean and string are supported.

None of methods raises any exceptions. 
If required file does not exists, cannot be accessed or something happened during the parsing parser method silently returns False. Otherwise parser will always return True even if in the readed file there was no proper key/value pairs.
 
