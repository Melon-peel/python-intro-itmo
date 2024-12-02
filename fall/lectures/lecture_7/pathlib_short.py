import pathlib
from pathlib import PureWindowsPath, PurePosixPath

print(PurePosixPath("../hello.txt"))
print(PureWindowsPath("../hello.txt"))