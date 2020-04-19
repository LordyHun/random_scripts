# Copying files to build directory with qMake
When I was working on a project built over Qt, I wanted to copy a number of files next to the directory where my executables were built to.
After much of google-fu (since this feature is not well documented in Qt docs), I've found [something nice](https://dragly.org/2013/11/05/copying-data-files-to-the-build-directory-when-working-with-qmake/) which worked well on my linux work machine:
## The first solution
```
copyconfig.commands = $(COPY_DIR) $$PWD/res/config $$OUT_PWD
first.depends = $(first) copyconfig
export(first.depends)
export(copyconfig.commands)
QMAKE_EXTRA_TARGETS += first copyconfig
```
But on Windows, I've ran into the following error message:
`xcopy /s /q /y /i D:/Dev/qWindowApp/app/res/config D:/Dev/builds/.../app Invalid number of parameters`

Naturally, I've turned to Qt's support, who gave me the following response:
`copyconfig.commands = $(COPY_DIR) $$shell_quote($$shell_path($$PWD/res/config)) $$shell_quote($$shell_path($$OUT_PWD))`

Which is a clear and understandable solution. And I really didn't want to follow it since... I don't know if "using `$$shell_*` seems kind of a lot of typing to copy files" sounds like a valid reason, but that was _my_ reason for it.

Nevertheless, the main reason for me to use Qt is usually because I really want something to work on all OSs the same way. So I really needed to find a solution.

So I've found the following solution to the task:

## My usual go-to solution
qMake actually has an [undocumented feature](https://codereview.qt-project.org/c/qt/qtbase/+/156784) for this. It's simple to understand, you don't have to type scary-looking variable names into your makefiles and works on all OSs that I normally use (which would be Linux and Windows):
```
# Add file_copies to the config
CONFIG += file_copies
# Copies is not documented, but nevertheless works (received it as a tip on a Qt Support channel
COPIES += configFiles

# Add files to copy to the list
configFiles.files = $$PWD/docs/*
# this could be something like: configFiles.files = $$PWD/res/config/*
configFiles.path = $$OUT_PWD/data
```

I've decided to add this to this repo since about 90% of Google results for this topic are people wondering if this is something that one can actually do and most of the rest are ingenious hacks to get something work, while the feature is actually there, it's just not documented!
(I've also added a very minimal example project to the repo)
