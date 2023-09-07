package com.example;

abstract class CompanySoftware {
    public void execute() {
        System.out.println("Ejecutando programa!");
        startProcess();
        updateData();
        applyChanges();
    }

    private void startProcess() {
        System.out.println("Iniciando proceso X");
    }

    private void updateData() {
        System.out.println("Actualizando informacion Y");
    }

    abstract protected void applyChanges();
}

class NewEmployeeImplementation extends CompanySoftware {
    protected void applyChanges() {
        System.out.println("Aplicando logica Z");
    }
}

public class Main {
    public static void main(String[] args) {
        NewEmployeeImplementation newSystemImplementation = new NewEmployeeImplementation();
        newSystemImplementation.execute();
    }
}
