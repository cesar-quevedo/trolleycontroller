# Custom Trolley Controller GUI
![](images/gui1.PNG)
![](images/gui2.PNG)
# 3D Metal Jet Printer(Twelve printer)
![](images/twelveprinter.PNG)
# Build Unit(Trolley)
![](images/buildunit.PNG)
# Overview
This is an interactive software application that uses Python and TCL commands to control HP’s 3D metal jet printer's build units. The GUI was designed to eliminate the need to connect the build unit to a 3D metal jet printer. Now, it is no longer necessary for operators to use a metal jet printer to lower or raise the build unit. The GUI was created using CustomTkinter, and the build units are controlled with Python serial, also known as pyserial. This software application was added to a Raspberry Pi, which was connected to a touch-screen display. The Raspberry Pi was communicating with the build units via a RS232 serial cable.
# Learn more about CustomTkinter
"CustomTkinter is a python UI-library based on Tkinter, which provides new, modern and fully customizable widgets. They are created and used like normal Tkinter widgets and can also be used in combination with normal Tkinter elements. The widgets and the window colors either adapt to the system appearance or the manually set mode ('light', 'dark'), and all CustomTkinter widgets and windows support HighDPI scaling (Windows, macOS). With CustomTkinter you'll get a consistent and modern look across all desktop platforms (Windows, macOS, Linux)" - TomSchimansky
- https://github.com/TomSchimansky/CustomTkinter
# Learn more about pyserial
"This module encapsulates the access for the serial port. It provides backends for Python running on Windows, OSX, Linux, BSD (possibly any POSIX compliant system) and IronPython. The module named "serial" automatically selects the appropriate backend" - pyserial
- https://github.com/pyserial/pyserial
# IMPORTANT INFORMATION
https://github.com/cesar-quevedo/trolleycontroller/wiki
