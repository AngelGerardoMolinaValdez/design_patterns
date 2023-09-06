package com.example;

// strategy
interface BasicOperation {
    void operation(Integer num1, Integer num2);
}

// concrete strategy
class SumOperation implements BasicOperation {
    public void operation(Integer num1, Integer num2) {
        System.out.println(num1 + num2);
    }
}

class SubOperation implements BasicOperation {
    public void operation(Integer num1, Integer num2) {
        System.out.println(num1 - num2);
    }
}

// context
class BasicCalculator {
    private BasicOperation strategy;

    public BasicCalculator(BasicOperation strategy) {
        this.strategy = strategy;
    }

    public void setStrategy(BasicOperation strategy) {
        this.strategy = strategy;
    }
    
    public void strategy(Integer num1, Integer num2) {
        strategy.operation(num1, num2);
    }
}

public class Main {
    public static void main(String[] args) {
        SumOperation sumOperation = new SumOperation();
        SubOperation subOperation = new SubOperation();
        BasicCalculator calculator = new BasicCalculator(sumOperation);

        calculator.strategy(20, 25);
        calculator.setStrategy(subOperation);
        calculator.strategy(20, 25);
        
    }
}
