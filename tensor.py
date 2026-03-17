import tensorflow as tf


텐서2 = tf.constant([6,7,8])

텐서3 = tf.constant([[1,2],[3,4]])

# 또는

텐서4 = tf.constant([[1,2],
                    [3,4]])

텐서5 = tf.constant([[3,4],
                    [5,6]])

# print(텐서3 * 텐서5)
# print(tf.matmul(텐서4,텐서5))

# print(tf.zeros(10))
# print(tf.zeros( [3,3] ))
# print(tf.zeros( [2,3,3] ))

몇차원텐서일까 = tf.constant([
    [
        [1,2,3,4],
        [4,1,2,4],
        [1,2,3,4]
    ],
    [
        [1,2,3,4],
        [1,2,3,14],
        [123,4,1,2]
    ]
])
# print(몇차원텐서일까.shape)

# 텐서 = tf.constant([3,4,5.0])
# print(텐서)


w = tf.Variable(1.3)
print(w)
print(w.numpy())

w.assign(2.77)
print(w)

