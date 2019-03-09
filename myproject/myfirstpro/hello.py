import tensorflow as tf

a = tf.constant(100)
b = tf.constant(200)

sess = tf.Session()

print(sess.run(a))
print(sess.run(b))

sess.close()