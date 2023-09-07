package com.example;
// visitor
interface ProcessesValidator {
    void visitLaptop(Laptop laptop);
    void visitCellPhone(CellPhone cellPhone);
    void visitSmartTv(SmartTv smartTv);
}

// concrete visitor
class TechStoreSystem implements ProcessesValidator {
    public void visitLaptop(Laptop laptop) {
        System.out.println(laptop.ownerValue() + "compro una laptop");
    }

    public void visitCellPhone(CellPhone cellPhone) {
        System.out.println(cellPhone.ownerValue() + "compro un telefono");
    }

    public void visitSmartTv(SmartTv smartTv) {
        System.out.println(smartTv.ownerValue() + "compro una smart tv");
    }
}

// element
interface SmartDevice {
    void accept(ProcessesValidator visitor);
}

// concrete element
class CellPhone implements SmartDevice {
    private String owner;
    private String model;

    public CellPhone(String owner, String model) {
        this.owner = owner;
        this.model = model;
    }

    public String ownerValue() {
        return owner;
    }

    public String modelValue() {
        return model;
    }

    public void accept(ProcessesValidator visitor) {
        visitor.visitCellPhone(this);
    }
}

class Laptop implements SmartDevice {
    private String owner;
    private String model;

    public Laptop(String owner, String model) {
        this.owner = owner;
        this.model = model;
    }

    public String ownerValue() {
        return owner;
    }

    public String modelValue() {
        return model;
    }

    public void accept(ProcessesValidator visitor) {
        visitor.visitLaptop(this);
    }
}

class SmartTv implements SmartDevice {
    private String owner;
    private String model;

    public SmartTv(String owner, String model) {
        this.owner = owner;
        this.model = model;
    }

    public String ownerValue() {
        return owner;
    }

    public String modelValue() {
        return model;
    }

    public void accept(ProcessesValidator visitor) {
        visitor.visitSmartTv(this);
    }
}

public class Main {
    public static void main(String[] args) {
        CellPhone cellPhone = new CellPhone("Angel Molina", "Xiaomi");
        Laptop laptop = new Laptop("Raul Ramirez", "Razer");
        SmartTv smartTv = new SmartTv("Ana Rodriguez", "samsumg");

        TechStoreSystem TechStoreSystem = new TechStoreSystem();
        cellPhone.accept(TechStoreSystem);
        laptop.accept(TechStoreSystem);
        smartTv.accept(TechStoreSystem);
    }
}
