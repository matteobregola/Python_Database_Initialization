# Python Database Initialization Package


## Overview


The purpose of this package is to provide 
a tool to convert data to a database structure.

The data can be collected from:
    txt file
    csv file
    input from keyboard 
    website

Then the package has two objectives:
1.  Create the table
2.  Initialize the table with the data given.



## Usage

1. Initialize the class:
    db=dbinit()
    
2. Select how we want to collect the data, the source file and where should the result be stored:
     - **db.setbase(mode,source,destination)**
     - *possible modes: "txt","csv","input","url"*
3. Decide hoe should the table and the attributes: should be called:
     - **db.setinfo(insertion)**
     - *possible modes: "regular" (an advanced option will be implemented to select the type of attributes)*



## Future development

1. set_info(advanded)
2. Collect data from multiple files, websites
3. Create multiple tables at the same time

