package com.example;
import java.util.List;
import java.util.ArrayList;

// product
class Michelada {
    public String size;
    public String model;
    public List<String> condiments = new ArrayList<>();

    public void describe() {
        System.out.println("Marca: " + model);
        System.out.println("Tamano: " + size);
        System.out.println(
            "Condimentos: " + String.join(", ", condiments));
    }
}

// builder
interface AbstractMicheladaBuilder {
    void defineSize(String size);
    void defineModel(String model);
    void addCondiments(String condiment);
    Michelada build();
}

// concrete builder
class MicheladaBuilder implements AbstractMicheladaBuilder {
    private Michelada miche = new Michelada();
        
    public void defineModel(String model) {
        miche.model = model;
    }

    public void defineSize(String size) {
        miche.size = size;
    }

    public void addCondiments(String condiment) {
        miche.condiments.add(condiment);
    }

    public Michelada build() {
        return miche;
    }

}

// director
class MicheladaMaker {
    public Michelada makeMichelada(MicheladaBuilder builder) {
        builder.defineSize("grandota");
        builder.defineModel("corona");
        builder.addCondiments("preparado de salsas picantes");
        return builder.build();
    }
}

// client code
public class Main {
    public static void main(String[] args) {
        MicheladaMaker director = new MicheladaMaker();
        Michelada michelada = director.makeMichelada(new MicheladaBuilder());
        michelada.describe();
    }
}
