# Merging Meeting Times

### Notes:

Instead of deepcopying the list, popping items from it and tracking index, could have indexed the running solution list's last item.
So, need to make better use of existing variables in the code.


# Reverse String in Place

### Notes:

No need to use a temporary variable. Can swap directly instead.


# Reverse Words

### Notes:

Instead of using pop and insert, get O(n) time complexity by first reversing in-place by swapping characters,

`input = ['g', 'o', 'o', 'd', ' ', 'a', 'm', ' ', 'i'] `

`step_1 = ['i', ' ', 'm', 'a', ' ', 'd', 'o', 'o', 'g']`

then tracking start and end of each word, and finally applying reverse again on each word.

`output = ['i', ' ', 'a', 'm', ' ', 'g', 'o', 'o', 'd']`


# Merge Sorted Arrays

### Notes:

O(n) time complexity is achievable. Instead of comparing each of the elements from each list every time (nested for loop and thus O(n^2) time complexity), do the following:
- Track current index of the two lists and the new merged list.
- Compare the items at the current index of the two lists, then update the merged list and the indices accordingly.
- Use indices and list length information to handle edge cases like exhausting list items (that lead to IndexError).


# Cafe Order Checker

### Notes:

None.
