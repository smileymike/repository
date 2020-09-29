# atom-selections.py
'''
Text selections in Atom support a number of actions, such as scoping deletion,
indentation and search actions, and marking text for actions such as quoting and
bracketing.

Selections mirror many of the movement commands. They're actually exactly the
same keybindings as the movement commands, but with a Shift key added in.

    Shift+Down - Select down
    Shift+Up - Select up
    Shift+Left - Select previous character
    Shift+Right - Select next character
    Ctrl+Shift+Left - Select to beginning of word
    Ctrl+Shift+Right - Select to end of word
    Shift+End - Select to end of line
    Shift+Home - Select to first character of line
    Ctrl+Shift+Home - Select to top of file
    Ctrl+Shift+End - Select to bottom of file

In addition to the cursor movement selection commands, there are also a few
commands that help with selecting specific areas of content.

    Ctrl+A - Select the entire contents of the file
    Ctrl+L - Select the entire line
'''
# Move statment line up or down
# Ctrl+<UP cursor> or Ctrl+<DOWN Cursor>

# Indent or undent a block of statements
# Firstly, Shift+<UP cursor> or Shift+<DOWN cursor> to select block of statements
# Secondly, Ctrl+[ to indent left or Ctrl+] to indent right
