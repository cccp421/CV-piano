import tensorflow as tf
from tensorflow.keras import Sequential
from tensorflow.keras.layers import Conv2D, MaxPooling2D, Dense, Flatten
import os

UNTOUCH_FOLDER = "src/training_data/untouched"
TOUCH_FOLDER = "src/training_data/touched"
def start_training():
    # GPU设置保持不变，有助于动态分配内存
    gpus = tf.config.experimental.list_physical_devices('GPU')
    for gpu in gpus:
        tf.config.experimental.set_memory_growth(gpu, True)

    # 设置随机种子以避免数据划分时的重叠问题
    SEED = 2  # 你可以选择任何整数作为种子

    # 减少模型复杂度
    total_samples = len(os.listdir(TOUCH_FOLDER) + os.listdir(UNTOUCH_FOLDER))
    data = tf.keras.utils.image_dataset_from_directory(
        "src/training_data",
        image_size=(40,40),
        batch_size=total_samples // 5,
        validation_split=0.2,  # 直接在数据集划分时指定验证集比例
        subset="training",  # 指定当前分割为训练集
        seed=SEED  # 添加随机种子
    )

    # 使用数据集的validation_split特性，不再手动分割
    val_data = tf.keras.utils.image_dataset_from_directory(
        "src/training_data",
        image_size=(40,40),
        batch_size=total_samples // 5,
        validation_split=0.2,
        subset="validation",
        seed=SEED  # 同样在验证集划分时添加随机种子
    )

    model = Sequential([
        Conv2D(16, (3,3), padding='same', activation='relu', input_shape=(40,40,3)),  # 减少第一层卷积核
        MaxPooling2D(),
        Conv2D(8, (3,3), padding='same', activation='relu'),  # 减少第二层卷积核
        MaxPooling2D(),
        Flatten(),
        Dense(64, activation='relu'),  # 减少全连接层的神经元数量
        Dense(1, activation='sigmoid')
    ])

    model.compile(optimizer='adam',  # 保持adam优化器，因其效率较高
                  loss=tf.keras.losses.BinaryCrossentropy(from_logits=True),  # 使用logits形式损失函数，可能更高效
                  metrics=['accuracy'])
    print(model.summary())
    # 移除模型summary打印，减少训练时的输出
    hist = model.fit(data, epochs=23, validation_data=val_data)  # 减少训练轮次以加速训练过程

    # 移除可视化代码
    # 直接保存模型
    model.save('models/touch_detection_model.keras')

