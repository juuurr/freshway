package com.example.chatbot.controller;

import com.example.chatbot.model.NutritionInfo;
import com.example.chatbot.model.Patient;  // 수정된 클래스 이름
import com.example.chatbot.repository.NutritionInfoRepository;
import com.example.chatbot.repository.PatientRepository;  // 수정된 리포지토리 이름
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.GetMapping;
import java.util.List;

@Controller
public class DataController {

    @Autowired
    private NutritionInfoRepository nutritionInfoRepository;

    @Autowired
    private PatientRepository patientRepository;  // 수정된 리포지토리 이름

    // NutritionInfo 데이터 반환
    @GetMapping("/api/nutrition-info")
    public List<NutritionInfo> getNutritionInfo() {
        return nutritionInfoRepository.findAll();
    }

    // Patient 데이터 반환
    @GetMapping("/api/patient-info")
    public List<Patient> getPatientInfo() {  // 수정된 클래스 이름
        return patientRepository.findAll();  // 수정된 리포지토리 이름
    }
}
