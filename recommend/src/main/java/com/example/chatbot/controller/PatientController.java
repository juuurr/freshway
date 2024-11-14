package com.example.chatbot.controller;

import com.example.chatbot.model.NutritionInfo;
import com.example.chatbot.model.Patient;
import com.example.chatbot.repository.NutritionInfoRepository;
import com.example.chatbot.repository.PatientRepository;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.web.bind.annotation.GetMapping;

import java.util.List;

@Controller
public class PatientController {

    @Autowired
    private PatientRepository patientRepository;

    @Autowired
    private NutritionInfoRepository nutritionInfoRepository;

    @GetMapping("/patient.html")
    public String getPatients(Model model) {
        // DB에서 환자 데이터를 가져옵니다.
        List<Patient> patients = patientRepository.findAll();

        // 모델에 환자 데이터를 추가
        model.addAttribute("patients", patients);

        // templates/patient.html을 렌더링
        return "patient";  // patient.html을 렌더링
    }

    @GetMapping("/menu.html")
    public String getNutritions(Model model) {
        // Fetch and add data to the model
        List<NutritionInfo> nutrition = nutritionInfoRepository.findAll();
        model.addAttribute("nutritionList", nutrition);
        return "menu";  // This should correspond to the 'nutrition.html' template
    }

}
