#! /usr/bin/python
"""
run python ./diff_html.py > diff.html  ;then use web to open diff.html
"""
import difflib
text1 = """text1:
This module provides classes and functions for comparing sequences.
Including Html and context and unified diffs.
difflib document v7.4.
add string
"""

text1_lines = text1.splitlines()

text2 = """text2:
This module provides classes and functions for comparing sequences.
including Html and context and unified diffs.
difflib document v7.5
"""
text2_lines = text2.splitlines()

d = difflib.HtmlDiff()
diff = d.make_file(text1_lines,text2_lines)
print(diff)
