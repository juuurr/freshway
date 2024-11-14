package com.example.chatbot.repository;

import com.example.chatbot.model.Patient;
import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.stereotype.Repository;

@Repository
public interface PatientRepository extends JpaRepository<Patient, Long> {
    // 필요한 추가 쿼리 메소드 작성 가능
}
