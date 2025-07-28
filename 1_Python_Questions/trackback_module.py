import traceback
try:
    int('k')
except:
    var = traceback.format_exc()
    print(var)
# Traceback (most recent call last):
#   File "<stdin>", line 2, in <module>
# ValueError: invalid literal for int() with base 10: 'k'