# version-control-in-atom.py
'''Version control is an important aspect of any project and Atom comes with
basic Git and GitHub integration built in.

In order to use version control in Atom, the project root needs to contain the
Git repository.
'''

# Checkout HEAD status
# Alt+Ctrl+Z        yet to work = "git checkout HEAD --<path>
# and git reset HEAD -- <path>"

# Git status list
# Ctrl+Shift+B      is equal to "git status" which displays a list of all the
# untracked and modified files in the project

# Quickly open files in the project
# Ctrl + B

# Status bar icons for short cut
# "master"
# "push"
# "github"
# "git"

# Line diffs
# The included git-diff package colorizes the gutter next to lines that have
# been added or edited (green highlight), or removed(red highlight) when
# selected any either unstaged or staged "changed" files in "git" pane.

'''Open on GitHub

If the project you're working on is on GitHub, there are also some very useful
integrations you can use. Most of the commands will take the current file you're
viewing and open a view of that file on GitHub - for instance, the blame or
commit history of that file.

    Alt+G O - Open file on GitHub
    Alt+G B - Open Blame view of file on GitHub
    Alt+G H - Open History view of file on GitHub
    Alt+G C - Copy the URL of the current file on GitHub to the clipboard
    Alt+G R - Branch compare on GitHub

The branch comparison shows you the commits that are on the branch you're
currently working on locally that are not on the mainline branch.
'''
