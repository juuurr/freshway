package com.example.chatbot.model;

import jakarta.persistence.*;
import lombok.Getter;
import lombok.Setter;

@Entity
@Table(name = "nutrition")
@Getter
@Setter
public class NutritionInfo {

    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Long id;

    @Column(name = "food_name")
    private String foodName;

    @Column(name = "energy_kcal")
    private Double energyKcal;  // Changed from 'double' to 'Double'

    @Column(name = "moisture_g")
    private Double moisture;    // Changed from 'double' to 'Double'

    @Column(name = "protein_g")
    private Double protein;     // Changed from 'double' to 'Double'

    @Column(name = "fat_g")
    private Double fat;         // Changed from 'double' to 'Double'

    @Column(name = "carbohydrate_g")
    private Double carbohydrate; // Changed from 'double' to 'Double'

    @Column(name = "sugar_g")
    private Double sugars;      // Changed from 'double' to 'Double'

    @Column(name = "sodium_mg")
    private Double sodium;      // Changed from 'double' to 'Double'

    @Column(name = "potassium_mg")
    private Double potassium;   // Changed from 'double' to 'Double'

    @Column(name = "calcium_mg")
    private Double calcium;     // Changed from 'double' to 'Double'

    @Column(name = "iron_mg")
    private Double iron;        // Changed from 'double' to 'Double'

    @Column(name = "vitamin_a_ug_rae")
    private Double vitaminA;    // Changed from 'double' to 'Double'

    @Column(name = "vitamin_c_mg")
    private Double vitaminC;    // Changed from 'double' to 'Double'

    @Column(name = "vitamin_d_ug")
    private Double vitaminD;    // Changed from 'double' to 'Double'

    @Column(name = "saturated_fat_g")
    private Double saturatedFattyAcids; // Changed from 'double' to 'Double'

    @Column(name = "cholesterol_mg")
    private Double cholesterol;  // Changed from 'double' to 'Double'

    // No need for explicit getter and setter methods because Lombok @Getter and @Setter generate them.
}
