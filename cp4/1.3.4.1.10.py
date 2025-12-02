import re

inputStr = "123 a12 34 sjfa;dl;j  adfljdsflje;o9uarogiu s     asldfj;jsdf aa12 j123"
print(re.sub(r"\b[a-z]\d{2}\b", "***", inputStr))
