# Deployed on JETSON NANO  

It is recommended to burn a new SD card and to configure the environment directly in the system environment.  
**Configuration environment:** `JetPack4.6.1, Cuda10.2, Python3.6.9`  
## MediaPipe installation
Priority installation of [MediaPipe](https://github.com/google/mediapipe) packages. Refer to this [零基础入门Jetson Nano——MediaPipe双版本（CPU+GPU）的安装与使用](https://blog.csdn.net/qq_56548850/article/details/123981579?ops_request_misc=%257B%2522request%255Fid%2522%253A%2522171394895816800213081926%2522%252C%2522scm%2522%253A%252220140713.130102334..%2522%257D&request_id=171394895816800213081926&biz_id=0&utm_medium=distribute.pc_search_result.none-task-blog-2~all~sobaiduend~default-1-123981579-null-null.142^v100^pc_search_result_base7&utm_term=jetson%20nano%20mediapipe&spm=1018.2226.3001.4187)  

## Tensorflow installation  
When installing tensorflow on a Jetson Nano, the dependency library `h5py` installation reports an error.  
Refer to this [jetson nano使用tensorflow时h5py安装报错](https://blog.csdn.net/coco1234_1590/article/details/134476185?ops_request_misc=%257B%2522request%255Fid%2522%253A%2522171410996016800226530774%2522%252C%2522scm%2522%253A%252220140713.130102334..%2522%257D&request_id=171410996016800226530774&biz_id=0&utm_medium=distribute.pc_search_result.none-task-blog-2~all~sobaiduend~default-2-134476185-null-null.142^v100^pc_search_result_base7&utm_term=jetson%20nano%20tensorflow&spm=1018.2226.3001.4187) . You need to download the [h5py-3.1.0.tar.gz](https://github.com/h5py/h5py/releases) file and modify the `setup.py`.  
Change this 
```# Minimum supported versions of Numpy & Cython depend on the Python version
NUMPY_MIN_VERSIONS = [
    # Numpy    Python
    ('1.12',   "=='3.6'"),
    ('1.14.5', "=='3.7'"),
    ('1.17.5', "=='3.8'"),
    ('1.19.3', ">='3.9'"),]
```
to
```
# Minimum supported versions of Numpy & Cython depend on the Python version
NUMPY_MIN_VERSIONS = [
    # Numpy    Python
    # ('1.12',   "=='3.6'"),
    ('1.14.5', "=='3.7'"),
    ('1.17.5', "=='3.8'"),
    ('1.19.3', "=='3.6'"),]
```
Make sure `numpy` version is **1.19.x** and replace `Cython` version with **3.0.0a10**  

```
sudo pip3 install -U Cython==3.0.0a10
sudo python3 ./setup.py install
```
After successfully installing `h5py3.1.0`, download the `Jetpack4.6.1` version of `tensorflow` provided by [nvidia](https://developer.nvidia.cn/embedded/downloads) official website. Installing tensorflow


```
sudo pip install xxx/xxx/xxx.whl
```

## We need to install opencv-python
Reference [Howto-Install-Mediapipe-in-Jetson-Nano](https://github.com/Melvinsajith/How-to-Install-Mediapipe-in-Jetson-Nano). Since the OpenCV that comes with the Jetson system will cause some problems, opencv needs to be reinstalled here. The `remove` operation is completed after the `install`.
```
 sudo apt-get install python3-opencv 
 sudo apt-get remove python3-opencv
```

After deploying to `Jetson Nano`, due to the lack of memory on the Nano development board, an error occurs when calling multi-threaded playback of mp3 audio, as well as when calling the `pygame` library, it will not run. So in this branch of the code, the `pygame` library is removed, and the `GPIO` port on the development board is used to implement the mp3 audio playback function with the `BY8002` voice module.  

![ca8887bc235ab42e6f3b583cb2bd098.png](https://github.com/cccp421/CV-piano/blob/jetson/ca8887bc235ab42e6f3b583cb2bd098.png)
# run  
```
python3 run.py
```

## Jetson.GPIO User's Guide  
```
sudo pip install Jetson.GPIO
```
### Problems with GPIOs not working  
```
sudo chmod a+rw /dev/gpiochip0  
sudo chmod a+rw /dev/gpiochip1
```
