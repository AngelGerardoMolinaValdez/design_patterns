package com.example;

// abstract handler
interface AlumnsGroupHandler {
    void setNextGroup(AlumnsGroupHandler group);
    
    // chain
    void study(String level);
}

// handler
class PrimarySchoolGroup implements AlumnsGroupHandler {
    private AlumnsGroupHandler group;

    public void setNextGroup(AlumnsGroupHandler group) {
        this.group = group;
    }

    public void study(String level) {
        if (level == "primary") {
            System.out.println("Study in primary school");
        } else {
            this.group.study(level);
        }
    }
}

class HighSchoolGroup implements AlumnsGroupHandler {
    private AlumnsGroupHandler group;

    public void setNextGroup(AlumnsGroupHandler group) {
        this.group = group;
    }

    public void study(String level) {
        if (level == "high") {
            System.out.println("Study in high school");
        } else {
            this.group.study(level);
        }
    }
}

class UniversitySchoolGroup implements AlumnsGroupHandler {
    private AlumnsGroupHandler group;

    public void setNextGroup(AlumnsGroupHandler group) {
        this.group = group;
    }

    public void study(String level) {
        if (level == "university") {
            System.out.println("Study in university school");
        } else if (group == null){
            System.out.println("The school year has ended");
        } else {
            this.group.study(level);
        }
    }
}

public class Main {
    public static void main(String[] args) {
        PrimarySchoolGroup primaryStudentGroup = new PrimarySchoolGroup();
        HighSchoolGroup highStudentGroup = new HighSchoolGroup();
        UniversitySchoolGroup universityStudentGroup = new UniversitySchoolGroup();

        primaryStudentGroup.setNextGroup(highStudentGroup);
        highStudentGroup.setNextGroup(universityStudentGroup);

        // client
        primaryStudentGroup.study("primary");
        primaryStudentGroup.study("high");
        primaryStudentGroup.study("university");        primaryStudentGroup.study("nothing");
    }
}