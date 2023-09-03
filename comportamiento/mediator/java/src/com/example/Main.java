package com.example;

import java.util.List;
import java.util.ArrayList;


// mediator
abstract class ControlCenter {
    public abstract void requestOn(SmartDevice smartDevice, Boolean hasInternet);
    public abstract void requestOff(SmartDevice smartDevice, Boolean hasInternet);
}

// colleague
abstract class SmartDevice {
    public abstract void on(Boolean hasInternet);
    public abstract void off(Boolean hasInternet);
}

//concrete colleagues
class SmartLamp extends SmartDevice {
    private ControlCenter mediator;

    public SmartLamp(ControlCenter mediator) {
        this.mediator = mediator;
    }

    public void on(Boolean hasInternet) {
        this.mediator.requestOn(this, hasInternet);
    }

    public void off(Boolean hasInternet) {
        this.mediator.requestOn(this, hasInternet);
    }
}

class SmartHomeTeather extends SmartDevice {
    private ControlCenter mediator;

    public SmartHomeTeather(ControlCenter mediator) {
        this.mediator = mediator;
    }

    public void on(Boolean hasInternet) {
        this.mediator.requestOn(this, hasInternet);
    }

    public void off(Boolean hasInternet) {
        this.mediator.requestOn(this, hasInternet);
    }
}

class SmartTv extends SmartDevice {
    private ControlCenter mediator;

    public SmartTv(ControlCenter mediator) {
        this.mediator = mediator;
    }

    public void on(Boolean hasInternet) {
        this.mediator.requestOn(this, hasInternet);
    }

    public void off(Boolean hasInternet) {
        this.mediator.requestOn(this, hasInternet);
    }
}

// concrete mediator
class Home extends ControlCenter {
    private List<SmartDevice> devices = new ArrayList<>();

    public void addDevice(SmartDevice device) {
        devices.add(device);
    }

    public void requestOn(SmartDevice smartDevice, Boolean hasInternet) {
        String deviceName = smartDevice.getClass().getSimpleName();

        if (hasInternet) {
            System.out.println(
                deviceName + " se ha encendido");
        } else {
            System.out.println(
                deviceName + " no tiene internet y no puede" + "encenderse");
        }
    }

    public void requestOff(SmartDevice smartDevice, Boolean hasInternet) {
        String deviceName = smartDevice.getClass().getSimpleName();

        if (hasInternet) {
            System.out.println(
                deviceName + " se ha apagado");
        } else {
            System.out.println(
                deviceName + " no tiene internet y no puede" + "apagarse");
        }
    }
}

public class Main {
    public static void main(String[] args) {
        Home home = new Home();
        SmartLamp smartLamp = new SmartLamp(home);
        SmartTv smartTv = new SmartTv(home);
        SmartHomeTeather smartHomeTeather = new SmartHomeTeather(home);

        home.addDevice(smartLamp);
        home.addDevice(smartTv);
        home.addDevice(smartHomeTeather);

        smartLamp.on(true);
        smartTv.on(false);
        smartHomeTeather.on(true);

        smartLamp.off(false);
        smartTv.off(true);
        smartHomeTeather.off(true);

    }
}