package com.example.chatbot.model;

import jakarta.persistence.*;
import lombok.Getter;
import lombok.Setter;

@Entity
@Table(name = "patients")
@Getter
@Setter
public class Patient {

    @Id
    @Column(name = "Patient_ID")
    private String id;  // Change Long to String if the ID is stored as a string in the database

    @Column(name = "Age")
    private int age;

    @Column(name = "Gender")
    private String gender;

    @Column(name = "Height_cm")
    private double height;

    @Column(name = "Weight_kg")
    private double weight;

    @Column(name = "Chronic_Diseases")
    private String chronicDiseases;

    @Column(name = "blood_pressure_mm_hg")
    private String bloodPressure;

    @Column(name = "Blood_Glucose_mg_dL")
    private double bloodGlucose;

    @Column(name = "Cholesterol_mg_dL")
    private double cholesterol;

    @Column(name = "Diagnosis")
    private String diagnosis;

    @Column(name = "Medications")
    private String medications;

    @Column(name = "Systolic_BP")
    private int systolicBp;

    @Column(name = "Diastolic_BP")
    private int diastolicBp;
}
