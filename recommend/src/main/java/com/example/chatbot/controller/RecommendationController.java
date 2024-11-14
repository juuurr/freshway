package com.example.chatbot.controller;

import org.springframework.http.ResponseEntity;
import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.client.RestTemplate;
import org.springframework.beans.factory.annotation.Autowired;

import java.util.List;
import java.util.Map;

@Controller
public class RecommendationController {

    @Autowired
    private RestTemplate restTemplate;

    // 다른 경로에서만 사용
//    @GetMapping("/recommendations/all")
//    public ResponseEntity<Map<String, List<Map<String, Object>>>> getAllRecommendations() {
//        String url = "http://localhost:8000/recommendations/all";
//
//        // 외부 API 호출하여 추천 데이터 가져오기
//        Map<String, List<Map<String, Object>>> allRecommendations = restTemplate.getForObject(url, Map.class);
//
//        return ResponseEntity.ok(allRecommendations);
//    }
//
//    @GetMapping("/recommendations/all2")
//    public ResponseEntity<Map<String, List<Map<String, Object>>>> getAllRecommendations() {
//        String url = "http://localhost:8001/recommendations/all2";
//
//        // 외부 API 호출하여 추천 데이터 가져오기
//        Map<String, List<Map<String, Object>>> allRecommendations = restTemplate.getForObject(url, Map.class);
//
//        return ResponseEntity.ok(allRecommendations);
//    }

    @GetMapping("/recommendations/all")
    public ResponseEntity<Map<String, List<Map<String, Object>>>> getAllRecommendations() {
        String url = "http://localhost:8000/recommendations/all";
        // External API call to fetch recommendation data
        Map<String, List<Map<String, Object>>> allRecommendations = restTemplate.getForObject(url, Map.class);
        return ResponseEntity.ok(allRecommendations);
    }

    @GetMapping("/recommendations/all2")
    public ResponseEntity<Map<String, List<Map<String, Object>>>> getAllRecommendations2() {
        String url = "http://localhost:8001/recommendations/all2";
        // External API call to fetch recommendation data
        Map<String, List<Map<String, Object>>> allRecommendations = restTemplate.getForObject(url, Map.class);
        return ResponseEntity.ok(allRecommendations);
    }

    // /charts 경로는 그대로 유지
    @GetMapping("/charts.html")
    public String getCharts() {
        return "charts";  // charts.html 파일을 렌더링
    }

    @GetMapping("/index.html")
    public String getIndex() {
        return "index";  // index.html 파일을 렌더링
    }

    @GetMapping("/index2.html")
    public String getIndex2() {
        return "index2";  // index.html 파일을 렌더링
    }
}
