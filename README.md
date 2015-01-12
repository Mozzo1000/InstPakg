InstPakg
========
InstPakg is a interactive python script were the user can easily install preselected applications and other software available on the Ubuntu operating system. It uses .json files located in the .instpakg folder in your home directory to install the applications listed if so selected.

Supported package managers & distributions
---------------------------
**NOTE: Probably works with earlier/later versions and with distros which uses the supported package managers**

| Package Manager | Tested distros     |
| --------------- | ------------------ |
| Dpkg - Apt      | Ubuntu 14.04/14.10 |
| RPM - Yum       | Fedora 21          |

How to install
-----------------
First download the .zip file from the repository
* In terminal type ```wget https://github.com/Mozzo1000/InstPakg/archive/master.zip```
This will download a "master.zip" in your working directory
* Unzip master.zip, ```unzip master.zip```
* In terminal move to the unziped directory, ```cd InstPakg-master/```
* Install the python script ```python setup.py install``` (NOTE: run as sudo)
* In terminal type ```InstPakg``` and done!

How to use
----------
While inside ```InstPakg``` you move the selector with your up and down keyboard keys and hit enter to select the highlighted option.
#### Install Software
The first option "Install Software" will run you through a list of applications inside of the .json file selected(by default: DEFAULT.json), you either press ```y``` to install or ```n``` to not install.
#### Bulk Software Installer
This option is if you want to install all applications inside of the .json file(by default: DEFAULT.json) without any confirmation.
#### Select JSON file
"Select JSON file" is the option for selecting a .json file in which the program will install from. All .json files are located at .instpakg folder in your home directory.
#### Exit
Exits the python script.

Proper JSON file handling
----------
Please look at the [Wiki](https://github.com/Mozzo1000/InstPakg/wiki) for a detailed explanation.

License
-------
InstPakg is is distributed under the [MIT License](http://opensource.org/licenses/MIT).  
Read the LICENSE.md for more details.
