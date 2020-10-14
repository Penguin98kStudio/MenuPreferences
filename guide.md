Apply The Guide on Menu/Preferences/Menu by Penguin/Settings - Lists
##### This setting if empty please run a toggle preference command and a file commands command once to fill the list with default options

Caution: The Settings - Lists is key to how the plugin works,
please modify only according to the guidelines


### Add/Remove commands from File Commands List Guide

in the "file_commands_list" add the command at end in the following way:

if command has no args:
	[Requires Input,Command Name(Alias), command]
	// datatypes
		 boolean     ,    string         , string

if command has args:
	[Requires Input,Command Name(Alias), [command, {"argname": argvalue}]]
	// datatypes
		boolean      ,    string         , [string,  {string:  argdatatype}]]

also in the "file_commands_freq": add a value at end,
this value determines the place(order) of the command if sorting is enabled,
else the command will be at end of the list


### Add/Remove preferences from Preferences List Guide
in the "preferences_list" add the preference at end in the following way:

if preference is boolean i.e true, false:
	[preference name]
else:
	[preference name, valueiftrue, valueiffalse]
or:
	[preference name, valueiftrue, valueiffalse, preference alias]

	the preference name is not case senstive
	the preference alias is what shows in the list

also in the "preferences_freq": add a value at end,
this value determines the place(order) of the preference if sorting is enabled,
else the command will be at end of the list
