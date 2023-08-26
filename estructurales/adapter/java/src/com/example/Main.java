package com.example;

interface API1 {
    void get(String typeCat);
}

interface API2 {
    void post(String typeCat);
}

class APICat1 implements API1 {
    public void get(String typeCat) {
        System.out.println("get to api cats!!");
    }
}

class APICat2 implements API2 {
    public void post(String typeCat) {
        System.out.println("post to api cat 2!");
    }
}

class API2Adapter implements API1 {
    private APICat2 newApi;

    public API2Adapter(APICat2 newApi) {
        this.newApi = newApi;
    }

    public void get(String typeCat) {
        newApi.post(typeCat);
    }
}

public class Main {
    public static void main(String[] args) {
        APICat1 api1 = new APICat1();
        APICat2 api2 = new APICat2();
        API2Adapter apiAdapter = new API2Adapter(api2);
        api1.get("Siames");
        apiAdapter.get("egipcio");
    }
}