#! /usr/bin/python
import difflib
text1 = """text1:
This module provides classes and functions for comparing sequences.
Including Html and context and unified diffs.
difflib document v7.4.
add string
"""

text1_lines = text1.splitlines()
print(text1_lines)

text2 = """text2:
This module provides classes and functions for comparing sequences.
including Html and context and unified diffs.
difflib document v7.5
"""
text2_lines = text2.splitlines()
print(text2_lines)

d = difflib.Differ()
diff = d.compare(text1_lines,text2_lines)
print('\n'.join(list(diff)))
