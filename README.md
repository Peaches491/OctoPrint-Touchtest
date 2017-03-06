# OctoPrint-Touchtest

The Touch Test plugin for OctoPrint adds a new sidebar panel, essential for manual bed leveling. A simple 3x3 grid of buttons allows the user to move the printhead to all 4 corners and edges of the printbed, where you can perfotm "the paper test".

Simply slide a piece of paper back and forth underneath the printhead. Adjust your bed leveling screws until the hotend starts to "grab" the paper. Repeat for the center all 4 corners, double checking at the edges (to make sure your bed is nice and flat)


![alt text][screenshot1]


## Setup

Install via the bundled [Plugin Manager](https://github.com/foosel/OctoPrint/wiki/Plugin:-Plugin-Manager)
or manually using this URL:

    https://github.com/Peaches491/OctoPrint-Touchtest/archive/master.zip

## Configuration

Under `Settings > Plugins > Touchtest plugin` be sure to set your bed dimensions, as well as your preferred "Edge Offset" (useful for avoiding the sccrews in the corners fo your print bed. 


[screenshot1]: https://cloud.githubusercontent.com/assets/494334/23596279/dfd73e88-01dd-11e7-862d-46ca012149af.PNG "Logo Title Text 2"
