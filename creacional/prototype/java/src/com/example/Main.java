package com.example;

// prototype
interface IceCreamPrototype extends Cloneable {
    void printFlavor();
    void printSize();
}

// concrete prototype
class HolandaIceCream implements IceCreamPrototype {
    public String flavor;
    public String size;

    public HolandaIceCream(String flavor, String size) {
        this.flavor = flavor;
        this.size = size;
    }

    @Override
    protected HolandaIceCream clone() {
        try {
            return (HolandaIceCream) super.clone();
        } catch (CloneNotSupportedException e) {
            return null;
        }
    }

    public void printFlavor() {
        System.out.println("Helado sabor:" + flavor);
    }

    public void printSize() {
        System.out.println("Helado tamanio:" + size);
    }

    public void setFlavor(String flavor) {
        this.flavor = flavor;
    }
}

// client code
public class Main{
    public static void main(String[] args) {
        HolandaIceCream holandaIceCream = new HolandaIceCream("napolitano", "grande");
        holandaIceCream.printFlavor();
        holandaIceCream.printSize();

        HolandaIceCream holandaIceCreamCloned = holandaIceCream.clone();
        holandaIceCreamCloned.setFlavor("chocolate");
        holandaIceCreamCloned.printFlavor();
        holandaIceCreamCloned.printSize();
    }
}
