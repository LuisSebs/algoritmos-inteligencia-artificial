PATH_TO_FX=<path to javafx>/lib
WORKING_DIRECTORY="$(shell pwd)/classes"

compile:
	javac --module-path $(PATH_TO_FX) --add-modules=javafx.fxml,javafx.controls,java.logging -d ./classes --source-path ./src/pakuman/classes/ src/pakuman/classes/pacman/MainPacMan.java
	javac --module-path $(PATH_TO_FX) --add-modules=javafx.fxml,javafx.controls,java.logging -d ./classes --source-path ./src/pakuman/classes/ src/pakuman/classes/pacman/Controller.java
	cp -r ./src/pakuman/classes/pacman/data ./classes/pacman

run:
	java -Duser.dir=$(WORKING_DIRECTORY) --module-path $(PATH_TO_FX) --add-modules=javafx.fxml,javafx.controls,java.logging pacman.MainPacMan

.PHONY: clean
clean:
	rm -rf classes

