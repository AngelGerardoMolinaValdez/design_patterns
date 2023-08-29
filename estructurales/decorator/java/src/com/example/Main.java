package com.example;

/**
 * Liquid
 */
interface Liquid {
    String drink();
}

/**
 * Water
 */
class Water implements Liquid {
    public String drink() {
        return "water";
    }
}

interface Flavor {
    String addFlavor();
}

class LemonFlavor implements Flavor {
    private Liquid liquid;

    public LemonFlavor(Liquid liquid) {
        this.liquid = liquid;
    }

    public String addFlavor() {
        return liquid.drink() + " with lemon flavor";
    }
}

public class Main {
    public static void main(String[] args) {
        Water water = new Water();
        LemonFlavor lemonFlavor = new LemonFlavor(water);
        System.out.println(lemonFlavor.addFlavor());
    }    
}
