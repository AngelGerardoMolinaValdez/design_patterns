package com.example;

interface Operation {
    void start();
    void end();
}

class Logger implements Operation {
    public void start() {
        System.out.println("proceso start en logger");
    }

    public void end() {
        System.out.println("proceso end en logger");
    }
}

class Process implements Operation {
    public void start() {
        System.out.println("proceso start en process");
    }

    public void end() {
        System.out.println("proceso end en process");
    }
}

class Report implements Operation {
    public void start() {
        System.out.println("proceso start en report");
    }

    public void end() {
        System.out.println("proceso end en report");
    }
}

class SystemFoo {
    private Logger logger;
    private Process process;
    private Report report;

    public SystemFoo() {
        logger = new Logger();
        process = new Process();
        report = new Report();
    }

    public void on() {
        logger.start();
        process.start();
        report.start();
    }

    public void off() {
        logger.end();
        process.end();
        report.end();
    }
}

public class Main {
    public static void main(String[] args) {
        SystemFoo mySystem = new SystemFoo();
        mySystem.on();
        mySystem.off();
    }
}
