package com.example;

// receiver
class Door {
    void open() {
        System.out.println("Abriendo puerta");
    }

    void close() {
        System.out.println("Cerrando puerta");
    }
}

// command
interface Command {
    void execute();
}

// concrete command
class OpenDoorCommand implements Command {
    private Door door;

    public OpenDoorCommand(Door door) {
        this.door = door;
    }

    public void execute() {
        this.door.open();
    }
}

class CloseDoorCommand implements Command {
    private Door door;

    public CloseDoorCommand(Door door) {
        this.door = door;
    }

    public void execute() {
        this.door.close();
    }
}

// invoker
class SecurityGuard {
    private Command command;

    public void setCommand(Command command) {
        this.command = command;
    }

    public void receive() {
        this.command.execute();
    }
}

public class Main {
    public static void main(String[] args) {
        Door door = new Door();
        OpenDoorCommand openDoorCommand = new OpenDoorCommand(door);        CloseDoorCommand closeDoorCommand = new CloseDoorCommand(door);
        SecurityGuard securityGuard = new SecurityGuard();

        securityGuard.setCommand(openDoorCommand);
        securityGuard.receive();
        securityGuard.setCommand(closeDoorCommand);
        securityGuard.receive();
    }
}
