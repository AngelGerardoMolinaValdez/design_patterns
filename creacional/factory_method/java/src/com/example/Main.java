package com.example;

interface CarFactory {
    Car createCar();
}


class FerrariFactory implements CarFactory {
    public Car createCar() {
        return new FerrariPortofino();
        
    }
}


class LamborghiniFactory implements CarFactory {
    public Car createCar() {
        return new LamborghiniGallardo();
        
    }
}


interface Car {
    void turnOn();

    void turnOff();
}


class FerrariPortofino implements Car {

    public FerrariPortofino() {
        System.out.println("Ferrari creado!!");
    }

    public void turnOn() {
        System.out.println("Ruuuuuuuuuuuuuuuuuuuuuun!!");
    }

    public void turnOff() {
        System.out.println("Ruuu........");
    }
}


class LamborghiniGallardo implements Car {

    public LamborghiniGallardo() {
        System.out.println("Lambo creado");
    }

    public void turnOn() {
        System.out.println("Ruuuuuuuuuuuuuuuuuuuuuun!!");
    }

    public void turnOff() {
        System.out.println("Ruuu........");
    }
}


public class Main {
    public static void clientCode(CarFactory factory) {
        Car car = factory.createCar();
        car.turnOn();
        car.turnOff();
    }

    public static void main(String[] args) {
        System.out.println("Iniciando sistema...\n");
        clientCode(new FerrariFactory());
        clientCode(new LamborghiniFactory());
    }
}
