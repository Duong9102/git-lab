Answer1:2.34.1
Answer2:user.name=Nguyen Duc Duong
               User.name=251020905247@st.phenikaa-uni.edu.vn
Answer3:
NAME
       git-add - Add file contents to the index

SYNOPSIS
       git add [--verbose | -v] [--dry-run | -n] [--force | -f] [--interactive | -i] [--patch | -p]
                 [--edit | -e] [--[no-]all | --[no-]ignore-removal | [--update | -u]] [--sparse]
                 [--intent-to-add | -N] [--refresh] [--ignore-errors] [--ignore-missing] [--renormalize]
                 [--chmod=(+|-)x] [--pathspec-from-file=<file> [--pathspec-file-nul]]
                 [--] [<pathspec>...]

DESCRIPTION
       This command updates the index using the current content found in the
       working tree, to prepare the content staged for the next commit. It
       typically adds the current content of existing paths as a whole, but
       with some options it can also be used to add content with only part of
       the changes made to the working tree files applied, or remove paths that
       do not exist in the working tree anymore.

       The "index" holds a snapshot of the content of the working tree, and it
       is this snapshot that is taken as the contents of the next commit. Thus
       after making any changes to the working tree, and before running the
       commit command, you must use the add command to add any new or modified
       files to the index.

       This command can be performed multiple times before a commit. It only
       adds the content of the specified file(s) at the time the add command is
       run; if you want subsequent changes included in the next commit, then
       you must run git add again to add the new content to the index.

       The git status command can be used to obtain a summary of which files
       have changes that are staged for the next commit.

       The git add command will not add ignored files by default. If any
       ignored files were explicitly specified on the command line, git add
       will fail with a list of ignored files. Ignored files reached by
       directory recursion or filename globbing performed by Git (quote your
       globs before the shell) will be silently ignored. The git add command
       can be used to add ignored files with the -f (force) option.

       Please see git-commit(1) for alternative ways to add content to a
       commit.

OPTIONS
       <pathspec>...
Answer4:
On branch master

No commits yet

Untracked files:
  (use "git add <file>..." to include in what will be committed)
        README.me
       the changes made to the working tree files applied, or remove paths that
       do not exist in the working tree anymore.

       The "index" holds a snapshot of the content of the working tree, and it
       is this snapshot that is taken as the contents of the next commit. Thus
       after making any changes to the working tree, and before running the
       commit command, you must use the add command to add any new or modified
       files to the index.

       This command can be performed multiple times before a commit. It only
       adds the content of the specified file(s) at the time the add command is
       run; if you want subsequent changes included in the next commit, then
       you must run git add again to add the new content to the index.

       The git status command can be used to obtain a summary of which files
       have changes that are staged for the next commit.
nothing added to commit but untracked files present (use "git add" to track)•	Answer1:2.34.1
Answer2:user.name=Nguyen Duc Duong
               User.name=251020905247@st.phenikaa-uni.edu.vn
Answer3:
NAME
       git-add - Add file contents to the index

SYNOPSIS
       git add [--verbose | -v] [--dry-run | -n] [--force | -f] [--interactive | -i] [--patch | -p]
                 [--edit | -e] [--[no-]all | --[no-]ignore-removal | [--update | -u]] [--sparse]
                 [--intent-to-add | -N] [--refresh] [--ignore-errors] [--ignore-missing] [--renormalize]
                 [--chmod=(+|-)x] [--pathspec-from-file=<file> [--pathspec-file-nul]]
                 [--] [<pathspec>...]

DESCRIPTION
       This command updates the index using the current content found in the
       working tree, to prepare the content staged for the next commit. It
       typically adds the current content of existing paths as a whole, but
       with some options it can also be used to add content with only part of
       the changes made to the working tree files applied, or remove paths that
       do not exist in the working tree anymore.

       The "index" holds a snapshot of the content of the working tree, and it
       is this snapshot that is taken as the contents of the next commit. Thus
       after making any changes to the working tree, and before running the
       commit command, you must use the add command to add any new or modified
       files to the index.

       This command can be performed multiple times before a commit. It only
       adds the content of the specified file(s) at the time the add command is
       run; if you want subsequent changes included in the next commit, then
       you must run git add again to add the new content to the index.

       The git status command can be used to obtain a summary of which files
       have changes that are staged for the next commit.

       The git add command will not add ignored files by default. If any
       ignored files were explicitly specified on the command line, git add
       will fail with a list of ignored files. Ignored files reached by
       directory recursion or filename globbing performed by Git (quote your
       globs before the shell) will be silently ignored. The git add command
       can be used to add ignored files with the -f (force) option.

       Please see git-commit(1) for alternative ways to add content to a
       commit.

OPTIONS
       <pathspec>...
Answer4:
On branch master

No commits yet

Untracked files:
  (use "git add <file>..." to include in what will be committed)
        README.me
       the changes made to the working tree files applied, or remove paths that
       do not exist in the working tree anymore.

       The "index" holds a snapshot of the content of the working tree, and it
       is this snapshot that is taken as the contents of the next commit. Thus
       after making any changes to the working tree, and before running the
       commit command, you must use the add command to add any new or modified
       files to the index.

       This command can be performed multiple times before a commit. It only
       adds the content of the specified file(s) at the time the add command is
       run; if you want subsequent changes included in the next commit, then
       you must run git add again to add the new content to the index.

       The git status command can be used to obtain a summary of which files
       have changes that are staged for the next commit.

       The git add command will not add ignored files by default. If any
       ignored files were explicitly specified on the command line, git add
       will fail with a list of ignored files. Ignored files reached by
       directory recursion or filename globbing performed by Git (quote your
       globs before the shell) will be silently ignored. The git add command
       can be used to add ignored files with the -f (force) option.

       Please see git-commit(1) for alternative ways to add content to a
       commit.

OPTIONS
       <pathspec>...
Answer4:
On branch master

No commits yet

Untracked files:
  (use "git add <file>..." to include in what will be committed)
        README.me

nothing added to commit but untracked files present (use "git add" to track)
Answer1:2.34.1
Answer2:user.name=Nguyen Duc Duong
               User.name=251020905247@st.phenikaa-uni.edu.vn
Answer3:
NAME
       git-add - Add file contents to the index

SYNOPSIS
       git add [--verbose | -v] [--dry-run | -n] [--force | -f] [--interactive | -i] [--patch | -p]
                 [--edit | -e] [--[no-]all | --[no-]ignore-removal | [--update | -u]] [--sparse]
                 [--intent-to-add | -N] [--refresh] [--ignore-errors] [--ignore-missing] [--renormalize]
                 [--chmod=(+|-)x] [--pathspec-from-file=<file> [--pathspec-file-nul]]
                 [--] [<pathspec>...]

DESCRIPTION
       This command updates the index using the current content found in the
       working tree, to prepare the content staged for the next commit. It
       typically adds the current content of existing paths as a whole, but
       with some options it can also be used to add content with only part of
       the changes made to the working tree files applied, or remove paths that
       do not exist in the working tree anymore.

       The "index" holds a snapshot of the content of the working tree, and it
       is this snapshot that is taken as the contents of the next commit. Thus
       after making any changes to the working tree, and before running the
       commit command, you must use the add command to add any new or modified
       files to the index.

       This command can be performed multiple times before a commit. It only
       adds the content of the specified file(s) at the time the add command is
       run; if you want subsequent changes included in the next commit, then
       you must run git add again to add the new content to the index.

       The git status command can be used to obtain a summary of which files
       have changes that are staged for the next commit.

       The git add command will not add ignored files by default. If any
       ignored files were explicitly specified on the command line, git add
       will fail with a list of ignored files. Ignored files reached by
       directory recursion or filename globbing performed by Git (quote your
       globs before the shell) will be silently ignored. The git add command
       can be used to add ignored files with the -f (force) option.

       Please see git-commit(1) for alternative ways to add content to a
       commit.

OPTIONS
       <pathspec>...
Answer4:
On branch master

No commits yet

Untracked files:
  (use "git add <file>..." to include in what will be committed)
        README.me
       the changes made to the working tree files applied, or remove paths that
       do not exist in the working tree anymore.

       The "index" holds a snapshot of the content of the working tree, and it
       is this snapshot that is taken as the contents of the next commit. Thus
       after making any changes to the working tree, and before running the
       commit command, you must use the add command to add any new or modified
       files to the index.

       This command can be performed multiple times before a commit. It only
       adds the content of the specified file(s) at the time the add command is
       run; if you want subsequent changes included in the next commit, then
       you must run git add again to add the new content to the index.

       The git status command can be used to obtain a summary of which files
       have changes that are staged for the next commit.
nothing added to commit but untracked files present (use "git add" to track)
