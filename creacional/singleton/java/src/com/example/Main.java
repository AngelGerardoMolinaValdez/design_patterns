package com.example;

class OriginalCredential {
    private static OriginalCredential instance;
    private String name;

    private OriginalCredential(String name){
        this.name = name;
        // se define el constructor privado para evitar instanciacion directa
        // es decir si se instancia directamente por "new"
    }

    public static OriginalCredential getInstance(String name) {
        if (instance == null) {
            instance = new OriginalCredential(name);
        }
        return instance;
    }

    public String getName() {
        return this.name;
    }
}

public class Main {
    public static void main(String[] args) {
        OriginalCredential myCredential = OriginalCredential.getInstance("Angel Molina");
        
        OriginalCredential yourCredential = OriginalCredential.getInstance("Foo Bar");

        System.out.println("La credencial original a nombre de:" + myCredential.getName());
        System.out.println("La credencial de alguien mas a nombre de:" + yourCredential.getName());
    }
}