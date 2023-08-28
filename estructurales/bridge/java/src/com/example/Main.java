package com.example;

interface Car {
    void drive();
}

class AngelNissan implements Car {
    public void drive() {
        System.out.println("Run Ruuuuuuun...");
    }
}

abstract class Employee {
    protected Car car;

    public Employee(Car car) {
        this.car = car;
    }

    public abstract void driveCar();
}

class AngelEmployee extends Employee {
    public AngelEmployee(Car car) {
        super(car);
    }

    public void driveCar() {
        car.drive();
    }
}

public class Main {
    public static void main(String[] args) {
        AngelEmployee angel = new AngelEmployee(new AngelNissan());
        angel.driveCar();
    }        
}
