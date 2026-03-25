import tensorflow as tf

# 간단한 수학문제 풀어보기
키 = 170
신발 = 260

# 문제 : 키와 신발사이즈는 어떤관련이 있을까요?

a = tf.Variable(0.1)
b = tf.Variable(0.2)

# 키로 신발사이즈를 추론해보자
# 경사 하강법을 사용하여 구하는 도구
opt = tf.keras.optimizers.Adam(learning_rate=0.1)

# minimize = 경사하강이 일어남
# 여기서 var_list는 경사하강법으로 업데이트 할 weight Variable 목록

def 손실함수():
    # return tf.square(실제값 - 예측값)
    return tf.square(260 - (키 * a + b) )

# 300번 반복 (데이터가 많고 횟수가 많으면 많을수록 좋음)
for i in range(300):
    with tf.GradientTape() as t:
        결과 = 손실함수()
    opt.apply_gradients(zip(t.gradient(결과, [a, b]), [a, b]))
print(a.numpy(),b.numpy())