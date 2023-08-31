package com.example;

// subject
interface Alumn {
    String validateCredentials();

}

// concrete subject
class SchoolFooBarAlumn implements Alumn {
    private String id;

    public SchoolFooBarAlumn(String id) {
        this.id = id;
    }

    public SchoolFooBarAlumn() {
        // vacio para permitir poder no ingresar la credencial
    }

    public String validateCredentials() {
        if(id == null) {
            return "No puede pasar";
        }
        return "Puede Pasar";
    }

}

// proxy
class CredentialValidator {
    public void validateCredential(Alumn alumn, String name) {
        System.out.println("Validando informacion del alumno " + name);
        System.out.println(alumn.validateCredentials());
        System.out.println("Siguiente alumno...");
    }
}

public class Main {
    public static void main(String[] args) {
        SchoolFooBarAlumn angel = new SchoolFooBarAlumn();        SchoolFooBarAlumn roberto = new SchoolFooBarAlumn("Roberto123");
        CredentialValidator proxy = new CredentialValidator();
        proxy.validateCredential(angel, "Angel");
        proxy.validateCredential(roberto, "Roberto");
    }
}
