package com.example;
import java.util.ArrayList;
import java.util.List;

interface LedStructure {
    String turnOn();
    String turnOff();
}

class Led implements LedStructure {
    private String color;

    public Led(String color) {
        this.color = color;
    }

    public String turnOn() {
        return "Encendiendo led " + color + "...";
    }

    public String turnOff() {
        return "Apagando led " + color + "...";
    }
}

class StripLed implements LedStructure {
    private List<Led> leds = new ArrayList<>();

    public void addLed(Led led) {
        leds.add(led);
    }

    public String turnOff() {
        List<String> turnOffLeds = new ArrayList<>();
        for (Led led : leds){
            turnOffLeds.add(led.turnOff());
        }
        return "Luces apagadas: [" + String.join("--- ", turnOffLeds) +"]";
    }

    public String turnOn() {
        List<String> turnOnLeds = new ArrayList<>();
        for (Led led : leds){
            turnOnLeds.add(led.turnOn());
        }
        return "Luces apagadas: [" + String.join("--- ", turnOnLeds) +"]";
    }
}

public class Main {
    public static void main(String[] args) {
        Led ledBlue = new Led("blue");
        Led ledRed = new Led("red");
        Led ledGreen = new Led("green");

        System.out.println(ledBlue.turnOn() + " " + ledBlue.turnOff());
        System.out.println(ledRed.turnOn() + " " + ledRed.turnOff());
        System.out.println(ledGreen.turnOn() + " " + ledGreen.turnOff());

        StripLed stripLed = new StripLed();
        stripLed.addLed(ledBlue);
        stripLed.addLed(ledRed);
        stripLed.addLed(ledGreen);

        System.out.println(stripLed.turnOn());
        System.out.println(stripLed.turnOff());

    }   
}