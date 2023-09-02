package com.example;

import java.util.List;
import java.util.ArrayList;
import java.util.Iterator;


class DaysWeekIterator<T> implements Iterator<T> {
    private List<T> data;
    private Integer index = 0;

    public DaysWeekIterator(List<T> data) {
        this.data = data;
    }

    public boolean hasNext() {
        return index < data.size();
    }

    public T next() {
        if (!hasNext()){
            throw new IndexOutOfBoundsException("Se ha terminado de iterar");
        }
        T result = data.get(index);
        index++;
        return result;
    }
}

class DaysWeekIterable<T> implements Iterable<T> {
    private List<T> data = new ArrayList<>();

    public void add(T value) {
        data.add(value);
    }

    public Iterator<T> iterator() {
        return new DaysWeekIterator<>(data);
    }
}

public class Main {
    public static void main(String[] args) {
        DaysWeekIterable<String> daysWeekCollection = new DaysWeekIterable<>();
        daysWeekCollection.add("lunes");
        daysWeekCollection.add("martes");
        
        for (String i : daysWeekCollection) {
            System.out.println("El valor es: " + i);
        }
    }
}
