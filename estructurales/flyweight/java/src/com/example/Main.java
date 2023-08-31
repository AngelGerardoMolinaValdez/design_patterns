package com.example;
import java.util.Map;
import java.util.HashMap;
import java.util.List;
import java.util.ArrayList;
import java.util.Arrays;


// flyweight
interface Animal {
    void eat();
}

// concrete flyweight
class Pet implements Animal {
    private String name;
    private String food;

    public Pet(String name, String food) {
        this.name = name;
        this.food = food;
    }

    public void eat() {
        System.out.println(name + " esta comiendo: " + food);
    }
}

//client
class PetFeeder {
    private static Map<String, Animal> pets = new HashMap<>();

    public static Animal feed(String name, String food) {
        Animal pet = pets.get(name);
        if (pet == null) {
            pet = new Pet(name, food);
            pets.put(name, pet);
        }
        return pet;
    }
}

public class Main {
    public static void main(String[] args) {
    List<List<String>> pets = new ArrayList<>();
    List<String> odyData = new ArrayList<>(
        Arrays.asList("Ody", "Pollo"));
    pets.add(odyData);
    List<String> maxData = new ArrayList<>(
        Arrays.asList("Max", "Croquetas"));
    pets.add(maxData);
    for(List<String> petData : pets) {
        Animal pet = PetFeeder.feed(
            petData.get(0), petData.get(1));
        pet.eat();
    }
    }
}
