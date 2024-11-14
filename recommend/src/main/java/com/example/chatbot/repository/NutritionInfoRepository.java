package com.example.chatbot.repository;

import com.example.chatbot.model.NutritionInfo;
import org.springframework.data.jpa.repository.JpaRepository;

public interface NutritionInfoRepository extends JpaRepository<NutritionInfo, Long> {
}

