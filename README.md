# 🎓 Graduate Admission Prediction Model

TensorFlow를 활용하여 대학원 합격 여부를 예측하는 이진 분류 모델입니다.  
(GRE, GPA, Rank 데이터를 기반으로 합격 확률을 예측)

---

## 📌 프로젝트 소개

이 프로젝트는 간단한 머신러닝/딥러닝 모델을 통해  
지원자의 스펙(GRE 점수, GPA, 학교 등급)을 바탕으로  
대학원 합격 가능성을 예측하는 모델을 구현하는 것을 목표로 합니다.

---

## 🧠 사용 기술

- Python 3.x
- TensorFlow / Keras
- Pandas
- NumPy

---

## 📊 데이터셋 설명

| Feature | 설명 |
|--------|------|
| GRE    | GRE 점수 |
| GPA    | 학점 |
| Rank   | 학부 학교 등급 (1~4) |
| Admit  | 합격 여부 (0 or 1) |

---

26/03/27 진행
📌 MNIST 숫자 분류 (Softmax Regression)
파일명 : mnist_classification.py

TensorFlow 2.0을 활용하여 MNIST 데이터셋 기반의 숫자 분류 모델을 구현하였다.
Softmax Regression을 이용한 다중 클래스 분류 문제를 해결하고, 약 91%의 정확도를 달성함을 테스트 하였다.