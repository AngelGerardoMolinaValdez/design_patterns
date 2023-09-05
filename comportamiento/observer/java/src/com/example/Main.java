package com.example;

import java.util.List;
import java.util.ArrayList;

// observer / suscriber
class FactoryManager {
    private String name;

    public FactoryManager(String name) {
        this.name = name;
    }

    public void udpate() {
        System.out.println(name + " ha sido notificado de la creacion");
    }
}

class Car {
    private String model;
    private String color;
    
    public Car(String model, String color) {
        this.model = model;
        this.color = color;
    }

    public void data() {
        System.out.println(
            "El auto es modelo " + model + " y color " + color);
    }
}

// subject / publisher
class CarFactory {
    private List<FactoryManager> managers = new ArrayList<>();
    
    public void addManager(FactoryManager manager) {
        managers.add(manager);
    }

    private void notifyChange() {
        for (FactoryManager manager : managers) {
            manager.udpate();
        }
    }

    public Car createCar(String model, String color) {
        notifyChange();
        return new Car(model, color);
    }
}

public class Main {
    public static void main(String[] args) {
        FactoryManager manager = new FactoryManager("Saul");
        CarFactory factory = new CarFactory();

        factory.addManager(manager);

        Car car = factory.createCar("versa", "naranja");
    }
}