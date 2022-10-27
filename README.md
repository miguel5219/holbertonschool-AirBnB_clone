![image](https://user-images.githubusercontent.com/98335124/177196137-35b5a657-1f9d-45b3-8e96-45a0fd659660.png)

# Holberton School AirBnB Clone
***
## The Console
***

The console is the first segment of the AirBnB project at **Holberton School**. The goal of AirBnB project is to eventually deploy our server a simple copy of the AirBnB Website. A command interpreter is created in this segment to manage objects for the AirBnB website.

#### Functionalities of this command interpreter:
- Create a new object (ex: a new User or a new Place)
- Retrieve an object from a file, a database etc...
- Do operations on objects (count, compute stats, etc...)
- Update attributes of an object
- Destroy an object

####  Installation process
- Clone this repository: [Click here](https://github.com/TATTANRAM0X/holbertonschool-AirBnB_clone "Install")
- Access AirBnb directory: `cd holbertonschool-AirBnB_clone`
- Run hbnb(interactively): `./console` and enter command
- Run hbnb(non-interactively): `echo "<command>" | ./console.py`

#### How to use it?
| Command | Yes/No | Description |
| :------------: | :------------: | :------------: |
| all  | ✅  | Command that prints all string representation of all instances based or not on the class name Usage: - To show all instances of all classes: all - To show all instances of a specific class: all <class_name> |
| create | ✅ | Command that creates a new instance of a class, saves it to a JSON file and prints the id. Usage: create <class_name> |
| destroy | ✅ | Command that deletes an instance based on the class nameand id. It saves the change into the JSON file. Usage: destroy <class_name> <object_id> |
| EOF | ✅ | Command to exit the program  |
| help  | ✅  | It shows the docummented commands available in the console |
| quit | ✅ | Command to exit the program |
| show | ✅  | Command that prints the string representation of an instance based on the class name and id. Usage: show <class_name> <object_id> |