package com.example;
import java.util.ArrayList;
import java.util.List;

// abstract factory
interface CellPhoneFactory {
    HighEndCellPhone createHighEndCellPhone();
    MidRangeCellPhone createMidRangeCellPhone();
}

// concrete factory
class SamsungFactory implements CellPhoneFactory {
    public HighEndCellPhone createHighEndCellPhone() {
        return new GalaxyS28CellPhone();
    }

    public MidRangeCellPhone createMidRangeCellPhone() {
        return new GalaxyA51CellPhone();
    }
}

class XiaomiFactory implements CellPhoneFactory {
    public HighEndCellPhone createHighEndCellPhone() {
        return new Mi10TProCellPhone();
    }

    public MidRangeCellPhone createMidRangeCellPhone() {
        return new RedmiNote9CellPhone();
    }
}

// abstract product
interface HighEndCellPhone {
    void turnOn();
}

interface MidRangeCellPhone {
    void turnOn();
}

// concrete product
class GalaxyS28CellPhone implements HighEndCellPhone {
    public void turnOn() {
        System.out.println("Gama alta Galaxy S28");
    }
}

class GalaxyA51CellPhone implements MidRangeCellPhone {
    public void turnOn() {
        System.out.println("Gama media Galaxy A51");
    }
}

class RedmiNote9CellPhone implements MidRangeCellPhone {
    public void turnOn() {
        System.out.println("gama media redmi note 9");
    }
}

class Mi10TProCellPhone implements HighEndCellPhone {
    public void turnOn() {
        System.out.println("gama alta mi 10t pro");
    }
}


public class Main {
    public static void cellPoneMarket(List<CellPhoneFactory> factories) {
        for(CellPhoneFactory factory : factories) {
            HighEndCellPhone highEndCellPhone = factory.createHighEndCellPhone();
            MidRangeCellPhone midRangeCellPhone = factory.createMidRangeCellPhone();

            highEndCellPhone.turnOn();
            midRangeCellPhone.turnOn();
        }
    }

    public static void main(String [] args) {
        List<CellPhoneFactory> factories = new ArrayList<>();
        factories.add(new XiaomiFactory());
        factories.add(new SamsungFactory());
        cellPoneMarket(factories);
    }
}
