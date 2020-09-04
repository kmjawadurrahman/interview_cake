# Merging Meeting Times

### Notes:

Instead of deepcopying the list, popping items from it and tracking index, could have indexed the running solution list's last item.
So, need to make better use of existing variables in the code.


# Reverse String in Place

### Notes:

No need to use a temporary variable. Can swap directly instead.


# Reverse Words

### Notes:

Instead of using pop and insert, get O(n) time complexity by first swapping characters,

`input = ['g', 'o', 'o', 'd', ' ', 'a', 'm', ' ', 'i'] `

`step_1 = ['i', ' ', 'm', 'a', ' ', 'd', 'o', 'o', 'g']`

then tracking start and end of each words, and finally applying reverse again on each word.

`output = ['i', ' ', 'a', 'm', ' ', 'g', 'o', 'o', 'd']`
