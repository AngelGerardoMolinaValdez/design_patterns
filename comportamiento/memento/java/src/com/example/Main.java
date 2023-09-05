package com.example;
import java.util.List;
import java.util.ArrayList;

// memento
class FileContentBackUp {
    private String content;

    public FileContentBackUp(String content){
        this.content = content;
    }

    public String contentValue() {
        return content;
    }
}

// originator
class FileObject {
    private String content;

    public void writeContent(String content) {
        this.content = content;
    }

    public FileContentBackUp saveContent() {
        return new FileContentBackUp(content);
        
    }

    public void restoreContent(FileContentBackUp backUp) {
        this.content = backUp.contentValue();
    }

    public String getContent() {
        return content;
    }
}

// caretaker
class FileManager {
    private List<FileContentBackUp> contents = new ArrayList<>();

    public void addContent(FileContentBackUp content) {
        contents.add(content);
    }

    public FileContentBackUp getContent(Integer index) {
        return contents.get(index);
    }
}

public class Main {
    public static void main(String[] args) {
        FileManager manager = new FileManager();
        FileObject fileObject = new FileObject();

        fileObject.writeContent("Primer version de mi archivo");
        FileContentBackUp backUp = fileObject.saveContent();
        manager.addContent(backUp);
        System.out.println("Contenido inicial: " + fileObject.getContent());

        fileObject.writeContent("Segunda version");
        backUp = fileObject.saveContent();
        FileContentBackUp lastChanges = manager.getContent(0);
        System.out.println("Contenido actual: " + fileObject.getContent());
        System.out.println("Ultimo contenido guardado: " + lastChanges.contentValue());
    }
}
