pyblish-3dsmax
==============
Pyblish for 3ds Max.

Note: This only tested in `3dsmax-2020`.

What is included?
----------------
A set of common plug-ins and functions shared across other integrations - such as getting the current working file. It also visually integrates Pyblish into the File-menu for easy access.
- Common [plug-ins](https://github.com/pyblish/pyblish-photoshop/tree/master/pyblish_3dsmax/plugins)

<br>
<br>
<br>

Installation
------------
Via pip install `pyblish-3dsmax` will be installing all depends packages.

```cmd
pip install pyblish_3dsmax
```

Copy module files to `<3dsmax_install_root/python/Lib/site-packages>`
Copy startup script `<root>/startup/pyblish_3dsmax.ms` to `<3dsmax_install_root>/scripts/startup/pyblish_3dsmax.ms`.
 
For example:

copy `C:\Users\longhao\PycharmProjects\pyblish-3dsmax\startup\pyblish_3dsmax.ms` to `C:\Program Files\Autodesk\3ds Max 2020\scripts\Startup\pyblish_3dsmax.ms`


<img src="https://i.imgur.com/sQvwGFF.png" alt="menu"></a>

<img src="https://i.imgur.com/76SH1xb.gif">
