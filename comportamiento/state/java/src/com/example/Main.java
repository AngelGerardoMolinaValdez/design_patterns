package com.example;

// state
interface CarState {
    void handleState();
}

// concrete state
class CarStateStart implements CarState {
    public void handleState() {
        System.out.println("Auto encendido!");
    }
}

class CarStateOff implements CarState {
    public void handleState() {
        System.out.println("Auto apagdo!");
    }
}

// context
class Car {
    private CarState state;

    public Car(String model) {
        System.out.println("Auto " + model + " creado.");
        this.state = new CarStateOff();
    }

    public void setState(CarState state) {
        this.state = state;
    }

    public void printState() {
        state.handleState();
    }
    
}

public class Main {
    public static void main(String[] args) {
        Car car = new Car("Versa");
        CarStateStart stateStart = new CarStateStart();

        car.printState();
        car.setState(stateStart);
        car.printState();
    }
}
